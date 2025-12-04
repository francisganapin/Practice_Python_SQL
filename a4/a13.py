graph = {
    "A":["B","C"],
    "B":["A","D"],
    "C":["A","D"]
}


for node in graph:
    print(node,graph[node])