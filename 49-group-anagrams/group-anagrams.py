class Solution(object):
    def groupAnagrams(self, strs):
        """
        First thing that comes to mind is create a group of anagram by using count of letters in alphabet as encoding.
        """
        res = collections.defaultdict(list)

        for s in strs:
            res[str(sorted(s))].append(s)
        return res.values()