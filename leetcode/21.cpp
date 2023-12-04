/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode *a = list1;
        ListNode *b = list2;
        ListNode *root = new ListNode();
        ListNode *cur = root;
        while (a || b) {
            if (!a) {
                cur->next = new ListNode(b->val);
                b = b->next;
            } else if (!b || a->val < b->val) {
                cur->next = new ListNode(a->val);
                a = a->next;
            } else {
                cur->next = new ListNode(b->val);
                b = b->next;
            }
            cur = cur->next;
        }
        return root->next;
    }
};