 def largestRectangleArea(self, heights):
      st=list()
      area=0
      max_area=0
      i=0
      #for i in range(len(heights)-1):
      while i < len(heights):
          if len(st)==0 or (heights[st[-1]] < heights[i]):
              st.append(i)
              i+=1
          else:
              top = st.pop()
              if len(st)==0:
                  area=heights[top]*i
              else:
                  area= heights[top]*(i-st[-1]-1)
              if(area)> max_area:
                  max_area= area

      while len(st)!=0:
          top = st.pop()
          if len(st)==0:
              area= heights[top]*i
          else:
              area = heights[top]*(i- st[-1]-1)
          if area> max_area:
              max_area = area
      return max_area
                
