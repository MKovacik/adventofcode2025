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
            delta = -1
        elif direction == "R":
            delta = 1
        else:
            raise ValueError(f"Unknown direction: {direction}")

        for _ in range(distance):
            position = (position + delta) % modulo
            if position == 0:
                zero_hits += 1

    return zero_hits


def main():
    input_path = "D1_02_input.txt"
    with open(input_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    rotations = parse_rotations(lines)
    password = simulate(rotations)
    print(password)


if __name__ == "__main__":
    main()