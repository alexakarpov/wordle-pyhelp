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
    parser.add_argument("-f", "--fixed", type=str, help="the pattern of the regexp-ish form 'a.b..'", default="-----")
    parser.add_argument("-s", "--some", type=str, help="characters present in unknown position", default="")
    parser.add_argument("-x", "--exclude", type=str, help="eliminated characters", default="")
    args = parser.parse_args()

    with open("english3.txt") as f:
        lines = f.readlines()
        lines = list(map(lambda line: line.lower().strip(), lines))
        words = list(filter(lambda w: len(w) == 5, lines))
        res = words
        if args.exclude != "":
            excluded = exclude(words, args.exclude)
            print(f"{len(excluded)} after exclusion")
            res = excluded
        if args.fixed != "":
            fixed = pin(res, args.fixed)
            res = fixed
            print(f"got {len(fixed)} remaining")

    for w in res:
        print(w)
