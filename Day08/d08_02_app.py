import math

def parse_input(input_text):
    lines = input_text.rstrip('\n').split('\n')
    
    boxes = []
    for line in lines:
        x, y, z = map(int, line.split(','))
        boxes.append((x, y, z))
    
    return boxes

def calculate_distance(box1, box2):
    dx = box1[0] - box2[0]
    dy = box1[1] - box2[1]
    dz = box1[2] - box2[2]
    return math.sqrt(dx*dx + dy*dy + dz*dz)

def get_all_distances(boxes):
    distances = []
    n = len(boxes)
    
    for i in range(n):
        for j in range(i + 1, n):
            dist = calculate_distance(boxes[i], boxes[j])
            distances.append((dist, i, j))
    
    distances.sort()
    return distances

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.num_components = n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x == root_y:
            return False
        
        if self.size[root_x] < self.size[root_y]:
            root_x, root_y = root_y, root_x
        
        self.parent[root_y] = root_x
        self.size[root_x] += self.size[root_y]
        self.num_components -= 1
        return True

def find_last_connection(boxes):
    distances = get_all_distances(boxes)
    uf = UnionFind(len(boxes))
    
    last_i, last_j = None, None
    
    for _, i, j in distances:
        if uf.union(i, j):
            last_i, last_j = i, j
            if uf.num_components == 1:
                break
    
    return boxes[last_i], boxes[last_j]

def solve(input_text):
    boxes = parse_input(input_text)
    
    box1, box2 = find_last_connection(boxes)
    result = box1[0] * box2[0]
    
    print(f"\nNumber of junction boxes: {len(boxes)}")
    print(f"Last connection: {box1} <-> {box2}")
    print(f"Product of X coordinates: {box1[0]} * {box2[0]} = {result}")
    return result

if __name__ == "__main__":
    with open("D8_02_input.txt", "r") as f:
        input_text = f.read()
    
    solve(input_text)
