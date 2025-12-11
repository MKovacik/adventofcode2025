import re
from itertools import combinations


def parse_input(input_text):
    lines = input_text.strip().split('\n')
    
    machines = []
    for line in lines:
        if not line.strip():
            continue
        
        pattern_match = re.search(r'\[([.#]+)\]', line)
        pattern = pattern_match.group(1)
        
        button_matches = re.findall(r'\(([0-9,]+)\)', line)
        buttons = []
        for btn in button_matches:
            indices = [int(x) for x in btn.split(',')]
            buttons.append(indices)
        
        machines.append((pattern, buttons))
    
    return machines


def pattern_to_target(pattern):
    return [1 if c == '#' else 0 for c in pattern]


def button_to_mask(button_indices, num_lights):
    mask = [0] * num_lights
    for idx in button_indices:
        if idx < num_lights:
            mask[idx] = 1
    return mask


def apply_buttons(num_lights, buttons, button_presses):
    state = [0] * num_lights
    for i, pressed in enumerate(button_presses):
        if pressed:
            for idx in buttons[i]:
                if idx < num_lights:
                    state[idx] ^= 1
    return state


def find_min_presses(pattern, buttons):
    target = pattern_to_target(pattern)
    num_lights = len(pattern)
    num_buttons = len(buttons)
    
    min_presses = float('inf')
    
    for num_pressed in range(num_buttons + 1):
        if num_pressed >= min_presses:
            break
        
        for combo in combinations(range(num_buttons), num_pressed):
            button_presses = [1 if i in combo else 0 for i in range(num_buttons)]
            state = apply_buttons(num_lights, buttons, button_presses)
            
            if state == target:
                min_presses = num_pressed
                break
        
        if min_presses == num_pressed:
            break
    
    return min_presses


def solve(input_text):
    machines = parse_input(input_text)
    
    total_presses = 0
    for i, (pattern, buttons) in enumerate(machines):
        min_presses = find_min_presses(pattern, buttons)
        total_presses += min_presses
    
    print(f"\nNumber of machines: {len(machines)}")
    print(f"Total minimum button presses: {total_presses}")
    return total_presses


if __name__ == "__main__":
    with open("D10_02_input.txt", "r") as f:
        input_text = f.read()
    
    solve(input_text)
