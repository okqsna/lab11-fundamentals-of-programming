"""
Design a stack-like data structure to push elements
to the stack and pop the most frequent element from the stack.
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


class FreqStack(object):
    """
    Frequency stack implementation that pops the most frequent element.
    """
    def __init__(self):
        self.freqstack = Stack()
        self.freq_map = {}
        self.stack_map = {}
        self.curr_freq_max = 0

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.freqstack.push(val)

        if val not in self.freq_map:
            self.freq_map.setdefault(val, 1)
        else:
            self.freq_map[val] += 1

        curr_freq = self.freq_map[val]
        if curr_freq > self.curr_freq_max:
            self.curr_freq_max = curr_freq

        if curr_freq not in self.stack_map:
            self.stack_map.setdefault(curr_freq, Stack())
        self.stack_map[curr_freq].push(val)

    def pop(self):
        """
        :rtype: int
        """
        el = self.stack_map[self.curr_freq_max].pop()
        self.freq_map[el] -= 1

        if not self.stack_map[self.curr_freq_max]:
            self.curr_freq_max -= 1

        return el

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

# freqStack = FreqStack()
# freqStack.push(5)
# freqStack.push(7)
# freqStack.push(5)
# freqStack.push(7)
# freqStack.push(4)
# freqStack.push(5)
# print(freqStack.freqstack)
# print(freqStack.pop())
# print(freqStack.pop())
# print(freqStack.pop())
# print(freqStack.freqstack)
# print(freqStack.pop())
