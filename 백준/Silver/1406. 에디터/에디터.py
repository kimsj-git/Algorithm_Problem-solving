import sys

input = sys.stdin.readline


class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


string = input().rstrip()
start = Node(None)
current = start
for i in range(len(string)):
    new_node = Node(string[i])
    current.next = new_node
    new_node.prev = current
    current = new_node

M = int(input())
for _ in range(M):
    cmd = input().split()
    if (cmd[0] == "L") and current.val:
        current = current.prev
    elif (cmd[0] == "D") and current.next:
        current = current.next
    elif (cmd[0] == "B") and current.val:
        current.prev.next = current.next
        if current.next:
            current.next.prev = current.prev
        current = current.prev
    elif cmd[0] == "P":
        new_node = Node(cmd[1])
        if current.next:
            new_node.next = current.next
            current.next.prev = new_node
        new_node.prev = current
        current.next = new_node
        current = new_node

current = start.next
while current and current.val:
    print(current.val, end="")
    current = current.next
