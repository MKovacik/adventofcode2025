def parse_input(input_text):
    lines = input_text.strip().split('\n')
    
    ranges = []
    ingredient_ids = []
    parsing_ranges = True
    
    for line in lines:
        line = line.strip()
        if not line:
            parsing_ranges = False
            continue
        
        if parsing_ranges:
            start, end = line.split('-')
            ranges.append((int(start), int(end)))
        else:
            ingredient_ids.append(int(line))
    
    return ranges, ingredient_ids


def is_fresh(ingredient_id, ranges):
    for start, end in ranges:
        if start <= ingredient_id <= end:
            return True
    return False


def find_fresh_ingredients(ranges, ingredient_ids):
    fresh = []
    
    for ingredient_id in ingredient_ids:
        if is_fresh(ingredient_id, ranges):
            fresh.append(ingredient_id)
    
    return fresh


def solve(input_text):
    ranges, ingredient_ids = parse_input(input_text)
    
    fresh = find_fresh_ingredients(ranges, ingredient_ids)
    total = len(fresh)
    
    print(f"\nFresh ingredient IDs: {total}")
    return total


if __name__ == "__main__":
    with open("D5_01_input.txt", "r") as f:
        input_text = f.read()
    
    solve(input_text)
