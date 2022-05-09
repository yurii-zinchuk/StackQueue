"""
Queue to stack converter.
"""

from linkedqueue import LinkedQueue
from linkedstack import LinkedStack


def queue_to_stack(old_queue: LinkedQueue) -> LinkedStack:
    """Convert queue to stack.

    Args:
        old_queue (LinkedQueue): Queue to be converted.

    Returns:
        LinkedStack: Stack made from the queue.
    """
    new_stack = LinkedStack()
    queue_l = list(old_queue)
    for elem in reversed(queue_l):
        new_stack.push(elem)
    return new_stack


if __name__ == "__main__":
    queue = LinkedQueue()
    for i in range(10):
        queue.add(i)
    stack = queue_to_stack(queue)
    print(queue)
    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(stack)
    # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    print(stack.pop())
    # 0
    print(queue.pop())
    # 0
    stack.add(11)
    queue.add(11)
    print(queue)
    # [1, 2, 3, 4, 5, 6, 7, 8, 9, 11]
    print(stack)
    # [9, 8, 7, 6, 5, 4, 3, 2, 1, 11]
