class Solution:        
    def buildTrie(self, paths):
        self.trie = dict()
        for path in paths:
            curr = self.trie
            for subFolder in path[1:].split('/'):                
                curr = curr.setdefault(subFolder, dict())
                if '#' in curr:
                    break
            curr['#'] = dict()
    
    def removeSubfolders(self, folder: List[str]) -> List[str]:     
        def findAllPaths(node, pathSoFar):
            if '#' in node:
                result.append(pathSoFar)
                return

            for child in node.keys():
                findAllPaths(node[child], pathSoFar + '/' + child)
            
        self.buildTrie(folder)
        result = []
        findAllPaths(self.trie, pathSoFar='')  
        return result
        
