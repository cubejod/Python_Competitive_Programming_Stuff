'''
solves leetcode 208 https://leetcode.com/problems/implement-trie-prefix-tree/description

you might have to play around with what TrieNode stores in some problems

try to precompute everything you can in harder problems (ex number of words with a given prefix can be found by keeping a count in TrieNode that gets +1ed every insertion)
point of trie is to get an O(n^2) brute force down to O(n)
so pls don't add any O(n) stuff in bc then whats the point of using trie
'''
class TrieNode:
    def __init__(self):
        self.children={}
        self.is_end=False

class Trie:

    def __init__(self):
        self.root=TrieNode()
        

    def insert(self, word: str) -> None:
        cur=self.root
        for i in range(len(word)):
            if word[i] not in cur.children:
                cur.children[word[i]]=TrieNode()
            cur=cur.children[word[i]]
        cur.is_end=True
        

    def search(self, word: str) -> bool:
        cur=self.root
        for i in range(len(word)):
            if word[i] in cur.children:
                cur=cur.children[word[i]]
            else:
                return False
        return cur.is_end

    def startsWith(self, prefix: str) -> bool:
        cur=self.root
        for i in range(len(prefix)):
            if prefix[i] in cur.children:
                cur=cur.children[prefix[i]]
            else:
                return False
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)