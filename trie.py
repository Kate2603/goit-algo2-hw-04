class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        self.value = None

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def put(self, key, value=None):
        if not isinstance(key, str):
            raise ValueError("Key має бути рядком")
        node = self.root
        for char in key:
            node = node.children.setdefault(char, TrieNode())
        node.is_end_of_word = True
        node.value = value

    def get(self, key):
        if not isinstance(key, str):
            raise ValueError("Key має бути рядком")
        node = self.root
        for char in key:
            if char not in node.children:
                return None
            node = node.children[char]
        return node.value if node.is_end_of_word else None

    def _collect_words(self, node, prefix, results):
        if node.is_end_of_word:
            results.append(prefix)
        for char, child in node.children.items():
            self._collect_words(child, prefix + char, results)

    def get_all_words(self):
        results = []
        self._collect_words(self.root, "", results)
        return results
