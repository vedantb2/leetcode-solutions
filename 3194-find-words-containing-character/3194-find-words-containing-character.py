class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        indices = []
        for i in range(0, len(words)):
            if x in words[i]:
                indices.append(i)
        return indices