class Node(object):
    def __init__(self, elem, next=None):
        self.elem = elem
        self.next = next
class Queue(object):
    def __init__(self):
        self.head = None
        self.rear = None

    def is_empty(self):
        return self.head is None
    def enqueue(self, elem):
        p = Node(elem)
        if self.is_empty():
            self.head = p
            self.rear = p

        else:
            self.rear.next = p
            self.rear = p

    def dequeue(self):
        if self.is_empty():
            print('Queue_is_empty')
        else:
            result = self.head.elem
            self.head = self.head.next
            return result
    def peek(self):
        if self.is_empty():
            print('NOT_FOUND')
        else:
            return self.head.elem

    def print_queue(self):
            print("queue:")
            temp=self.head
            myqueue=[]
            while temp is not None:
                myqueue.append(temp.elem)
                temp = temp.next

if __name__=="__main__":
    queue=Queue()
    queue.enqueue(21)
    queue.enqueue(35)
    queue.enqueue(58)
    queue.enqueue(13)
    queue.print_queue()
    print(queue.peek())
    queue.dequeue()
    queue.print_queue()
    print(queue.peek())
