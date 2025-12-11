def count_adjacent_rolls(grid, row, col):
    rows = len(grid)
    cols = len(grid[0])
    count = 0
    
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == 0 and dc == 0:
                continue
            nr, nc = row + dr, col + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if grid[nr][nc] == '@':
                    count += 1
    
    return count


def find_accessible_rolls(grid):
    accessible = []
    
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == '@':
                adjacent = count_adjacent_rolls(grid, row, col)
                if adjacent < 4:
                    accessible.append((row, col))
    
    return accessible


def remove_rolls(grid, positions):
    new_grid = [list(row) for row in grid]
    
    for row, col in positions:
        new_grid[row][col] = '.'
    
    return [''.join(row) for row in new_grid]


def solve(input_text):
    lines = input_text.strip().split('\n')
    
    grid = []
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
        grid.append(line)
    
    total_removed = 0
    
    while True:
        accessible = find_accessible_rolls(grid)
        if not accessible:
            break
        
        total_removed += len(accessible)
        grid = remove_rolls(grid, accessible)
    
    print(f"\nTotal rolls removed: {total_removed}")
    return total_removed


if __name__ == "__main__":
    with open("D4_02_input.txt", "r") as f:
        input_text = f.read()
    
    solve(input_text)
