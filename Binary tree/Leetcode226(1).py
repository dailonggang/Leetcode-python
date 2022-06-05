def invertTree(self, root: TreeNode) -> TreeNode:
    queue = collections.deque() #使用deque()
    if root:
        queue.append(root)
    while queue:
        size = len(queue)
        for i in range(size):
            node = queue.popleft()
            node.left, node.right = node.right, node.left #节点处理
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return root
