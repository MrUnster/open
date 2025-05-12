class Node:
    __counter = 0

    def __init__(self):
        self.value = None
        self.prev = None
        self.next = None
        self.__id = Node.__counter
        Node.__counter += 1
    
    def get_id(self):
        return self.__id

    def __hash__(self):
        return hash(self.__id)

    def __del__(self):
        pass

class LinkedList:
    '''
        LinkedList[i]           - O(n)
        LinkedList.add()        - O(1)
        LinkedList.addleft()    - O(1)
        LinkedList.pop()        - O(1)
        LinkedList.popleft()    - O(1)
        LinkedList.clear()      - O(1)
    '''
    
    def __init__(self):
        self.__len = 0
        self.__root = Node()
        self.__leaf = Node()
        self.__root.next = self.__leaf
        self.__leaf.prev = self.__root

    def get_start(self):
        return self.__root.next

    def __len__(self):
        return self.__len

    def to_list(self, start = None, end = None):
        if start == None: start = self.__root.next
        r = list()
        while start != end and start.next != None:
            r.append(start.value)
            start = start.next
        return r

    def __iter__(self):
        return self.to_list().__iter__()

    def __getitem__(self, item, start = None):
        if start == None: start = self.__root.next
        if item == 0: return start
        return self.__getitem__(item - 1, start.next)
    
    def add(self, value):
        node = Node()
        node.value = value
        node.prev = self.__leaf.prev
        node.next = self.__leaf
        self.__leaf.prev.next = node
        self.__leaf.prev = node
        self.__len += 1
        return node

    def addleft(self, value):
        node = Node()
        node.value = value
        node.prev = self.__root
        node.next = self.__root.next
        self.__root.next.prev = node
        self.__root.next = node
        self.__len += 1
        return node

    def pop(self):
        node = self.__leaf.prev
        node.prev.next = self.__leaf
        self.__leaf.prev = node.prev
        self.__len -= 1
        return node

    def popleft(self):
        node = self.__root.next
        node.next.prev = self.__root
        self.__root.next = node.next
        self.__len -= 1
        return node

    def clear(self):
        self.__root.next = self.__leaf
        self.__leaf.prev = self.__root

class NamedLinkedList(LinkedList):
    '''
        NamedLinkedList[name]        - O(1)
        NamedLinkedList.pop()        - O(1)
        NamedLinkedList.pop(name)    - O(1)
        NamedLinkedList.popleft()    - O(1)
        NamedLinkedList.add()        - O(1)
        NamedLinkedList.add(name)    - O(1)
        NamedLinkedList.addleft()    - O(1)
        NamedLinkedList.clear()      - O(1)
    '''

    def __init__(self):
        super().__init__()
        self.__len = 0
        self.__names = dict()
        self.__nodes = dict()
    
    def to_list(self, start = None, end = None):
        if start == None: start = self.get_start()
        r = list()
        while start != end and start.next != None:
            r.append((self.__nodes[start], start.value))
            start = start.next
        return r
    
    def __getitem__(self, item):
        if item not in self.__names.keys(): return None
        return self.__names[item]

    def add(self, name, value):
        if name in self.__names.keys(): return None
        node = super().add(value)
        self.__names[name] = node
        self.__nodes[node] = name
        return node
    
    def addleft(self, name, value):
        if name in self.__names.keys(): return None
        node = super().addleft(value)
        self.__names[name] = node
        self.__nodes[node] = name
        return node
    
    def addbefore(self, target, name, value):
        if name in self.__names.keys(): return None
        if target in self.__names.keys():
            target = self.__names[target]
            node = Node()
            self.__names[name] = node
            self.__nodes[node] = name
            node.value = value
            node.prev = target.prev
            node.next = target
            target.prev.next = node
            target.prev = node
            self.__len += 1
            return node
        return None

    def addafter(self, target, name, value):
        if name in self.__names.keys(): return None
        if target in self.__names.keys():
            target = self.__names[target]
            node = Node()
            self.__names[name] = node
            self.__nodes[node] = name
            node.value = value
            node.prev = target
            node.next = target.next
            target.next.prev = node
            target.next = node
            self.__len += 1
            return node
        return None

    def pop(self, name = None):
        if name == None:
            node = super().pop()
            name = self.__nodes[node]
        elif name not in self.__names.keys():
            return None
        else:
            node = self.__names[name]
            node.prev.next = node.next
            node.next.prev = node.prev
        self.__nodes.pop(node)
        self.__names.pop(name)
        self.__len -= 1
        return node

    def popleft(self):
        node = super().popleft()
        name = self.__nodes[node]
        self.__nodes.pop(node)
        self.__names.pop(name)
        self.__len -= 1
        return node

    def clear(self):
        super().slear()
        self.__names.clear()
        self.__nodes.clear()

if __name__ == '__main__':
    nll = NamedLinkedList()

    for i in range(10):
        nll.add(chr(ord('a')+i), 100+i)
    print(list(nll))

    for i in range(10):
        nll.addleft('l' + chr(ord('a')+i), i)
    print(list(nll))

    nll.addbefore('a', 'aaa', 777)
    nll.addafter('a', 'bbb', 666)
    print(list(nll))

    for i in range(5):
        nll.pop(chr(ord('a')+i))
        nll.pop('l' + chr(ord('a')+i))
    print(list(nll))

    for i in range(2):
        nll.popleft()
        nll.pop()
    print(list(nll))

    for e in 'ghf':
        print(nll[e].value)