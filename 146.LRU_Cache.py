#!/usr/bin/env python3

class Node:
    def __init__(self, key, val, next=None):
        self.key = key
        self.val = val
        self.next = next


class LRUCache:

    def __init__(self, capacity: int):
        head = Node(None, None)
        self.head = head
        self.curr = head
        self.cap = capacity
        self.d = {}

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            self.d[key].next.val = value
            self.get(key)
            return

        node = Node(key, value)

        self.d[key] = self.curr
        self.curr.next = node
        self.curr = node

        if len(self.d) > self.cap:
            node = self.head.next
            del self.d[node.key]

            self.head.next = node.next
            self.d[node.next.key] = self.head

    def get(self, key: int) -> int:
        if key not in self.d:
            return -1

        prev, node = self.d[key], self.d[key].next
        if self.curr != node:
            prev.next = node.next
            self.d[node.next.key] = prev

            self.curr.next = node
            self.d[node.key] = self.curr

            node.next = None
            self.curr = node

        return node.val


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
