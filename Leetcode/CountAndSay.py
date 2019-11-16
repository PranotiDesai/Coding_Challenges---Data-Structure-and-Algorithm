s="1"
if(n==1):
    return "1"
while n > 1:
    result = []
    count = 1
    for i in range(0,len(s)):
        if i > 0 and s[i] == s[i-1]:
            count=count+1
            result[len(result)-1] = str(count) +s[i]
        else:
            count = 1
            result.append(str(count) +s[i])
            i=i+1
    s='' .join(result)      
    n -=1
return s
