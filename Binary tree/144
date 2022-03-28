def preorderTraversal(self, root: TreeNode):
    # 保存结果
    result = []

    def traversal(root: TreeNode):
        if root == None:
            return
        result.append(root.val) # 前序
        traversal(root.left)    # 左
        traversal(root.right)   # 右

    traversal(root)
    return result
