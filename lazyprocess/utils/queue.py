from typing import Generic
from typing import TypeVar
from typing import Optional

T = TypeVar("T")

class Node(Generic[T]):
    def __init__(self, value: T):
        self.value = value
        self.next: Optional[Node] = None 

class Queue(Generic[T]):
    def __init__(self):
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None
        self.size: int = 0

    def __len__(self) -> int:
        return self.size

    def enqueue(self, value: T) -> None:
        node = Node(value)
        
        if self.head == None:
            self.head = node
            self.tail = node
            self.size += 1

            return None
        
        self.tail.next = node
        self.tail = node
        self.size += 1

    def dequeue(self) -> Optional[T]:
        if self.head == None:
            return None
        
        node = self.head

        nodeValue = node.value
        
        self.head = self.head.next

        del node

        if not self.head:
            self.tail = None

        return nodeValue
    