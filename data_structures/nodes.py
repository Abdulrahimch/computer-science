class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def __repr__(self):
        return '{0} {1}'.format(self.get_value(),self.get_next_node())

    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, next_node):
        self.next_node = next_node

# node_a = Node('A')
# node_b = Node('B')
# node_c = Node('C')
#
# node_a.set_next_node(node_b)
# node_b.set_next_node(node_c)

# print(node_a)
