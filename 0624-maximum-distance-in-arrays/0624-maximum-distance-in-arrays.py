class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        min_val = arrays[0][0]
        max_val = arrays[0][-1]
        
        # Variable to store the maximum distance
        max_distance = 0
        
        # Loop through the arrays starting from the second array
        for i in range(1, len(arrays)):
            # Calculate distance using the global min with the current array's max
            max_distance = max(max_distance, abs(arrays[i][-1] - min_val))
            
            # Calculate distance using the global max with the current array's min
            max_distance = max(max_distance, abs(max_val - arrays[i][0]))
            
            # Update the global min and max with the current array
            min_val = min(min_val, arrays[i][0])
            max_val = max(max_val, arrays[i][-1])
        
        return max_distance