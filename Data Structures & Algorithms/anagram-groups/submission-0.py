class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for candidate in strs:
            count = [0] * 26
            for c in candidate:
                count[ord(c) - ord('a')] += 1
            
            groups[tuple(count)].append(candidate)

        return list(groups.values())
