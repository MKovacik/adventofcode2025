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


def solve(input_text):
    lines = input_text.strip().split('\n')
    
    grid = []
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
        grid.append(line)
    
    accessible = find_accessible_rolls(grid)
    total = len(accessible)
    
    print(f"\nAccessible paper rolls: {total}")
    return total


if __name__ == "__main__":
    with open("D4_01_input.txt", "r") as f:
        input_text = f.read()
    
    solve(input_text)
