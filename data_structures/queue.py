from nodes import Node

class Queue:
    def __init__(self, limit=5):
        self.head = None
        self.tail = None
        self.limit = limit
        self.queue_size = 0

    def enqueue(self, value):
        new_node = Node(value)
        if self.no_space():
            return 'Queue is full'

        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.set_next_node(new_node)
            self.tail = new_node
        self.queue_size += 1

    def dequeue(self):
        if self.queue_size > 0:
            node_to_remove = self.head

            if self.queue_size == 1:
                self.head = None
                self.tail = None
            else:
                self.head = node_to_remove.get_next_node()
            self.queue_size -= 1
            return node_to_remove.get_value()
        return 'Qeueu is empty'

    def peek(self):
        if self.queue_size > 0:
            return self.head.get_value()
        return 'Queue is empty'

    def no_space(self):
        return self.queue_size == self.limit

    def is_empty(self):
        return self.queue_size == 0

# a = Queue()
# a.enqueue('A')
# a.enqueue('B')
# a.enqueue('C')
# a.enqueue('D')
# a.enqueue('E')
# print(a.enqueue('F'))
# a.dequeue()
# a.dequeue()
# a.dequeue()
# a.dequeue()
#
#
#
# print(a.peek())

