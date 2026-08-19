class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrammap=defaultdict(list)
        for word in strs:
            key_map="".join(sorted(word))
            anagrammap[key_map].append(word)
        return list(anagrammap.values())