class Solution:
    def lengthOfLongestSubstring(self, s):
        dic={}
        start=0
        output=0
        for i,val in enumerate(s):
            if val in dic:
                start=max(start,dic[val]+1)
            if(output<  i-start+1):
                output=i-start+1
            dic[val]=i
        return output
                
    
            
            
                
        
