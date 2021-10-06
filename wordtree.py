
class WordTree:
    def __init__(self):
        self.root = WordNode("")
    def add_word(self, word):
        self.root.add_word(word)
    def has_word(self, word):
        return self.root.has_word(word)
    def get_intersect(self, words):
        return self.root.get_intersect("", words)

class WordNode:
    def __init__(self, content):
        self.content = content
        self.isfinal = False
        self.nexts = {}
    def add_word(self, word):
        if word == "":
            self.isfinal = True
        else:
            first = word[0]
            rest = word[1:]
            if first in list(self.nexts):
                self.nexts[first].add_word(rest)
            else:
                self.nexts[first] = WordNode(first)
                self.nexts[first].add_word(rest)
    def has_word(self, word):
        if word == "":
            return self.isfinal
        else:
            first = word[0]
            rest = word[1:]
            if first in list(self.nexts):
                return self.nexts[first].has_word(rest)
            else:
                return False
    def get_intersect(self, word, words):
        candidates = []
        if (len(words)==0) and self.isfinal:
            candidates += [""]
        if word != "":
            first = word[0]
            rest = word[1:]
            if first in list(self.nexts):
                if (rest == "") and (len(words)>0):
                    cands = self.nexts[first].get_intersect(words[0], words[1:])
                elif (rest == ""):
                    if self.nexts[first].isfinal:
                        cands = [""]
                    else:
                        cands = []
                else:
                    cands = self.nexts[first].get_intersect(rest, words)
                cands = [first+cand for cand in cands]
                candidates += cands
        if len(words) > 0:
            word = words[0]
            words = words[1:]
            first = word[0]
            rest = word[1:]
            if first in list(self.nexts):
                if (rest == "") and (len(words)>0):
                    cands = self.nexts[first].get_intersect(words[0], words[1:])
                elif (rest == ""):
                    if self.nexts[first].isfinal:
                        cands = [""]
                    else:
                        cands = []
                else:
                    cands = self.nexts[first].get_intersect(rest, words)
                cands = [first.upper()+cand for cand in cands]
                candidates += cands
        return candidates
