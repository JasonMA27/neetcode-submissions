class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        rMax = -1
        
        for i in range(len(arr) - 1, -1, -1):
            newMax = max(rMax, arr[i])
            arr[i] = rMax
            rMax = newMax
        return arr

            
                