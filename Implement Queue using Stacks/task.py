"""
Implement Queue using Stacks
"""

class Stack:
    """
    Data structure stack.
    """

    def __init__(self):
        """
        Initializes an empty stack.
        """
        self.__index = []

    def __len__(self):
        """
        Returns the number of elements in the stack.

        :return: The number of elements in the stack.
        """
        return len(self.__index)

    def push(self, item):
        """
        Adds an item to the top of the stack.

        :param item: The item to be added to the stack.
        """
        self.__index.append(item)

    def peek(self):
        """
        Returns the top item of the stack without removing it.

        :return: The top item of the stack.
        """
        if len(self) == 0:
            raise ValueError('Stack is empty')
        return self.__index[-1]

    def pop(self):
        """
        Removes and returns the top item of the stack.

        :return: The top item of the stack.
        """
        if len(self) == 0:
            raise ValueError('Stack is empty')
        return self.__index.pop()

    def __str__(self):
        """
        Returns a string representation of the stack.

        :return: A string representing the stack.
        """
        return str(self.__index)


class MyQueue:
    """
    A queue implemented using two stacks.
    """

    def __init__(self):
        """
        Initializes an empty queue using two stacks.
        """
        self.stack_one = Stack()
        self.stack_final = Stack()

    def add(self, x):
        """
        Adds an element to the end of the queue.

        :param x: The element to be added to the queue.
        :type x: Any
        """
        self.stack_one.push(x)

    def pop(self):
        """
        Removes and returns the element at the front of the queue.

        :return: The element at the front of the queue.
        """
        if not self.stack_final:
            while self.stack_one:
                last_el = self.stack_one.pop()
                self.stack_final.push(last_el)

        return self.stack_final.pop()

    def peek(self):
        """
        Returns the element at the front of the queue without removing it.

        :return: The element at the front of the queue.
        """
        if not self.stack_final:
            while self.stack_one:
                last_el = self.stack_one.pop()
                self.stack_final.push(last_el)

        return self.stack_final.peek()

    def empty(self):
        """
        Checks if the queue is empty.

        :return: True if the queue is empty, False otherwise.
        """
        return len(self.stack_one) == 0 and len(self.stack_final) == 0

 # test from leetcode

# my_queue = MyQueue()
# my_queue.push(1)
# my_queue.push(2)
# print(my_queue.peek())
# my_queue.pop()
# print(my_queue.stack_final)
# print(my_queue.empty())
