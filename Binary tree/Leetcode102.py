import collections

class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None
def levelOrder(root):
    queue = collections.deque()
    queue.append(root)
    res = []
    while queue:
        size = len(queue)
        level = []
        for _ in range(size):
            cur = queue.popleft()
            if not cur:
                continue
            level.append(cur.val)
            queue.append(cur.left)
            queue.append(cur.right)
        if level:
            res.append(level)
    return res


if __name__ == "__main__":
    # 新建节点
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)
    node7 = TreeNode(7)
    node8 = TreeNode(8)
    node9 = TreeNode(9)
    node10 = TreeNode(10)
    node11 = TreeNode(11)

    # 构建二叉树
    node1.left, node1.right = node2, node3
    node2.left, node2.right = node4, node5
    node3.left, node3.right = node6, node7
    node4.left, node4.right = node8, node9
    node5.left, node5.right = node10, node11

    # 指定 node1 为root节点
    root = node1

    # 打印
    print("\nprint in one line:" )
    print(levelOrder(root))
