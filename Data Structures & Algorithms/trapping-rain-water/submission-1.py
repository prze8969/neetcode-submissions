class Solution:
    def trap(self, height: List[int]) -> int:
        l =0
        r=len(height)-1
        lefgreatest=-1
        lef=[]
        for i in range(r+1):
            if height[i] > lefgreatest:
                lefgreatest = height[i]
            lef.append(lefgreatest)
        righgreatest=-1
        righ=[]
        for i in range(r,-1,-1):
            if height[i] >righgreatest:
                righgreatest = height[i]
            righ.append(righgreatest)
        
        trappedwater=0
        righ = righ[::-1]
        
        for i in range(len(height)):
            water = min(lef[i],righ[i])-height[i]
            trappedwater+=water
        return trappedwater

