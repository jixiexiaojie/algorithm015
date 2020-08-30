class Solution():
	def maxArea(self,height):
		“time:O(n),step:O(1)”
		left,right,res=0,len(height)-1,0
		while left<right:
			if height[left]<height[right]:
				res=max(res,height[left]*(right-left))
				left+=1
			else:
				res=max(res,height[right]*(right-left))
				right-=1
		return res
if __name__=="__main__":
	height=[1,8,6,2,5,4,8,3,7]
	s=Solution()
	value=s.maxArea(height)
	print(value)