def removeElement(self,nums,val):
    i=0
    length=len(nums)
    while i<length:
        if nums[i]==val:
            print(nums[i])
            nums.remove(nums[i])
            length = length - 1
            continue
        i=i+1
