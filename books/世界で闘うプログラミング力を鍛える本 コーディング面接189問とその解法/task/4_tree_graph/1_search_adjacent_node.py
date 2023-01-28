# 指定した2つのノードに経路があるかを見つける

import queue
from enum import IntEnum


class Visit(IntEnum):
    UnVisit = 0
    Visiting = 1
    Visit = 2


def search_adjacent_node_by_dfs(graph: list, start_node: int = 0, end_node: int = 8) -> bool:
    if start_node < 0 and end_node < 0:
        return False

    if len(graph) < start_node or len(graph[0]) < end_node:
        return False

    if start_node == end_node:
        return True

    stack = [start_node]
    is_visited_nodes = [[Visit.UnVisit for _ in range(
        len(graph))] for _ in range(len(graph[0]))]

    while len(stack) > 0:
        current_node = stack[-1]
        adjacent_nodes = graph[current_node]

        if adjacent_nodes[end_node] == 1:
            return True

        is_all_nodes_visited = True
        for adjacent_node in range(len(adjacent_nodes)):
            if adjacent_node <= end_node:
                if is_visited_nodes[current_node][adjacent_node] == Visit.UnVisit:
                    is_all_nodes_visited = False
                    is_visited_nodes[current_node][adjacent_node] = Visit.Visit
                    stack.append(adjacent_node)

        if is_all_nodes_visited == True:
            stack.pop()

    return False


def search_adjacent_node_by_bfs(graph: list, start_node: int = 0, end_node: int = 8) -> bool:
    if start_node < 0 and end_node < 0:
        return False

    if len(graph) < start_node or len(graph[0]) < end_node:
        return False

    if start_node == end_node:
        return True

    q = queue.Queue()
    q.put(start_node)
    is_visited_nodes = [[Visit.UnVisit for _ in range(
        len(graph))] for _ in range(len(graph[0]))]
    while q.empty() == False:
        current_node = q.get()
        adjacent_nodes = graph[current_node]

        # 2つのノード間で経路が存在する
        if adjacent_nodes[end_node] == 1:
            return True
        # 経路が存在しない場合は、2つのノードの間にあるデータを訪れたことにする
        for adjacent_node in range(len(adjacent_nodes)):
            if adjacent_node <= end_node:
                if is_visited_nodes[current_node][adjacent_node] == Visit.UnVisit:
                    q.put(adjacent_node)

                is_visited_nodes[current_node][adjacent_node] = Visit.Visit
    return False


if __name__ == "__main__":
    graph = [
        [0, 0, 1, 1, 1, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
    print(search_adjacent_node_by_dfs(graph, 0, 1))  # False
    print(search_adjacent_node_by_dfs(graph, 1, 4))  # True
    print(search_adjacent_node_by_dfs(graph, 4, 7))  # True
    print(search_adjacent_node_by_bfs(graph, 0, 1))  # False
    print(search_adjacent_node_by_bfs(graph, 1, 4))  # True
    print(search_adjacent_node_by_bfs(graph, 4, 7))  # True
