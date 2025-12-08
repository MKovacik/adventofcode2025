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
        return True
    
    def get_circuit_sizes(self):
        sizes = []
        for i in range(len(self.parent)):
            if self.parent[i] == i:
                sizes.append(self.size[i])
        return sorted(sizes, reverse=True)


def connect_boxes(boxes, num_connections):
    distances = get_all_distances(boxes)
    uf = UnionFind(len(boxes))
    
    connections_made = 0
    for _, i, j in distances:
        if connections_made >= num_connections:
            break
        uf.union(i, j)
        connections_made += 1
    
    return uf.get_circuit_sizes()


def solve(input_text):
    boxes = parse_input(input_text)
    
    circuit_sizes = connect_boxes(boxes, 1000)
    
    top_three = circuit_sizes[:3]
    result = top_three[0] * top_three[1] * top_three[2]
    
    print(f"\nNumber of junction boxes: {len(boxes)}")
    print(f"Top 3 circuit sizes: {top_three}")
    print(f"Product of top 3: {result}")
    return result


if __name__ == "__main__":
    with open("D8_01_input.txt", "r") as f:
        input_text = f.read()
    
    solve(input_text)
