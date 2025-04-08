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

    def add(self, x):
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
        self.freqstack = Queue()

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.freqstack.add(val)

    def pop(self):
        """
        :rtype: int
        """
        all_dict = {}
        queue_second = Queue()

        while self.freqstack:
            el = self.freqstack.pop()
            queue_second.add(el)
            all_dict.setdefault(el, 0)
            if el in all_dict:
                all_dict[el] += 1
        print(all_dict)
        curr_val = 0
        curr_key = None
        for key, val in all_dict.items():
            if curr_val < val:
                curr_val = val
                curr_key = key

        all_dict.pop(curr_key)
        for key in all_dict:
            self.freqstack.add(key)
        return curr_key


#leetcode tests
# FreqStack freqStack = new FreqStack();
# freqStack.push(5); // The stack is [5]
# freqStack.push(7); // The stack is [5,7]
# freqStack.push(5); // The stack is [5,7,5]
# freqStack.push(7); // The stack is [5,7,5,7]
# freqStack.push(4); // The stack is [5,7,5,7,4]
# freqStack.push(5); // The stack is [5,7,5,7,4,5]
# freqStack.pop();   // return 5, as 5 is the most frequent. The stack becomes [5,7,5,7,4].
# freqStack.pop();   // return 7, as 5 and 7 is the most frequent, but 7 is closest to the top. The stack becomes [5,7,5,4].
# freqStack.pop();   // return 5, as 5 is the most frequent. The stack becomes [5,7,4].
# freqStack.pop();   // return 4, as 4, 5 and 7 is the most frequent, but 4 is closest to the top. The stack becomes [5,7].

freqStack = FreqStack()
freqStack.push(5)
freqStack.push(7)
freqStack.push(5)
freqStack.push(7)
freqStack.push(4)
freqStack.push(5)
print(freqStack.freqstack)
print(freqStack.pop())
print(freqStack.pop())
print(freqStack.pop())
print(freqStack.pop())
