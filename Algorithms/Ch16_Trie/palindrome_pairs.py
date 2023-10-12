import collections
import pdb

class TrieNode:
    def __init__(self):
        self.word = False
        self.children = collections.defaultdict(TrieNode)
        self.word_id = -1
        self.palindrome_word_ids = []

class Trie:
    def __init__(self):
        self.root = TrieNode()

    @staticmethod
    def is_palindrome(word):
        return word[::]==word[::-1]

    def insert(self, index, word:str)->None:
        """
        index: a word index in a list.
        """
        node = self.root
        for i, char in enumerate(reversed(word)):
            if self.is_palindrome(word[0:len(word)-i]):
                node.palindrome_word_ids.append(index)
            node = node.children[char]
        node.word_id = index

    def search(self, index, word):
        result = []
        node = self.root

        # Palindrome Check 1
        while word:
            if node.word_id>=0:
                if self.is_palindrome(word):
                    result.append([index, node.word_id])
            if not word[0] in node.children:
                return result
            node = node.children[word[0]]
            word = word[1:]

        # Palindrome Check 2
        if node.word_id>=0 and node.word_id!=index:
            result.append([index, node.word_id])

        # Palindrome Check 3
        for palindrome_word_id in node.palindrome_word_ids:
            result.append([index, palindrome_word_id])

        return result

class Solution:
    def palindrome_pairs_check(self, words):
        trie = Trie()

        for i, word in enumerate(words):
            trie.insert(i, word)

        results = []
        for i, word in enumerate(words):
            results.extend(trie.search(i, word))

        return results

words = ["abcd","dcba","lls","s","sssll"]
sol = Solution()
print(sol.palindrome_pairs_check(words))

