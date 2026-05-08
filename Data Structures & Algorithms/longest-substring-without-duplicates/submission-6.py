class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        l = 0
        r = 1
        maxL = 1
        li = [s[l]]
        
        while r < len(s):
            if s[r] not in li:
                li.append(s[r])
                maxL = max(maxL, len(li))
                r += 1

            else:
                l += 1
                r = l + 1 
                li = [s[l]]
            #print(s[l], l, r, li , maxL)
            
        return maxL
