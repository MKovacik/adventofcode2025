def parse_input(input_text):
    lines = input_text.strip().split('\n')
    
    ranges = []
    
    for line in lines:
        line = line.strip()
        if not line:
            break
        
        start, end = line.split('-')
        ranges.append((int(start), int(end)))
    
    return ranges


def merge_ranges(ranges):
    if not ranges:
        return []
    
    sorted_ranges = sorted(ranges, key=lambda x: x[0])
    merged = [sorted_ranges[0]]
    
    for start, end in sorted_ranges[1:]:
        last_start, last_end = merged[-1]
        
        if start <= last_end + 1:
            merged[-1] = (last_start, max(last_end, end))
        else:
            merged.append((start, end))
    
    return merged


def count_fresh_ids(ranges):
    merged = merge_ranges(ranges)
    total = 0
    
    for start, end in merged:
        total += end - start + 1
    
    return total


def solve(input_text):
    ranges = parse_input(input_text)
    
    total = count_fresh_ids(ranges)
    
    print(f"\nTotal fresh ingredient IDs: {total}")
    return total


if __name__ == "__main__":
    with open("D5_02_input.txt", "r") as f:
        input_text = f.read()
    
    solve(input_text)
