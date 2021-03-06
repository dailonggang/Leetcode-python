class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


def isSymmetric(root):
    if not root:
        return True
    return compare(root.left, root.right)


def compare(left, right):
    # 首先排除空节点的情况
    if left == None and right != None:
        return False
    elif left != None and right == None:
        return False
    elif left == None and right == None:
        return True
    # 排除了空节点，再排除数值不相同的情况
    elif left.val != right.val:
        return False

    # 此时就是：左右节点都不为空，且数值相同的情况
    # 此时才做递归，做下一层的判断
    outside = compare(left.left, right.right)  # 左子树：左、 右子树：右
    inside = compare(left.right, right.left)  # 左子树：右、 右子树：左
    isSame = outside and inside  # 左子树：中、 右子树：中 （逻辑处理）
    return isSame


if __name__ == "__main__":
    # 新建节点
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(2)
    node4 = TreeNode(3)
    node5 = TreeNode(4)
    node6 = TreeNode(4)
    node7 = TreeNode(3)
    node8 = TreeNode(5)
    node9 = TreeNode(6)
    node10 = TreeNode(7)
    node11 = TreeNode(8)
    node12 = TreeNode(8)
    node13 = TreeNode(7)
    node14 = TreeNode(6)
    node15 = TreeNode(5)

    # 构建二叉树
    node1.left, node1.right = node2, node3
    node2.left, node2.right = node4, node5
    node3.left, node3.right = node6, node7
    node4.left, node4.right = node8, node9
    node5.left, node5.right = node10, node11
    node6.left, node6.right = node12, node13
    node7.left, node7.right = node14, node15


    # 指定 node1 为root节点
    root = node1

    # 打印
    print("print in one line:{}".format(isSymmetric(root)))
