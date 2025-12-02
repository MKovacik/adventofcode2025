def is_invalid_id(n):
    s = str(n)
    length = len(s)
    if length % 2 != 0:
        return False
    half = length // 2
    return s[:half] == s[half:]


def find_invalid_ids_in_range(start, end):
    invalid_ids = []
    
    s_end = str(end)
    max_len = len(s_end)
    
    for pattern_len in range(1, max_len // 2 + 1):
        pattern_start = max(1, 10 ** (pattern_len - 1))
        pattern_end = 10 ** pattern_len - 1
        
        for p in range(pattern_start, pattern_end + 1):
            s_pattern = str(p)
            repeated = int(s_pattern * 2)
            
            if start <= repeated <= end:
                invalid_ids.append(repeated)
    
    return invalid_ids


def solve(input_text):

    input_text = input_text.strip().rstrip(',')
    ranges = input_text.split(',')
    
    all_invalid_ids = []
    
    for r in ranges:
        r = r.strip()
        if not r:
            continue
        start, end = map(int, r.split('-'))
        invalid_ids = find_invalid_ids_in_range(start, end)
        all_invalid_ids.extend(invalid_ids)
        if invalid_ids:
            print(f"{start}-{end} has {len(invalid_ids)} invalid ID(s): {sorted(invalid_ids)}")
        else:
            print(f"{start}-{end} contains no invalid IDs.")
    
    total = sum(all_invalid_ids)
    print(f"\nTotal sum of all invalid IDs: {total}")
    return total


if __name__ == "__main__":
    with open("D2_01_input.txt", "r") as f:
        input_text = f.read()
    
    solve(input_text)
