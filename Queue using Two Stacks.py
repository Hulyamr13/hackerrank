# Enter your code here. Read input from STDIN. Print output to STDOUT

class MyQueue:
    def __init__(self):
        self.stack_enqueue = []
        self.stack_dequeue = []

    def enqueue(self, x):
        self.stack_enqueue.append(x)

    def dequeue(self):
        if not self.stack_dequeue:
            while self.stack_enqueue:
                self.stack_dequeue.append(self.stack_enqueue.pop())
        if self.stack_dequeue:
            return self.stack_dequeue.pop()

    def peek(self):
        if not self.stack_dequeue:
            while self.stack_enqueue:
                self.stack_dequeue.append(self.stack_enqueue.pop())
        if self.stack_dequeue:
            return self.stack_dequeue[-1]


if __name__ == '__main__':
    q = int(input())
    queue = MyQueue()

    for _ in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            queue.enqueue(query[1])
        elif query[0] == 2:
            queue.dequeue()
        elif query[0] == 3:
            print(queue.peek())
