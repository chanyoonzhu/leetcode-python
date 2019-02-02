class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        
        """
        - O(n^2)
        - graph BFS
        - time limit exceeded: generating graph is O(n^2)
        
        def connected(word1, word2):
            diff = 0
            for i in range(len(word1)):
                if word1[i] != word2[i]:
                    diff += 1
            if diff == 1:
                return True
            return False
        
        graph = collections.defaultdict(list)
        for i in range(len(wordList)):
            for j in range(len(wordList)):
                if i != j and connected(wordList[i], wordList[j]):
                    graph[i].append(j)
        
        q = []
        visited = [0] * len(wordList)
        for i in range(len(wordList)):
            if connected(beginWord, wordList[i]):
                q.append((i, 1))
                visited[i] = 1
        while q:
            curr = q[0]
            del q[0]
            if wordList[curr[0]] == endWord:
                return curr[1] + 1
            else:
                neighbors = [i for i in graph[curr[0]] if visited[i] == 0]
                for i in neighbors:
                    q.append((i, curr[1] + 1))
                    visited[i] = 1
        return 0
        """
        
    
        """
        - O(n^2)
        - with words removed from wordList everytime visited
        """
        def connected(word1, word2):
            diff = 0
            for i in range(len(word1)):
                if word1[i] != word2[i]:
                    diff += 1
            if diff == 1:
                return True
            return False
        
        def findNextWords(begin, words):
            idx, res = [], []
            for i in range(len(words)):
                if begin != words[i] and connected(begin, words[i]):
                    idx.insert(0, i)
            for i in idx:
                res.append(words[i])
                del words[i]
            return res
        
        nextWords = findNextWords(beginWord, wordList)
            
        q = []
        for w in nextWords:
            q.append((w, 1))
        while q:
            curr = q[0]
            del q[0]
            if curr[0] == endWord:
                return curr[1] + 1
            else:
                neighbors = [w for w in findNextWords(curr[0], wordList)]
                for w in neighbors:
                    q.append((w, curr[1] + 1))
        return 0
    
        """
        - O(n)
        - store Wordlist as sets, find if all possible one distance word is in wordlist
        """
        wordSet = set(wordList)
        visited = set()
        if endWord not in wordSet:
            return 0
        
        q = [(beginWord, 1)]
        while q:
            word, distance = q.pop(0) # q.pop(0)
            if word == endWord:
                return distance
            for i in range(len(word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    candidate = word[:i] + c + word[i+1:]
                    if candidate != word and candidate in wordSet and candidate not in visited:
                        q.append[(candidate, distance + 1)]
                        visited.add(candidate)
        return 0
        

sl = Solution()
begin = "hit"
end = "cog"
words = ["hot","dot","dog","lot","log","cog"]
print(sl.ladderLength(begin, end, words))