def dfs(node, previous, graph, visited_time, low_link, discovery_time):

    visited_time[node] = discovery_time
    low_link[node] = discovery_time

    for child in graph[node]:
        if child == previous:   #   we don't go back in undirected graph
            continue
        if child not in visited_time:
            dfs(child, node, graph, visited_time, low_link, discovery_time + 1)

            if low_link[child] > visited_time[node]:
                #   node is articulation point, because no another path to child exists
                print(child.val)
            elif low_link[child] == visited_time[node] and len(graph[node] >= 2):
                #   check if it is a root of cycle and it need to have 2+ children
                print(child.val)
        else:
            #   if child is visited we only update low link value
            low_link[node] = min(low_link[node], low_link[child])
