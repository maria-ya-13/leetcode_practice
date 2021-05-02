# Easy python solution
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        return [list(row) for row in zip(*matrix)]    
      
# Normal solution
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        new_num_rows = len(matrix[0])
        new_matrix = [[] for i in range(new_num_rows)]
        
        for i in range(len(matrix)):
            for j in range(new_num_rows):
                new_matrix[j].append(matrix[i][j])
        return new_matrix
    
