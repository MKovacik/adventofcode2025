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


def count_paths_through_both(graph, start, end, required1, required2):
    
    @lru_cache(maxsize=None)
    def dfs(node, visited_req1, visited_req2):
        if node == required1:
            visited_req1 = True
        if node == required2:
            visited_req2 = True
        
        if node == end:
            return 1 if (visited_req1 and visited_req2) else 0
        
        if node not in graph:
            return 0
        
        total = 0
        for neighbor in graph[node]:
            total += dfs(neighbor, visited_req1, visited_req2)
        
        return total
    
    result = dfs(start, False, False)
    return result


def solve(input_text):
    graph = parse_input(input_text)
    
    print(f"Number of devices: {len(graph)}")
    
    path_count = count_paths_through_both(graph, 'svr', 'out', 'dac', 'fft')
    
    print(f"Number of paths from 'svr' to 'out' visiting both 'dac' and 'fft': {path_count}")
    return path_count


if __name__ == "__main__":
    with open("D11_02_input.txt", "r") as f:
        input_text = f.read()
    
    solve(input_text)
