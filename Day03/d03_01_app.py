def find_max_joltage(bank):
    max_joltage = 0
    
    for i in range(len(bank)):
        for j in range(i + 1, len(bank)):
            joltage = int(bank[i] + bank[j])
            if joltage > max_joltage:
                max_joltage = joltage
    
    return max_joltage


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
    with open("D3_01_input.txt", "r") as f:
        input_text = f.read()
    
    solve(input_text)
