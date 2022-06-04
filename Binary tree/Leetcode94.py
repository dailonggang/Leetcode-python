class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


def preorderTraversal(root):
    # 保存结果
    result = []
    
    # 递归
    def traversal(root):
        if not root:
            return
        traversal(root.left)  # 左
        result.append(root.val)  # 中序
        traversal(root.right)  # 右

    traversal(root)
    return result
