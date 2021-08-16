//Given head, the head of a linked list, determine if the linked list has a cycle in it.

//There is a cycle in a linked list if there is some node in the list that can be reached
//again by continuously following the next pointer. Internally, pos is used to denote the
//index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

//Return true if there is a cycle in the linked list. Otherwise, return false.



#include <iostream>

using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    bool hasCycle(ListNode *head) {
        if (head == nullptr || head->next == nullptr) return false;
        ListNode *fast = head, *slow = head;
        while (fast->next != nullptr && fast->next->next != nullptr) {
            fast = fast->next->next;
            slow = slow->next;
            if (fast == slow) return true;
        }
        return false;
    }
};

int main()
{
    {
        // 1->2->3->4->5->6->3
        ListNode n1(1), n2(2), n3(3), n4(4), n5(5), n6(6);
        n1.next = &n2;
        n2.next = &n3;
        n3.next = &n4;
        n4.next = &n5;
        n5.next = &n6;
        n6.next = &n3;
        Solution s;
        bool res = s.hasCycle(&n1);
        assert(res);
    }
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
        bool res = s.hasCycle(&n1);
        assert(!res);
    }
    return 0;
}
