class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans=[]
        ansd={}
        for ch in strs:
            arr = [0]*26
            for s in ch:
                ss = ord(s)- ord('a')
                arr[ss]+=1
            if tuple(arr) in ansd.keys():
                ansd[tuple(arr)].append(ch)
            else:
                ansd[tuple(arr)] = [ch]
        return list(ansd.values())
