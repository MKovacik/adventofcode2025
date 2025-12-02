def is_invalid_id(n):
    s = str(n)
    length = len(s)
    
    for pattern_len in range(1, length // 2 + 1):
        if length % pattern_len == 0:
            pattern = s[:pattern_len]
            repetitions = length // pattern_len
            if repetitions >= 2 and pattern * repetitions == s:
                return True
    return False


def find_invalid_ids_in_range(start, end):
    invalid_ids = []
    
    s_end = str(end)
    max_len = len(s_end)
    
    for pattern_len in range(1, max_len + 1):
        for reps in range(2, max_len // pattern_len + 1):
            total_len = pattern_len * reps
            if total_len > max_len:
                break
            
            pattern_start = max(1, 10 ** (pattern_len - 1))
            pattern_end = 10 ** pattern_len - 1
            
            for p in range(pattern_start, pattern_end + 1):
                s_pattern = str(p)
                repeated = int(s_pattern * reps)
                
                if start <= repeated <= end:
                    invalid_ids.append(repeated)
    
    return list(set(invalid_ids))


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
    with open("D2_02_input.txt", "r") as f:
        input_text = f.read()
    
    solve(input_text)
