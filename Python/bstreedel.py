class DatabaseNode:
    def __init__(self, user_id, user_data):
        self.user_id = user_id
        self.user_data = user_data
        self.left = None
        self.right = None

def find_min_value_node(root):
    current = root
    while current.left is not None:
        current = current.left
    return current

def delete_user(root, target_id):
    if root is None:
        return root

    if target_id < root.user_id:
        root.left = delete_user(root.left, target_id)
    elif target_id > root.user_id:
        root.right = delete_user(root.right, target_id)
    else:
        # Node with only one child or no child
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left

        # Node with two children: Get the inorder successor (smallest in the right subtree)
        temp = find_min_value_node(root.right)

        # Copy the inorder successor's content to this node
        root.user_id = temp.user_id
        root.user_data = temp.user_data

        # Delete the inorder successor
        root.right = delete_user(root.right, temp.user_id)

    return root

def validate_bst_helper(node,min_value=-float('inf'),max_value=float('inf')):
    if node is None:
        return True

    if node.user_id <= min_value or node.user_id >= max_value:
        return False

    return (validate_bst_helper(node.left, min_value, node.user_id) and
            validate_bst_helper(node.right, node.user_id, max_value))

def is_valid_bst(root):
    return validate_bst_helper(root)

good_tree=DatabaseNode(50,"UserA")
good_tree.left=DatabaseNode(30,"UserB")
good_tree.right=DatabaseNode(70,"UserC")

bad_tree=DatabaseNode(50,"UserA")
bad_tree.left=DatabaseNode(30,"UserB")  
bad_tree.right=DatabaseNode(20,"UserC")  # Invalid BST

#call the tree validation function and print the results
print("Is good_tree a valid BST?", is_valid_bst(good_tree))  #

    