class node:
    def __init__(self, val):
        self.value = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def AddTail(self, val):
        if(self.count == 0):
            self.head = node(val)
            self.tail = self.head
            self.count = self.count + 1
        else:
            self.tail.next = node(val)
            self.tail = self.tail.next
            self.count = self.count + 1

    def AddHead(self, val):
        if(self.count == 0):
            self.head = node(val)
            self.tail = self.head
            self.count = self.count + 1
        else:
            temp = node(val)
            temp.next = self.head
            self.head = temp
            self.count = self.count + 1

    def DelTail(self):
        if(self.count == 0):
            pass
        elif (self.count == 1):
            self.head = None
            self.tail = None
        else:
            tracer = self.head
            while(tracer.next != self.tail):
                tracer = tracer.next
            tracer.next = None
            self.tail = tracer
    def DelHead(self):
        if(self.count == 0):
            pass
        elif (self.count == 1):
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next

    def PrintList(self):
        tracer = self.head
        while (tracer.next != None):
            print(tracer.value)
            tracer = tracer.next
        print(tracer.value)


L = LinkedList()

L.AddTail(5)
L.AddTail(10)
L.AddTail(15)
L.AddHead(0)
L.DelHead()
L.DelHead()


L.PrintList()
