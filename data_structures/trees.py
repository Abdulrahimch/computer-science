class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def get_child(self):
        for i in self.children:
            print(i.value)
    def remove_child(self, child_node):
        if child_node in self.children:
            child_node_index = self.children.index(child_node)
        else:
            return 'Child is not in the tree, please try again later'

        self.children.pop(child_node_index)

    def traverse(self):
        nodes_to_visit = [self]
        while len(nodes_to_visit) > 0:
            current_node = nodes_to_visit.pop()
            print(current_node.value)
            nodes_to_visit += current_node.children


root = TreeNode('I am root')
child = TreeNode('I am child')
child_2 = TreeNode('I am the second Child')
root.add_child(child)
root.add_child(child_2)

root.get_child()

root.remove_child(child)
print('Tree after removing a child')

root.traverse()



