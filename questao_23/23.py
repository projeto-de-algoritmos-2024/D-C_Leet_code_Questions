""" 
23. Merge k Sorted Lists
https://leetcode.com/problems/merge-k-sorted-lists/
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists: 
            return None
        
        def merge(l1: ListNode, l2: ListNode) -> ListNode:
            novaLista = ListNode()
            p = novaLista

            while(l1 and l2):
                if l1.val > l2.val:
                    p.next = l2
                    l2 = l2.next
                else:
                    p.next = l1
                    l1 = l1.next
                p = p.next
            if l1:
                p.next = l1
            if l2: 
                p.next = l2
            
            return novaLista.next
        
        def mergeSort(lists: list[Optional[ListNode]], l: int, r: int) -> Optional[ListNode]:
            if l == r:
                return lists[l]
            m = (l+r)//2
            if l < r:
                l1 = mergeSort(lists, l, m)
                l2 = mergeSort(lists, m + 1, r)
                return merge(l1, l2)
            
        return mergeSort(lists, 0, len(lists) - 1)