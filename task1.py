class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

def search(root, key):
    if root is None or root.val == key:
        return root
    if key < root.val:
        return search(root.left, key)
    return search(root.right, key)

def search_max(root):
    if root is None or root.right is None:
        return root
    return search_max(root.right)

def search_min(root):
    if root is None or root.left is None:
        return root
    return search_min(root.left)

def main():
    # Test
    root = Node(5)
    root = insert(root, 3)
    root = insert(root, 2)
    root = insert(root, 4)
    root = insert(root, 7)
    root = insert(root, 10)
    root = insert(root, 11)
    root = insert(root, 6)
    root = insert(root, 8)
    root = insert(root, 9)
    

    max = search_max(root)
    min = search_min(root)

    print(f"найбільше значення: {max.val}")
    print(f"найменше значення: {min.val}")

if __name__ == "__main__":
    main()