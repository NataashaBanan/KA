def read():
    incident_nodes = []
    with open("input1.txt", 'r')as f :
        count = int(f.readline())
        for i in range(count):
            incident_nodes.append(list(map(int, f.readline().split()))[:-1])
    return count, incident_nodes


def counter(incident_nodes, n):
    res = []
    non_visited = [i + 1 for i in range(n)]
    while len(non_visited) > 0:
        el = non_visited[0]
        ar = DFS(non_visited, incident_nodes, el, [])
        ar.sort()
        ar.append(0)
        res.append(ar)
    return res


def DFS(non_visited, incident_nodes, el, result):
    non_visited.remove(el)
    result.append(el)
    for node in incident_nodes[el - 1]:
        if node in non_visited:
            DFS(non_visited, incident_nodes, node, result)
    return result


n, incident_nodes = read()
res = counter(incident_nodes, n)
with open("output1.txt", 'w') as f:
    f.write(str(len(res)) + '\n')
    for i in res:
        for j in i:
            f.write(str(j))
        f.write('\n')

