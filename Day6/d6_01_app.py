def parse_input(input_text):
    lines = input_text.rstrip('\n').split('\n')
    
    operator_line = lines[-1]
    number_lines = lines[:-1]
    
    width = max(len(line) for line in lines)
    
    number_lines = [line.ljust(width) for line in number_lines]
    operator_line = operator_line.ljust(width)
    
    problems = []
    current_problem_start = None
    
    for col in range(width):
        has_content = False
        for row in number_lines:
            if col < len(row) and row[col].isdigit():
                has_content = True
                break
        if not has_content and col < len(operator_line):
            if operator_line[col] in '*+':
                has_content = True
        
        if has_content:
            if current_problem_start is None:
                current_problem_start = col
        else:
            if current_problem_start is not None:
                problems.append((current_problem_start, col))
                current_problem_start = None
    
    if current_problem_start is not None:
        problems.append((current_problem_start, width))
    
    parsed_problems = []
    for start, end in problems:
        numbers = []
        for row in number_lines:
            segment = row[start:end].strip()
            if segment:
                numbers.append(int(segment))
        
        operator_segment = operator_line[start:end].strip()
        operator = operator_segment if operator_segment in '*+' else None
        
        if numbers and operator:
            parsed_problems.append((numbers, operator))
    
    return parsed_problems


def solve_problem(numbers, operator):
    if operator == '+':
        result = sum(numbers)
    else:
        result = 1
        for num in numbers:
            result *= num
    return result


def calculate_grand_total(problems):
    total = 0
    
    for numbers, operator in problems:
        result = solve_problem(numbers, operator)
        total += result
    
    return total


def solve(input_text):
    problems = parse_input(input_text)
    
    grand_total = calculate_grand_total(problems)
    
    print(f"\nNumber of problems: {len(problems)}")
    print(f"Grand total: {grand_total}")
    return grand_total


if __name__ == "__main__":
    with open("D6_01_input.txt", "r") as f:
        input_text = f.read()
    
    solve(input_text)
