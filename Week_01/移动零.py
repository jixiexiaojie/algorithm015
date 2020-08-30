class Solution:
	def moveZeroes(self,nums):
		"frist: time:O(n),step:O(n)"
		j=0
		for i in range(len(nums)):
			if nums[i]!=0:
				nums[i],nums[j]=nums[j],nums[i]
				j+=1

	def moveZeroes(self,nums):
		"second: time:O(n),step:O(n)"
		j=0
		for i in range(len(nums)):
			if nums[i]!=0:
				nums[j]=nums[i]
			if i!=j:
				nums[i]=0
			j+=1
if __name__=="__main__":
	nums=[0,1,0,3,12]
	s=Solution()
	value=s.moveZeroes(nums)
	print(value)
