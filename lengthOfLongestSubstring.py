class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = ""
        tmp_val = res 
        for c in list(s):
            if c not in tmp_val: 
                tmp_val = f"{tmp_val}{c}"
            else: 
                idx = tmp_val.index(c)
                tmp_val = tmp_val[idx+1::] + c
            if len(tmp_val) > len(res):
                res = tmp_val 
        return len(res)