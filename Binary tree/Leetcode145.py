def postorderTraversal(root):
  # 存取结果
  result = []

  def traversal(root):
      if not root:
          return
      traversal(root.left)    # 左
      traversal(root.right)   # 右
      result.append(root.val) # 后序

  traversal(root)
  return result
