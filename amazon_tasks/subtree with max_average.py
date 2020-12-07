class Node:
    def __init__(self, val):
        self.val = val
        self.children = []


def helper(root):
    best_res = 0
    best_node = None
    def get_max_average(node):
        if len(node.children) == 0:
            return node.val, 1

        s, amount = 0, 0
        for child in node.children:
            s_child, amount_child = get_max_average(child)
            s += s_child
            amount += amount_child

        s += node.val
        amount += 1
        nonlocal best_res
        nonlocal best_node
        res = s / amount
        if res > best_res:
            best_res = max(best_res, s / amount)
            best_node = node.val
        return s, amount

    get_max_average(root)
    return best_node


root = Node(20)
node_12 = Node(12)
node_18 = Node(18)
root.children.append(node_12)
root.children.append(node_18)

node_11 = Node(11)
node_2 = Node(2)
node_3 = Node(3)
node_12.children.append(node_11)
node_12.children.append(node_2)
node_12.children.append(node_3)

node_15 = Node(15)
node_8 = Node(8)
node_18.children.append(node_15)
node_18.children.append(node_8)
print(helper(root))
