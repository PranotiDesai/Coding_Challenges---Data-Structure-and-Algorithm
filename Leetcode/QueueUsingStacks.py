class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.push_st=[]
        self.pop_st=[]
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.push_st.append(x)
        
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if len(self.pop_st)!=0:
            return self.pop_st.pop()
        else:
            
            while len(self.push_st)!= 0:
                self.pop_st.append(self.push_st.pop())
            return self.pop_st.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if len(self.pop_st)!= 0:
            return self.pop_st[-1]
        else:
            while len(self.push_st)!=0:
                self.pop_st.append(self.push_st.pop())
            return self.pop_st[-1]
        
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if len(self.push_st)==0 and len(self.pop_st)==0:
            return True
        else:
            return False
