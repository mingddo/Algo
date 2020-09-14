Size = 4
Q = [0]* Size
front, rear = 0, 0
def enQueue(item):
    global rear
    if (rear + 1) % Size == front: #full
        print("Queue Full")
    else:
        rear = (rear + 1) % Size
        Q[rear] = item

def deQueue():
    global front
    if front == rear:
        print("Queue Empty")
    else:
        front = (front + 1) % Size
        return Q[front]

def Qpeek():
    if front == rear:
        print("Queue Empty")

    else:
        return Q[(front + 1) % Size]

enQueue(1)
enQueue(2)
enQueue(3)

print(deQueue())
print(deQueue())
print(deQueue())
enQueue(4)
print(deQueue())

enQueue(5)
print(deQueue())
print(Q)