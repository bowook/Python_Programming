class Node:
    def __init__(self, value = 0, next = None):
        self.value = value
        self.next = next

class LinkedList(object):
    def __init__(self):
        self.head = None
        #self.tail = None
    def append(self, value):
        new_Node = Node(value)
        #근데 아직 head는 지정이 안됨
        if self.head == None:
            self.head = new_Node
        else:
            current = self.head
            while current.next:
                #현재 노드의 다음이 있음? 그러면 동작
                #head부터 시작해서 마지막노드까지 이동해야함
                current = current.next
            #while문이 동작하지 않는다는건 마지막 node임
            #그러면 current가 현재 마지막 노드니까,
            current.next = new_Node
            #current.next에 new_Node 설정
    def get(self, idx):
        current = self.head
        for _ in range(idx):
            current = current.next
        return current.value
    
    def insert(self, idx, value):
        if self.head is None:
            return
        previous = self.head
        new_Node = Node(value)
        for _ in range(idx-1):
            previous = previous.next
        #idx가 2야, 그러면 1을 가리키고 있는 상태
        temp_Node = previous.next
        #노드를 연결하기이전에 다음 노드의 주소를 저장해야하는 temp_Node
        previous.next = new_Node
        #저장했으니까, 이전에 다음은 새로 들어온 노드
        new_Node.next = temp_Node
        #새로 들어온 노드를 연결했으니까 그 노드의 다음은 temp_Node로 연결
    def remove(self, idx):
        if self.head == None:
            return
        current = self.head
        if idx == 0:
            #head를 지우란 소리네
            self.head = current.next
            current = None
            return
        for _ in range(idx-1):
            #이전 노드 까지 접근
            current = current.next
        #current는 현재 삭제할 노드 이전 노드임
        temp_node = current
        for _ in range(1):
            current = current.next
        #current는 현재 삭제할 노드임
        delete_next_node = current.next
        temp_node.next = delete_next_node
    # def append_tail_version(self, value):
    #     new_node = Node(value)
    #     if self.head is None:
    #         self.head = new_node
    #     else:
    #         self.tail.next = new_node
    #         self.tail = self.tail.next

ll = LinkedList() #인스턴스 만들어서 접근
ll.append(1) #value값이 1인 Node 생성
ll.append(2) #value값이 2인 Node 생성
ll.append(3)
ll.append(4)
ll.get(0)
ll.get(1)
ll.get(3)
ll.get(2)
ll.insert(idx = 2, value = 9)
ll.remove(3)
