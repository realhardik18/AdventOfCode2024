def generate_combinations(input_str):
    grid = input_str.splitlines()
    dot_positions = []
    for i, row in enumerate(grid):
        for j, char in enumerate(row):
            if char == '.':
                dot_positions.append((i, j))    
    combinations = []    
    for position in dot_positions:
        i, j = position        
        modified_grid = [list(row) for row in grid]
        modified_grid[i][j] = '#'                
        combinations.append('\n'.join(''.join(row) for row in modified_grid))
    
    return combinations
