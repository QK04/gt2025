# Function: Check if path from start to end exists
def path_exists(graph, start, end):
    visited = set()

    # Depth-First Search
    def dfs(node):
        if node == end:
            return True
        
        visited.add(node)

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                if dfs(neighbor):
                    return True
                
        return False

    return dfs(start)

graph = {
        '1': ['2'],
        '2': ['5'],
        '3': ['6'],
        '4': ['6', '7'],
        '5': [],
        '6': ['7'],
        '7': []
    }

start = input("Enter start node: ").strip()
end = input("Enter end node: ").strip()

# Check path exists
if path_exists(graph, start, end):
    print(f"=> Path exists between {start} and {end}.")
else:
    print(f"=> No path exists between {start} and {end}.")