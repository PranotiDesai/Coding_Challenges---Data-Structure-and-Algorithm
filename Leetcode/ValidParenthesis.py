def isValid(self, s):
      """
      :type s: str
      :rtype: bool
      """
      stack_s =[]
      for ch in s:
          if ch == '(' or ch=='{' or ch=='[':
              stack_s.append(ch)
          elif len(stack_s)> 0 and ch == ')' and stack_s.pop() == '(':
              continue
          elif len(stack_s)> 0 and ch ==']' and stack_s.pop() == '[':
              continue
          elif len(stack_s)> 0 and ch =='}' and stack_s.pop() == '{':
              continue
          else:
              return False
      return len(stack_s)==0
