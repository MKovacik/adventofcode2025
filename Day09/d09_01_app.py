def parse_input(input_text):
    lines = input_text.strip().split('\n')
    
    red_tiles = []
    for line in lines:
        if line.strip():
            x, y = line.strip().split(',')
            red_tiles.append((int(x), int(y)))
    
    return red_tiles


def calculate_rectangle_area(tile1, tile2):
    x1, y1 = tile1
    x2, y2 = tile2
    
    width = abs(x2 - x1)
    height = abs(y2 - y1)
    
    if width == 0 or height == 0:
        return 0
    
    return (width + 1) * (height + 1)


def find_largest_rectangle(red_tiles):
    max_area = 0
    best_pair = None
    
    for i in range(len(red_tiles)):
        for j in range(i + 1, len(red_tiles)):
            tile1 = red_tiles[i]
            tile2 = red_tiles[j]
            
            area = calculate_rectangle_area(tile1, tile2)
            
            if area > max_area:
                max_area = area
                best_pair = (tile1, tile2)
    
    return max_area, best_pair


def solve(input_text):
    red_tiles = parse_input(input_text)
    
    max_area, best_pair = find_largest_rectangle(red_tiles)
    
    print(f"\nNumber of red tiles: {len(red_tiles)}")
    print(f"Best pair: {best_pair}")
    print(f"Largest rectangle area: {max_area}")
    return max_area


if __name__ == "__main__":
    with open("D9_01_input.txt", "r") as f:
        input_text = f.read()
    
    solve(input_text)
