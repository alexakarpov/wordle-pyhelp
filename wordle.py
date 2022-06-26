#!/usr/bin/env python3

import argparse, os, sys, re


def my_range(start, end, step):
    while start <= end:
        yield start
        start += step

def split(word):
    return [char for char in word]

def exclude(words, chars):
    l = len(words)
    for i in my_range(0, l-1, 1):
        for c in chars:
            if c in words[i]:
                words[i] = 'X'
                continue
    res = list(filter(lambda w: w != 'X', words))
    return res

def somewhere(words, chars):
    s = set(chars)
    return list(filter(lambda w: len(set(w).intersection(s)) == len(s), words))

def pin(words, patstr):
    pat = re.compile(patstr)
    return list(filter(lambda w: pat.match(w), words))

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--pinned", type=str, help="the pattern of the regexp-ish form 'a.b..' for the 'green' letters", default=".....")
    parser.add_argument("-s", "--somewhere", type=str, help="characters present in unknown positions ('yellow' letters)", default="")
    parser.add_argument("-x", "--exclude", type=str, help="eliminated characters", default="")
    parser.add_argument("dictionary", help="words list to use")
    args = parser.parse_args()

    dict = args.dictionary

    with open(dict) as f:
        words = f.readlines()

        if args.exclude != "":
            words = exclude(words, args.exclude)
        if args.somewhere != "":
            words = somewhere(words, args.somewhere)
        if args.pinned != "":
            words = pin(words, args.pinned)

        print(f"{len(words)} words remain:")

        try:
            for w in words:
                print(w, end='')
        except BrokenPipeError:
            # Python flushes standard streams on exit; redirect remaining output
            # to devnull to avoid another BrokenPipeError at shutdown
            devnull = os.open(os.devnull, os.O_WRONLY)
            os.dup2(devnull, sys.stdout.fileno())
            sys.exit(1)  # Python exits with error code 1 on EPIPE
