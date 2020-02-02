 def longestCommonPrefix(self, strs):
      """
      :type strs: List[str]
      :rtype: str
      """
      longestprefix=""
      if len(strs)==0:
          return longestprefix
      minlen = len(strs[0])
      for i in range(len(strs)):
          minlen = min(len(strs[i]), minlen)


      i=0
      while i<minlen:
          char= strs[0][i]
          for j in range(1,len(strs)):
              print(j)
              if strs[j][i]!= char:
                  return longestprefix

          longestprefix= longestprefix+char
          i+=1
      return longestprefix
