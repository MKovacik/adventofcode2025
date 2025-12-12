def parse_input(input_text):
    shapes, regions = {}, []
    blocks = input_text.strip().split('\n\n')
    
    for block in blocks:
        lines = block.strip().split('\n')
        if 'x' in lines[0]:
            for line in lines:
                dims, qtys = line.split(':')
                w, h = map(int, dims.split('x'))
                regions.append((w, h, list(map(int, qtys.split()))))
        else:
            shape_id = int(lines[0].replace(':', ''))
            shapes[shape_id] = {(r, c) for r, row in enumerate(lines[1:]) 
                                for c, ch in enumerate(row) if ch == '#'}
    return shapes, regions


def normalize(shape):
    min_r, min_c = min(r for r, c in shape), min(c for r, c in shape)
    return frozenset((r - min_r, c - min_c) for r, c in shape)


def get_variants(shape):
    variants = set()
    for flip in [shape, {(r, -c) for r, c in shape}]:
        current = flip
        for _ in range(4):
            variants.add(normalize(current))
            current = {(c, -r) for r, c in current}
    return list(variants)


def get_placements(variant, w, h):
    max_r, max_c = max(r for r, c in variant), max(c for r, c in variant)
    return [frozenset((sr + r, sc + c) for r, c in variant)
            for sr in range(h - max_r) for sc in range(w - max_c)]


def can_fit(w, h, shapes, quantities):
    total = sum(len(shapes[i]) * q for i, q in enumerate(quantities))
    if total > w * h:
        return False
    
    presents = []
    for sid, qty in enumerate(quantities):
        if qty > 0:
            placements = [p for v in get_variants(shapes[sid]) for p in get_placements(v, w, h)]
            presents.extend([placements] * qty)
    
    if not presents:
        return True
    
    presents.sort(key=len)
    
    def backtrack(idx, occupied):
        if idx == len(presents):
            return True
        for p in presents[idx]:
            if not (p & occupied) and backtrack(idx + 1, occupied | p):
                return True
        return False
    
    return backtrack(0, set())


def solve(input_text):
    shapes, regions = parse_input(input_text)
    
    fit_count = sum(1 for w, h, q in regions if can_fit(w, h, shapes, q))
    
    print(f"\nNumber of shapes: {len(shapes)}")
    print(f"Number of regions: {len(regions)}")
    print(f"Regions that can fit all presents: {fit_count}")
    return fit_count


if __name__ == "__main__":
    with open("D12_01_input.txt", "r") as f:
        solve(f.read())
