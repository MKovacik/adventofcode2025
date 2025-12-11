from functools import lru_cache


def parse_input(input_text):
    lines = input_text.strip().split('\n')
    
    graph = {}
    for line in lines:
        if not line.strip():
            continue
        parts = line.strip().split(': ')
        if len(parts) == 2:
            source = parts[0]
            destinations = parts[1].split()
            graph[source] = destinations
    
    return graph


def count_paths(graph, start, end):
    @lru_cache(maxsize=None)
    def dfs(node):
        if node == end:
            return 1
        
        if node not in graph:
            return 0
        
        total = 0
        for neighbor in graph[node]:
            total += dfs(neighbor)
        
        return total
    
    result = dfs(start)
    return result


def solve(input_text):
    graph = parse_input(input_text)
    
    print(f"Number of devices: {len(graph)}")
    
    path_count = count_paths(graph, 'you', 'out')
    
    print(f"Number of paths from 'you' to 'out': {path_count}")
    return path_count


if __name__ == "__main__":
    with open("D11_01_input.txt", "r") as f:
        input_text = f.read()
    
    solve(input_text)
