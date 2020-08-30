class Solution():
	def threeSum(self,nums):
		if len(nums)<3:return None
		nums.sort()
		res=set()
		for k,v in enumerate(nums):
			if k>len(nums)-1:break
			l,r=0,len(nums)-1
			while l<r:
				Sum=nums[l]+nums[k]+nums[r]
				if Sum>0:
					r-=1
				elif Sum<0:
					l+=1
				else:
					res.add((nums[l],nums[r],nums[k]))
					l+=1
					r-=1
		return list(map(list,res))
if __name__=="__main__":
	nums=[-1,0,1,2,-1,-4]
	s=Solution()
	k=s.threeSum(nums)
	print(k)
