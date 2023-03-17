class TrieNode:
    # Initialize your data structure here.
    def __init__(self):
        self.word = False
        self.children = {}


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for i in word:
            if i not in node.children:
                node.children[i] = TrieNode()
            node = node.children[i]
        node.word = True

    def search(self, word: str) -> bool:
        node = self.root
        for i in word:
            if i not in node.children:
                return False
            node = node.children[i]
        return node.word

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for i in prefix:
            if i not in node.children:
                return False
            node = node.children[i]
        return True


if __name__ == '__main__':
    obj = Trie()
    obj.insert("apple")
    param_2 = obj.search("app")
    print(param_2)
    param_3 = obj.startsWith("app")
    print(param_3)
