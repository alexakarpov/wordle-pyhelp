import argparse
import re

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
                words[i] = 'xxxxx'
    res = list(filter(lambda w: w != 'xxxxx', words))
    return res

def pin(words, patstr):
    pat = re.compile(patstr)
    return list(filter(lambda w: pat.match(w), words))

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--pinned", type=str, help="the pattern of the regexp-ish form 'a.b..' for the 'green' letters", default=".....")
    parser.add_argument("-s", "--some", type=str, help="characters present in unknown position (NOT READY YET)", default="")
    parser.add_argument("-x", "--exclude", type=str, help="eliminated characters", default="")
    args = parser.parse_args()

    with open("dictionary.txt") as f:
        words = f.readlines()
        if args.exclude != "":
            excluded = exclude(words, args.exclude)
            words = excluded
        if args.pinned != "":
            pinned = pin(words, args.pinned)
            words = pinned

    print(f"{len(words)} words remained:")
    for w in words:
        print(w, end='')
