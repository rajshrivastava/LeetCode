class TrieNode:
    def __init__(self):
        self.endOfWord = False
        self.children = dict()
        
class Solution:
    def getTrie(self, dictionary):
        root = TrieNode()
        for word in dictionary:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]

                if node.endOfWord == True: #if we have already reached a root
                    break
                    
            node.endOfWord = True
        
        return root
                
        
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = self.getTrie(dictionary)
        
        replaced_sentence = ''
        for word in sentence.split(' '):
            node = trie
            replaced_word = ''
            for i, ch in enumerate(word):
                if ch in node.children:
                    node = node.children[ch]
                    replaced_word += ch
                    if node.endOfWord:
                        break
                else:
                    replaced_word = word
                    break
            replaced_sentence += replaced_word + ' '
        
        return replaced_sentence[:-1]
        
