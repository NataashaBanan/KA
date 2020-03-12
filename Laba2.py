def read():
    with open('input2.txt', 'r') as f:
        count = int(f.readline())
        incidence = []
        for i in range(count):
            incidence.append(list(map(int, f.readline().split())))
    return count, incidence


def BFS(incidence, count):
    track = {0: [-1]}
    not_visited = [i for i in range(count)]
    queue = [not_visited[0]]
    while len(not_visited) > 0:
        if len(queue) == 0:
            queue.append(not_visited[0])
            track[not_visited[0]] = [-1]
        el = queue.pop(0)
        not_visited.remove(el)
        tr = track[el].copy()
        tr.append(el)
        for i in range(count):
            if incidence[el][i] == 1 and i != track[el][-1]:
                if i in queue:
                    return create_answer(i, track[i], el, track[el])
                track[i] = tr
                queue.append(i)


def create_answer(i, track_i, el, track_el):
    res = [i, el]
    while track_el[-1] not in track_i:
        res.append(track_el.pop())
    while track_i[-1] != track_el[-1]:
        res.append(track_i.pop())
    res.append(track_i.pop())
    res.sort()
    return res


count, incidence = read()
res = BFS(incidence, count)
with open('output2.txt', 'w') as f:
    if res is None:
        f.write("A")
    else:
        f.write("N\n")
        for i in res:
            f.write(str(i) + " ")
