class TrieNode:
    def __init__(self):
        self.isEnd = False
        self.links = [None] * 26
class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            charIndex = ord(c)-ord('a')
            newNode = TrieNode()
            if not node.links[charIndex]:
                node.links[charIndex] = newNode
            node = node.links[charIndex]
        node.isEnd = True

    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            charIndex = ord(c)-ord('a')
            if not node.links[charIndex]:
                return False
            # keep traversing the trie
            node = node.links[charIndex]
        print(node.isEnd)
        return node.isEnd
        

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for c in prefix:
            if not node.links[ord(c)-ord('a')]:
                return False
            # keep traversing the trie
            node = node.links[ord(c)-ord('a')]
        return True
        