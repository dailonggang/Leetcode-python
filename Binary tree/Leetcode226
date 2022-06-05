class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


def InvertTree(root):
    """
    递归三部曲：
    曲一：确定递归函数的参数和返回值
    参数：传入节点指针
    返回值：返回root节点指针
    曲二：确定终止条件
    终止条件：节点为空返回
    曲三：确定单层递归的逻辑
    前序遍历为例，先交换左右节点，然后反转左子树，后反转右子树
    :param root: 根节点
    :return: 返回root节点指针
    """
    if not root:
        return None
    root.left, root.right = root.right, root.left # 中
    InvertTree(root.left)  # 左
    InvertTree(root.right)  # 右
    return root 
