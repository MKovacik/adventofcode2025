def parse_input(input_text):
    lines = input_text.rstrip('\n').split('\n')
    
    grid = []
    start_col = None
    
    for row, line in enumerate(lines):
        grid.append(list(line))
        if 'S' in line:
            start_col = line.index('S')
    
    return grid, start_col


def count_timelines(grid, start_col):
    height = len(grid)
    width = len(grid[0]) if grid else 0
    
    active_beams = {(0, start_col): 1}
    
    for row in range(height - 1):
        next_row = row + 1
        new_beams = {}
        
        for (beam_row, beam_col), timeline_count in active_beams.items():
            if beam_row != row:
                continue
            
            if beam_col < 0 or beam_col >= width:
                continue
            
            next_cell = grid[next_row][beam_col]
            
            if next_cell == '^':
                left_col = beam_col - 1
                right_col = beam_col + 1
                
                if left_col >= 0:
                    key = (next_row, left_col)
                    new_beams[key] = new_beams.get(key, 0) + timeline_count
                if right_col < width:
                    key = (next_row, right_col)
                    new_beams[key] = new_beams.get(key, 0) + timeline_count
            elif next_cell == '.' or next_cell == 'S':
                key = (next_row, beam_col)
                new_beams[key] = new_beams.get(key, 0) + timeline_count
        
        active_beams = new_beams
    
    total_timelines = sum(active_beams.values())
    
    return total_timelines


def solve(input_text):
    grid, start_col = parse_input(input_text)
    
    total_timelines = count_timelines(grid, start_col)
    
    print(f"\nGrid size: {len(grid[0])}x{len(grid)}")
    print(f"Total timelines: {total_timelines}")
    return total_timelines


if __name__ == "__main__":
    with open("D7_02_input.txt", "r") as f:
        input_text = f.read()
    
    solve(input_text)
