def parse_input(input_text):
    lines = input_text.rstrip('\n').split('\n')
    
    grid = []
    start_col = None
    
    for row, line in enumerate(lines):
        grid.append(list(line))
        if 'S' in line:
            start_col = line.index('S')
    
    return grid, start_col


def simulate_beams(grid, start_col):
    height = len(grid)
    width = len(grid[0]) if grid else 0
    
    active_beams = {(0, start_col)}
    split_count = 0
    
    for row in range(height - 1):
        next_row = row + 1
        new_beams = set()
        
        for beam_row, beam_col in active_beams:
            if beam_row != row:
                continue
            
            if beam_col < 0 or beam_col >= width:
                continue
            
            next_cell = grid[next_row][beam_col]
            
            if next_cell == '^':
                split_count += 1
                left_col = beam_col - 1
                right_col = beam_col + 1
                
                if left_col >= 0:
                    new_beams.add((next_row, left_col))
                if right_col < width:
                    new_beams.add((next_row, right_col))
            elif next_cell == '.' or next_cell == 'S':
                new_beams.add((next_row, beam_col))
        
        active_beams = new_beams
    
    return split_count


def solve(input_text):
    grid, start_col = parse_input(input_text)
    
    split_count = simulate_beams(grid, start_col)
    
    print(f"\nGrid size: {len(grid[0])}x{len(grid)}")
    print(f"Total splits: {split_count}")
    return split_count


if __name__ == "__main__":
    with open("D7_01_input.txt", "r") as f:
        input_text = f.read()
    
    solve(input_text)
