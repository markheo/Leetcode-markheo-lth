class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dct = {}
        tmp = [''.join(sorted(ch)) for ch in strs]
        for i in range(len(strs)):
            if tmp[i] not in dct:
                dct[tmp[i]] = [strs[i]]

            else:
                dct[tmp[i]].append(strs[i])
        return list(dct.values())
        