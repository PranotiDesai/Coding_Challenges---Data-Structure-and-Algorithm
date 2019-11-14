def twoSum(self,num,target):
    for i in range(len(num)):
        left= num[i+1:]
        for j in range(len(left)):
            if (num[i]+left[j])==target:
                return i, j+i+1
