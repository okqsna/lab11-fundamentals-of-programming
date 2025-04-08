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
    Frequency stack implementation
    """

    def __init__(self):
        self.freqstack = Stack()
        self.all_el = {}
        self.all_curr_stacks = {}

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.freqstack.push(val)
        if val not in self.all_el:
            self.all_el.setdefault(val, 1)
        else:
            self.all_el[val] += 1
        

    def pop(self):
        """
        :rtype: int
        """
        all_dict = self.all_el
        el = self.freqstack.pop()

        curr_key = 0
        for key, val in all_dict.items():
            if all_dict[el] >= val:
                curr_key = el
            else:
                curr_key = key
        all_dict[curr_key] -= 1
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
print(freqStack.freqstack)
print(freqStack.pop())
