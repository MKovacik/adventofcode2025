import re
import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds


def parse_input(input_text):
    lines = input_text.strip().split('\n')
    
    machines = []
    for line in lines:
        if not line.strip():
            continue
        
        joltage_match = re.search(r'\{([\d,]+)\}', line)
        if not joltage_match:
            continue
        target = [int(x) for x in joltage_match.group(1).split(',')]
        
        curly_idx = line.find('{')
        line_before_curly = line[:curly_idx] if curly_idx != -1 else line
        
        button_matches = re.findall(r'\(([\d,]+)\)', line_before_curly)
        buttons = []
        for bm in button_matches:
            indices = [int(x) for x in bm.split(',') if x]
            buttons.append(indices)
        
        machines.append((buttons, target))
    
    return machines


def find_min_presses(buttons, target):
    n_buttons = len(buttons)
    n_counters = len(target)
    
    A = np.zeros((n_counters, n_buttons))
    for j, btn in enumerate(buttons):
        for i in btn:
            if i < n_counters:
                A[i][j] = 1
    
    c = np.ones(n_buttons)
    target_array = np.array(target, dtype=float)
    constraints = LinearConstraint(A, target_array, target_array)
    
    max_target = max(target) if target else 0
    bounds = Bounds(0, max_target * 2)
    integrality = np.ones(n_buttons)
    
    result = milp(c, constraints=constraints, bounds=bounds, integrality=integrality)
    
    if result.success:
        return int(round(result.fun))
    return float('inf')


def solve(input_text):
    machines = parse_input(input_text)
    
    total_presses = 0
    for i, (buttons, target) in enumerate(machines):
        min_presses = find_min_presses(buttons, target)
        total_presses += min_presses
    
    print(f"\nNumber of machines: {len(machines)}")
    print(f"Total minimum button presses: {total_presses}")
    return total_presses


if __name__ == "__main__":
    with open("D10_01_input.txt", "r") as f:
        input_text = f.read()
    
    solve(input_text)
