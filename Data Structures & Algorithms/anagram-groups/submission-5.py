class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupes = defaultdict(list)
        for mot in strs:
            cle = "".join(sorted(mot))
            groupes[cle].append(mot)
        
        return list(groupes.values())