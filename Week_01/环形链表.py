class ListNode:
	def __init__(self,x):
		self.val=x
		self.next=None

class Solution:
	def hasCycle(self,head):
		"双指针法，time:O(n),step:O(1)"
		if head==None or head.next==None:
			return False
		slow=head
		fast=head.next
		while slow != fast:
			if fast==None or fast.next==None:
				return False
			slow=slow.next
			fast=fast.next.next
		return True

if __name__=="__main__":
	head=[3,2,0,-4]
	pos=1
	s=Solution()
	value=s.hasCycle(head)
	print(value)