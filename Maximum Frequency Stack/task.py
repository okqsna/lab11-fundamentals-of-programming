"""
Design a stack-like data structure to push elements
to the stack and pop the most frequent element from the stack.
"""
class Queue:
    """
    Data structure queue.
    """
    def __init__(self):
        """
        Data initiializer for queue
        """
        self.queue = []

    def push(self, x):
        """
        Adding element to queue
        :param x: element to be added
        """
        self.queue.append(x)

    def peek(self):
        """
        Returns the top item of the queue.

        :return: The top item of the stack.
        """
        if self.queue:
            return self.queue[0]

    def pop(self):
        """
        Removing element from queue
        """
        if not self.queue:
            return None
        return self.queue.pop(0)

    def __len__(self):
        """
        Getting length of queue
        :return: int,  length of queue
        """
        return len(self.queue)

    def empty(self):
        """
        Checking if queue is empty

        :return: bool, empty of full
        """
        return len(self.queue) == 0

    def __str__(self):
        """
        Returns a string representation of the queue.

        :return: A string representing the queue.
        """
        return str(self.queue)

class Stack:
    """
    Data structure stack.
    """

    def __init__(self):
        """
        Initializes an empty stack.
        """
        self.__index = []

    def __len__(self) -> int:
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

    def __str__(self)-> str:
        """
        Returns a string representation of the stack.

        :return: A string representing the stack.
        """
        return str(self.__index)


class FreqStack(object):
    """
    Frequency stack implementation
    """

    def __init__(self):
        pass

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        pass

    def pop(self):
        """
        :rtype: int
        """
        pass
