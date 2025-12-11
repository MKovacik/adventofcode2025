def find_max_joltage(bank, num_batteries=12):
    n = len(bank)
    result = []
    start = 0
    
    for remaining in range(num_batteries, 0, -1):
        end = n - remaining + 1
        best_digit = '0'
        best_idx = start
        
        for i in range(start, end):
            if bank[i] > best_digit:
                best_digit = bank[i]
                best_idx = i
        
        result.append(best_digit)
        start = best_idx + 1
    
    return int(''.join(result))


def solve(input_text):
    lines = input_text.strip().split('\n')
    
    all_joltages = []
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
        max_joltage = find_max_joltage(line)
        all_joltages.append(max_joltage)
    
    total = sum(all_joltages)
    print(f"\nTotal output joltage: {total}")
    return total


if __name__ == "__main__":
    with open("D3_02_input.txt", "r") as f:
        input_text = f.read()
    
    solve(input_text)
