#Final solution
def is_balanced(root):
  return is_balanced_helper(root) > -1

def is_balanced_helper(root):

  # a None tree is balanced
  if root is None:
    return 0

  left_height = is_balanced_helper(root.left)

  # if the left subtree is not balanced, then:
  # this tree is also not balanced
  if left_height == -1:
    return -1

  # if the right subtree is not balanced, then:
  # this tree is also not balanced
  right_height = is_balanced_helper(root.right)

  if right_height == -1:
    return -1

  # if the difference in heights is greater than 1, then:
  # this tree is not balanced
  if abs(left_height - right_height) > 1:
    return -1

  # this tree is balanced, return its height
  return max(left_height, right_height) + 1