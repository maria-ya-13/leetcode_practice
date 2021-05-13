# https://leetcode.com/problems/max-area-of-island/

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def is_on_map(line, pos):
            if 0 <= pos < len(grid[0]) and 0 <= line < len(grid):
                return True
            return False
        
        def get_area(line,pos):
            if is_on_map(line, pos):
                if not grid[line][pos]:
                    return 0
                grid[line][pos]=0    
                return 1 + get_area(line, pos+1) + get_area(line, pos-1)+ get_area(line+1, pos)+ get_area(line-1, pos)  
            return 0           
        
        areas = [0,]       
        for line in range(len(grid)):
            for pos in range(len(grid[0])):
                if grid[line][pos]:
                    areas.append(get_area(line, pos))
        return max(areas)   
