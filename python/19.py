from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def traverse_me(self):
        currentNode = self
        while currentNode:
            print(currentNode.val, end=" -> ")
            currentNode = currentNode.next
        print("null")

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Solution
        pass

def main():
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    print(f"Original list:")
    head.traverse_me()

    Solution().removeNthFromEnd(head, 2)

    print(f"New list:")
    head.traverse_me()

if __name__ == "__main__":
    main()