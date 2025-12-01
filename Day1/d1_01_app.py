def parse_rotations(lines):
    rotations = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        direction = line[0]
        value = int(line[1:])
        rotations.append((direction, value))
    return rotations


def simulate(rotations, start=50, modulo=100):
    position = start
    zero_hits = 0

    for direction, distance in rotations:
        if direction == "L":
            position = (position - distance) % modulo
        elif direction == "R":
            position = (position + distance) % modulo
        else:
            raise ValueError(f"Unknown direction: {direction}")

        if position == 0:
            zero_hits += 1

    return zero_hits


def main():
    input_path = "D1_01_input.txt"
    with open(input_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    rotations = parse_rotations(lines)
    password = simulate(rotations)
    print(password)


if __name__ == "__main__":
    main()