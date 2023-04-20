
import sys


def DepthFristSearch(argument):
    global finished
    global timer
    global t
    global b
    global f
    global c
    global stack
    global discovery_times
    global depth
    global list_neibors


    timer += 1
    discovery_times[argument] = timer
    stack.append(argument)

    for goal in list_neibors[argument]:
        depth[goal] = depth[argument] + 1
        DepthFristSearch(goal)

    stack.pop()

    for vertex in stack:
        if b <= 0:
            break
        list_neibors[argument].append(vertex)
        b -= 1

    for vertex in finished:
        if c <= 0 or discovery_times[vertex] >= discovery_times[argument]:
            break

        goal = vertex
        list_neibors[argument].append(goal)
        c -= 1

    for vertex in finished:
        if f <= 0 or discovery_times[vertex] <= discovery_times[argument]:
            break
        goal = vertex
        if depth[goal] == depth[argument] + 1:
            continue
        list_neibors[argument].append(goal)
        f -= 1

    finished.add(argument)


if __name__ == '__main__':
    tbfc = input().split()

    t = int(tbfc[0])

    b = int(tbfc[1])

    f = int(tbfc[2])

    c = int(tbfc[3])

    n_vertices = t + 1

    list_neibors = {i: list() for i in range(n_vertices)}
    stack = list()
    discovery_times = [0] * n_vertices
    depth = [0] * n_vertices
    timer = 0
    finished = set()
    minimum_height = max(f + t, b)
    maximum_height = (n_vertices * (n_vertices - 1)) / 2 - c
    if maximum_height < minimum_height:
        print(-1)
        sys.exit()


    sum_height = t
    for i in range(1, n_vertices):
        if sum_height + i - 1 <= minimum_height:
            list_neibors[i - 1].append(i)
            sum_height = sum_height + (i - 1)
        else:
            list_neibors[minimum_height - sum_height].append(i)
            sum_height = sum_height + (minimum_height - sum_height)

    if sum_height < minimum_height:
        print(-1)
        sys.exit()
    DepthFristSearch(0)
    print(n_vertices)
    for i in list_neibors:
        print(len(list_neibors[i]))
        for v in list_neibors[i]:
            print(v + 1)