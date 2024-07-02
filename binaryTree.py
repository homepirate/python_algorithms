class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Tree:

    def __init__(self):
        self.root = None

    def __find(self, node, parent, value):
        if value == node.data:
            return node, parent, True

        if value < node.data:
            if node.left:
                return self.__find(node.left, node, value)
        if value > node.data:
            if node.right:
                return self.__find(node.right, node, value)

        return node, parent, False

    def __find_min(self, node, parent):
        if node.left:
            return self.__find_min(node.left, node)
        return node, parent

    def append(self, obj: Node):
        if not self.root:
            self.root = obj
            return obj

        s, p, fl_find = self.__find(self.root, None, obj.data)
        if not fl_find and s:
            if obj.data < s.data:
                s.left = obj
            else:
                s.right = obj

        return obj

    def show_tree(self, node):
        if node is None:
            return
        self.show_tree(node.left)
        print(node.data)
        self.show_tree(node.right)

    def del_node(self, value):
        s, p, fl_find = self.__find(self.root, None, value)

        if not fl_find:
            return

        if s.left is None and s.right is None:
            self.__del_leaf(s, p)
        elif s.left is None or s.right is None:
            self.__del_one_child(s, p)
        else:
            sr, pr = self.__find_min(s.right, s)
            s.data = sr.data
            self.__del_one_child(sr, pr)

    def __del_leaf(self, s, p):
        if p.left == s:
            p.left = None
        elif p.right == s:
            p.right = None

    def __del_one_child(self, s, p):
        if p.left == s:
            if not s.left:
                p.left = s.right
            elif not s.right:
                p.left = s.left
        elif p.right == s:
            if not s.left:
                p.right = s.right
            elif not s.right:
                p.right = s.left


def main():
    v = [10, 10, 13, 5, 6, 7, 12]
    t = Tree()
    for i in v:
        t.append(Node(i))
    t.show_tree(t.root)


if __name__ == '__main__':
    main()
