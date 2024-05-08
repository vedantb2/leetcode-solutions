class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_score = sorted(score, reverse=True)
        medals = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        result = []

        for s in score:
            rank = sorted_score.index(s) + 1
            if rank <= 3:
                result.append(medals[rank - 1])
            else:
                result.append(str(rank))
        return result
        