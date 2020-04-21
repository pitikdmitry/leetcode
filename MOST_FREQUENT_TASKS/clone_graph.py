'''
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a val (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}
'''


# Definition for a Node.
class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.neighbors = []


class Solution:
    def clone_node(self, node: Node) -> Node:
        new_node = Node(node.val)
        return new_node

    def cloneGraph(self, root: Node) -> Node:
        if root is None:
            return None

        root_cl = self.clone_node(root)

        visited = set()
        #   we store here original_node: clone_node for all created clone nodes
        created_clones = {}
        s = []
        s_cl = []

        s.append(root)
        s_cl.append(root_cl)
        created_clones[root] = root_cl

        while len(s) > 0:
            node = s.pop(0)
            node_cl = s_cl.pop(0)

            if node in visited:
                continue
            visited.add(node)

            for child in node.neighbors:
                if child in created_clones:
                    child_cl = created_clones[child]
                else:
                    child_cl = self.clone_node(child)
                    created_clones[child] = child_cl

                node_cl.neighbors.append(child_cl)

                s.append(child)
                s_cl.append(child_cl)

        return root_cl
