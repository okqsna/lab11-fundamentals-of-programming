"""
Implement Stack using Queues
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


class MyStack(object):
    """
    A stack implemented using two queues.
    """

    def __init__(self):
        """
        Initializes an empty stack using two queues.
        """
        self.queue_one = Queue()
        self.queue_final = Queue()

    def push(self, x):
        """
        Adding element to stack
        :param x: element to be added
        """
        self.queue_final.push(x)
        self.queue_one.push(x)

        for _ in range(1, len(self.queue_one) + 1):
            el_one = self.queue_one.pop()
            self.queue_final.push(el_one)

        self.queue_one, self.queue_final = self.queue_final, self.queue_one

    def pop(self):
        """
        Removing element from stack
        """
        return self.queue_one.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.queue_one.peek()


    def empty(self):
        """
        :rtype: bool
        """
        return self.queue_one.empty()

# leetcode test

# mystack = MyStack()
# mystack.push(1)
# mystack.push(2)
# print(mystack.top())
# print(mystack.pop())
# print(mystack.empty())

# leetcode test

# mystack = MyStack()
# mystack.push(1)
# print(mystack.pop())
# print(mystack.empty())

