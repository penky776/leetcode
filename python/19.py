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
        if head is None:
            return None

        # Find length of linked list
        count_me = head
        new_head = head
        sz = 0
        while count_me:
            count_me = count_me.next
            sz += 1

        print(f"{sz} is the length of the linked list")

        if not (1 <= sz <= 30) or not (1 <= n <= sz):
            raise Exception("invalid parameters")

        # Example / Case 1
        # Input: head = [1,2,3,4,5], n = 2
        # Output: [1,2,3,5]

        # [1,2]
        # 2

        # [1,2,3]
        # 2
        # [1,3]

        change_index = sz - n - 1 
        print(f"Index of change is {change_index}")

        if (change_index == 0) and (sz == 2):
            new_head.next = None
            return new_head

        if (change_index < 0):
            new_head = new_head.next
            return new_head
    
        print("initial")
        new_head.traverse_me()
        for i in range(0, sz):
            print(f"Current iteration count is {i}")

            if (i == change_index):
                new_head.next = new_head.next.next

                print(f"head is {new_head}")
                new_head.traverse_me()
                break
            else:
                new_head = new_head.next
                new_head.traverse_me()

        return head
            

def main():
    # head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    # head = ListNode(1, None)
    head = ListNode(1, ListNode(2, ListNode(3)))
    # head = ListNode(1, ListNode(2))

    print(f"Original list:")
    head.traverse_me()

    new_head = Solution().removeNthFromEnd(head, 2)

    print(f"New list:")
    new_head.traverse_me() 

if __name__ == "__main__":
    main()