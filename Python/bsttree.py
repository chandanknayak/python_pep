class BSTree:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

    # @staticmethod
    def insert(root, key):
        if root is None:
            return BSTree(key)

        if key < root.val:
            root.left = BSTree.insert(root.left, key)
        else:
            root.right = BSTree.insert(root.right, key)

        return root

    # @staticmethod.3
    def search(root, key):
        if root is None or root.val == key:
            return root

        if key < root.val:
            return BSTree.search(root.left, key)

        return BSTree.search(root.right, key)


bstree = None
numbers = [15, 10, 20, 8, 12, 17, 25]

for num in numbers:
    bstree = BSTree.insert(bstree, num)

result = BSTree.search(bstree, 17)

if result:
    print("Found:", result.val)
else:
    print("Not Found")