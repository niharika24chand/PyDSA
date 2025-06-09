class TrieNode: #Defines a class to represent a single node in the Trie.
    def __init__(self):
        self.children = {} #This dictionary stores references to child TrieNode objects, with keys being characters of the wor
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode() #Creates the root node of the Trie.

    def insert(self, word):
        node = self.root #Starts the insertion process from the root node.
        for char in word:
            if char not in node.children:  #Checks if the character is already a child of the current node.
                node.children[char] = TrieNode() #If the character is not present, a new TrieNode is created and added to children.
            node = node.children[char] #Moves to the child node corresponding to the current character.
        node.is_end_of_word = True

    def search(self, word):
        node = self.root #Starts searching from the root node.
        for char in word:
            if char not in node.children: #Checks if the current character exists in the children of the current node.
                return False
            node = node.children[char] #Moves to the child node corresponding to the current character.
        return node.is_end_of_word

t = Trie()
t.insert("apple")
t.insert("app")
print(t.search("app"))
print(t.search("apple"))
print(t.search("appl"))