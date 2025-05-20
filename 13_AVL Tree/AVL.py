from os import waitid
from BST_Tree import BST
class AVL(BST):
    def get_height(self, node):
        if node is None:
            return -1
        left_height = node.left.height if node.left else -1
        right_height = node.right.height if node.right else -1
        return 1 + max(left_height, right_height)

    def get_balance(self, node):
        return self.get_height(node.left) - self.get_height(node.right)

    def insert(self, data):
        node = super(AVL,self).insert(data)
        node.height = self.get_height(node)
        node = self.balancing(node)
        return node

    def delete(self, data):
        node = super(AVL,self).deleteByMerging(data)
        node = self.balancing(node)
        return node


    def rotate_right(self, node):
      x = node.left
      b = x.right
      if node is None:
        return None
      if x is None:
        return node
      x.parent = node.parent
      if node.parent is not None:
        if node.parent.left == node:
          node.parent.left = x
        else:
          node.parent.right = x
      x.right = node
      node.parent = x
      node.left = b
      if b is not None:
        b.parent = node
      if self.root == node:
        self.root = x
      node.height = self.get_height(node)
      x.height = self.get_height(x)
      return x

    def rotate_left(self, node):
      x = node.right
      b = x.left
      if node is None:
        return None
      if x is None:
        return node
      x.parent = node.parent
      if node.parent is not None:
        if node.parent.left == node:
          node.parent.left = x
        else:
          node.parent.right = x
      x.left = node
      node.parent = x
      node.right = b
      if b is not None:
        b.parent = node
      if self.root == node:
        self.root = x
      node.height = self.get_height(node)
      x.height = self.get_height(x)
      return x

    def rotate_right_left(self, node):
        self.rotate_right(node.right)
        return self.rotate_left(node)

    def rotate_left_right(self, node):
        self.rotate_left(node.left)
        return self.rotate_right(node)

    def balancing(self, node):
        while node:
            balance_factor = self.get_balance(node)
            if balance_factor == 2:
                if self.get_balance(node.left) >= 0:
                    node = self.rotate_right(node)
                else:
                    node = self.rotate_left_right(node)
            elif balance_factor == -2:
                if self.get_balance(node.right) <= 0:
                    node = self.rotate_left(node)
                else:
                    node = self.rotate_right_left(node)
            w = node
            node = node.parent
        return waitid

