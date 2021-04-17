from nodes import Node

class Stack:
    def __init__(self, limit=100):
        self.top_item = None
        self.limit = limit
        self.stack_size = 0

    def push(self, value):
        if self.stack_size == self.limit:
            raise ValueError('the stack is full')

        new_node = Node(value)
        new_node.set_next_node(self.top_item)
        self.top_item = new_node
        self.stack_size += 1

    def peek(self):
        if self.stack_size > 0:
            return self.top_item.get_value()
        return 'Stack is empty'

    def pop(self):
        if self.stack_size > 0:
            node_to_remove = self.top_item
            self.top_item = node_to_remove.get_next_node()
            self.stack_size -= 1
            return node_to_remove.get_value()
        return 'Stack in empty'



# a = Stack(5)
# a.push('B')
# a.push('C')
# a.push('D')
# a.push('E')
# print(a.pop())
# print(a.pop())
# print(a.pop())
# a.push('f')
# a.push('g')
# print(a.pop())
# print(a.pop())
# print(a.pop())
# print(a.pop())
# print(a.peek())


