## 23. Merge k Sorted Lists

**Dificuldade:** Difícil

**Link da questão:**

https://leetcode.com/problems/merge-k-sorted-lists/description/

**Link do vídeo**

[![vídeo]()]()



### Cópia do Enunciado:

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.


## Exemplos:

### **Exemplo 1:**

**Input:** lists = [[1,4,5],[1,3,4],[2,6]]

**Output:** [1,1,2,3,4,4,5,6]

**Explanation:** The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6 

### **Exemplo 2:**

**Input:** lists = []

**Output:** []

### **Exemplo 3:**

**Input:** lists = [[]]

**Output:** []

## Constraints

**Constraints:**

-    k == lists.length

-    0 <= k <= 104

-    0 <= lists[i].length <= 500

-    -104 <= lists[i][j] <= 104

-    lists[i] is sorted in ascending order.

-    The sum of lists[i].length will not exceed 104.

