class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        if not strs:
            return ""

        for st in strs[1:]:
            while not st.startswith(prefix):
                prefix = prefix [:-1]
        if not prefix:
            return ""
        
        return prefix