from collections import deque

class NetworkNode:
    def __init__(self, username):
        self.username = username
        self.left = None
        self.right = None

def level_order_broadcast(root):
    if root is None:
        return []

    queue = deque([root])
    broadcast_order = []

    while queue:
        current_node = queue.popleft()
        broadcast_order.append(current_node.username)

        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)

    return broadcast_order
def level_order_by_layer(root):
    if root is None:
        return []

    queue = deque([root])
    result = []

    while queue:
        level_size = len(queue)
        current_level = []

        for _ in range(level_size):
            current_node = queue.popleft()
            current_level.append(current_node.username)

            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)

        result.append(current_level)

    return result

company=NetworkNode("CEO")
company.left=NetworkNode("Manager1")
company.right=NetworkNode("Manager2")

company.left.left=NetworkNode("Employee1")
company.left.right=NetworkNode("Employee2")

company.right.left=NetworkNode("Employee3")
company.right.right=NetworkNode("Employee4")

print("Broadcast Order:", level_order_broadcast(company))
print("Level Order by Layer:", level_order_by_layer(company))

