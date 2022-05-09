"""
Stack to queue converter.
"""

from linkedstack import LinkedStack
from linkedqueue import LinkedQueue


def stack_to_queue(old_stack: LinkedStack) -> LinkedQueue:
    """Comvert stack to queue.

    Args:
        old_stack (LinkedStack): Stack to be converted.

    Returns:
        LinkedQueue: New queue from the stack.
    """
    new_queue = LinkedQueue()
    stack_l = list(old_stack)
    for elem in reversed(stack_l):
        new_queue.add(elem)
    return new_queue


if __name__ == "__main__":
    stack = LinkedStack()
    for i in range(10):
        stack.add(i)
    queue = stack_to_queue(stack)
    print(queue)
    # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    print(stack)
    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(stack.pop())
    # 9
    print(queue.pop())
    # 9
    stack.add(11)
    queue.add(11)
    print(queue)
    # [8, 7, 6, 5, 4, 3, 2, 1, 0, 11]
    print(stack)
    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 11]
