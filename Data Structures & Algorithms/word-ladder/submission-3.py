class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        patternsToNextWords = defaultdict(list)
        # build adjlist
        # *ot: [hot, not]
        for word in wordList:
            for c in range(len(word)):
                pattern = word[:c] + '*' + word[c+1:]
                patternsToNextWords[pattern].append(word)

        visited = set([beginWord])
        q = deque([beginWord])
        count = 1
        print(patternsToNextWords)
        while q:
            for i in range(len(q)):
                cur = q.popleft()
                if cur == endWord:
                    return count
                for c in range(len(cur)):
                    pattern = cur[:c] + '*' + cur[c+1:]
                    print(pattern)
                    for neighbor in patternsToNextWords[pattern]:
                        if neighbor not in visited:
                            q.append(neighbor)
                            visited.add(neighbor)
            count += 1
        return 0
        

