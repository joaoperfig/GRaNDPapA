# GRaNDPapA: Generator of Rad Names from Decent Paper Acronyms

Trying to publish a new machine learning model and can't write a decent title for your paper?
Are all of your titles just sequences of 10 keywords?
Jealous of the cool kids with their sweet paper names like "ALBERT" and "ELMo"?
Well look no further, GRaNDPapA will take whatever buzzwords you want in the title and make a cool Acronym out of it.

### Examples:

* GRaNDPapA: Generator of Rad Names from Decent Paper Acronyms
* LaSAgNe Clustering: Language Space Agnostic News Clustering
* SeAtBeLT: Sentence Attention for Bert Label Transformers
* ReCUsAntS: Rejuvenation of Cells Using Ant Saliva

### Usage:

1. Install python 3
2. Clone this repository
3. Run `python3 main.py`
4. Input the set of keywords you want in your acronym

### Extra parameters:

**Preserve word order**: If true, will only create acronyms that maintain the provided word order.
    **Warning**: If false, pay attention to the exponential growth of the number of possible permutations for longer lists of words.

**Force use of all words**: If true, will ensure all words are used in the Acronym.
    **Warning**: There is a known bug that sometimes acronyms can be generated that are missing the last word.

### Implementation details:

For efficiency, a tree is constructed to represent all the words in the English language.
Each word string will represent a path down this tree and will end in a node labeled as "final" if the word exists.
Each node keeps track of all outgoing letters that lead to possible words from that point.
When the document words are introduced, this tree is intersected with the tree of possible acronyms for those words.
At each node, only outgoing nodes that follow the rules of the Acronym generation are maintained.
Paths down this intersected tree to final nodes are words that exist in the English language and are valid acronyms for the given words.


### Credits

Developed for [Priberam Labs](https://labs.priberam.com/)
List of all English words by [dwyl](https://github.com/dwyl/english-words)
