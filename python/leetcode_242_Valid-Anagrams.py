#hashmap #97ms 14.5memory
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countS = {}
        countT = {}
        for i in range(len(s)):
            #countS[s[i]] = 1 + countS[s[i]]  目標為此式子但以程式表示得做轉換         
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        for c in countS:
            if countS[c] != countT.get(c,0):
                return False
            
        return True

#sort    #103ms 15.2memory
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        return sorted(s) == sorted(t)   
    
    
#快速法時間最短    #45ms 14.3memory
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        return Counter(s) == Counter(t)
        
