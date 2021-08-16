#include <iostream>

using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    // 非递归
    ListNode* reverseList(ListNode* head) {
        if (head == nullptr || head->next == nullptr) return head;
        ListNode *pre = head, *cur = head->next;
        pre->next = nullptr;
        while (cur != nullptr) {
            ListNode *next = cur->next;
            cur->next = pre;
            pre = cur;
            cur = next;
        }
        return pre;
    }
    // 递归
    ListNode* reverseList2(ListNode* head) {
        if (head == nullptr || head->next == nullptr) return head;
        ListNode *last = reverseList2(head->next);
        head->next->next = head;
        head->next = nullptr;
        return last;
    }
    void print(ListNode* head) {
        if (head == nullptr) return;
        ListNode *temp = head;
        while (temp != nullptr) {
            cout << temp->val << " --> ";
            temp = temp->next;
        }
        cout << "end." << endl;
    }
};

int main()
{
    {
        // 1->2->3->4->5->6
        ListNode n1(1), n2(2), n3(3), n4(4), n5(5), n6(6);
        n1.next = &n2;
        n2.next = &n3;
        n3.next = &n4;
        n4.next = &n5;
        n5.next = &n6;
        n6.next = nullptr;
        Solution s;
        cout << "Before: " << endl;
        s.print(&n1);
        ListNode *res = s.reverseList2(&n1);
        cout << "After: " << endl;
        s.print(res);

    }
    return 0;
}
