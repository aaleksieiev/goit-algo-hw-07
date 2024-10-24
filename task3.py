class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def preorder_traversal_sum(root):
    if root:
        return root.val + preorder_traversal_sum(root.left) + preorder_traversal_sum(root.right)
    else: 
        return 0        


def main():
    # Створення дерева
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    sum = preorder_traversal_sum(root)
    print(f"Сума отримана прямим обходом: {sum} \n")
    


if __name__ == "__main__":
    main()