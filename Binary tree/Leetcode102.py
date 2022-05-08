import collections


# 二叉树节点定义
class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


def levelOrder(root):
    # 保存结果
    res = []
    # 如果开始结点为空，直接返回空列表
    if not root:
        return res
    # 创建双端队列，可以比较方便的从两头append数据
    queue = collections.deque()
    # 添加根结点
    queue.append(root)

    while queue:
        # 层数结点的个数
        size = len(queue)
        # 用于保存该层数的结点
        level = []
        for _ in range(size):
            # 从左侧弹出结点
            cur = queue.popleft()
            # 将结点值添加到level中
            level.append(cur.val)
            # 如果左侧子树不为None,那么就将其添加到queue中
            if cur.left:
                queue.append(cur.left)
            # 如果右侧子树不为None,那么就将其添加到queue中
            if cur.right:
                queue.append(cur.right)
        # 将每一层的结点值添加到res中
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
    print("print in one line:" )
    print(levelOrder(root))
