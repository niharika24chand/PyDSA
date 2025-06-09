class t_node:
    def __init__(self):
        self.children = {}
        self.is_eow = False #eow=end of word

class Trie:
    def __init__(self):
        self.root = t_node()

    def insert(self, wrd):
        node = self.root
        for ch in wrd:
            if ch not in node.children:
                node.children[ch] = t_node()
            node = node.children[ch]
        node.is_eow = True

    def search(self, wrd):
        node = self.root
        for ch in wrd:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.is_eow

t = Trie()
t.insert("OM")
t.insert("Shiva")
t.insert("Anayra")
t.insert("Aanaya")
print(t.search("Anayra"))
print(t.search("Priya"))
print(t.search("shiva"))