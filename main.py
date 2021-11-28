import argparse
import os
import pickle
import sys
#from IPython import embed
from tqdm import tqdm
from itertools import combinations
from itertools import permutations
from wordtree import WordTree
from wordtree import WordNode

raw_words = "words.txt"
word_tree = "words.pkl"


def make_tree():
    print("Constructing word tree")
    f = open(raw_words, "r")
    words = f.readlines()
    f.close()
    words = [word[:-1].lower() for word in words]
    tree = WordTree()
    for word in tqdm(words):
        tree.add_word(word)
    return tree

def get_tree():
    try:
        f = open(word_tree, "rb")
        print("Loading word tree")
        tree = pickle.load(f)
        f.close()
        return tree
    except:
        tree = make_tree()
        f = open(word_tree, "wb")
        pickle.dump(tree, f)
        f.close()
        return tree

if __name__ == "__main__":
    if len(sys.argv) > 1:
        parser = argparse.ArgumentParser(
            description="Generator of Rad Names from Decent Paper Acronyms"
        )
        parser.add_argument(
            "words",
            type=str,
            nargs="+",
            help="Paper title words.",
        )
        parser.add_argument(
            "--ordered",
            action="store_true",
            help="Preserve word order.",
        )
        parser.add_argument(
            "--minwords",
            type=int,
            default=0,
            help="Minimum number of used words. (default 0 => use all.)",
        )
        args = parser.parse_args()
        words = args.words
        preserve_order = args.ordered
        use_all = args.minwords in (0, len(words))
        minwords = 1
        if not use_all:
            minwords = args.minwords
    else:
        print()
        print("Please input paper title words separated by spaces")
        words = input(">").split(" ")

        preserve_order = input("Preserve word order? y/n >") == "y"
        use_all = input("Force use of all words? y/n >") == "y"
        minwords = 1
        if not use_all:
            minwords = eval(input("Minimum number of used words: >"))

    tree = get_tree()
    words = [word.lower() for word in words]

    orders = []
    if preserve_order and use_all:
        orders = [words]
    elif preserve_order and (not use_all):
        for count in range(minwords, len(words)+1):
            orders += combinations(words, count)
    elif (not preserve_order) and use_all:
        orders += permutations(words)
    elif (not preserve_order) and (not use_all):
        for count in range(minwords, len(words)+1):
            orders += permutations(words, count)
    print()
    print("Computing possible cool names")
    names = []
    namesdesc = {}
    for order in tqdm(orders):
        description = " ".join([word[0].upper() + word[1:] for word in order])
        ns = tree.get_intersect(order)
        names += ns
        for name in ns:
            namesdesc[name] = description

    print()
    print("Results:")
    names = list(dict.fromkeys(names))
    names.sort(key=len, reverse=False)
    for name in names:
        print("    ", name, "  -  ", namesdesc[name])
