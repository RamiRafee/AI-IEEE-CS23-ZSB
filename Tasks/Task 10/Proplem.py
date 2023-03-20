class Solution:
    def calculate_solution(height):
        """
        

        Parameters
        ----------
        height : List
            List of heights of black blocks.

        Returns
        -------
        list
            the soluiton of the first trapped water encountered.
            and
            the start index of the trap.
            and
            the finsih index of the trap.

        """
        solution = 0
        start = 0
        
        
        """Condition to know whether to iterate from right to left OR the opposite"""
        if height[0] <= height[-1]: 
            
            i = 0 ##iterating from left to right to find the frist trap
            while i < len(height):
                finish_in = i
                j = i + 1
                while j < len(height):
                    if height[i] <= height[j]:
                        finish_in = j
                        break
                    elif i == 0 and j == len(height) - 1:
                        solution = (height[i] - height[j]) * (j - i - 1)
                        i += 1
                        continue
                    j += 1
                j = i
                while j < finish_in:
                    solution += height[i] - height[j]
                    j += 1
                if i != finish_in:
                    i = finish_in
                else:
                    i += 1
                break ##break because we want the first trap encountered
        else:
            start = len(height) - 1 ##iterating from right to left to find the first trap
            i = len(height) - 1
            while i >= 0:
                finish_in = i
                j = i - 1
                while j >= 0:
                    if height[i] <= height[j]:
                        finish_in = j
                        break
                    j -= 1
                j = i
                while j > finish_in:
                    solution += height[i] - height[j]
                    j -= 1
                if i != finish_in:
                    i = finish_in
                else:
                    i -= 1
                break##break because we want the first trap encountered
        
        
        ##returning the indecies in order
        if(start<=finish_in):
            #print(solution,start,finish_in)
            return [solution,start,finish_in]
        else:
            #print(solution,finish_in,start)

            return [solution,finish_in+1,start+1] ## adding one to handle the exclusive slicing in python when deleting
   
    def trap(self, height: list[int]) -> int:
        solution = 0
        
        
        while(len(height)>1):

            temp = Solution.calculate_solution(height) ##finding the first trap and the water inside it
            solution += temp[0]
            del (height[temp[1]:temp[2]]) ##deleting that trap and starting all over as long as the list still has values
            #print(height)
            
        
        return solution