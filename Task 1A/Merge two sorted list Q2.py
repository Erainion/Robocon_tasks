dummy=ListNode(val=-1)
        a=dummy

        while list1 and list2:
            if(list1.val<list2.val):
                a.next=list1
                list1=list1.next
            else:
                a.next=list2
                list2=list2.next
            a=a.next

        a.next=list1 if list1 else list2
        return dummy.next
