class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList(object):

    def __init__(self):
        self.head = None
        self.length = 0

    def get_node(self, i:int) -> Node:
        n = self.head
        for _ in range(i):
            n = n.next
        return n

    # O(1)
    def insert_first(self, data):
        new_node = Node(data)
        self.length += 1
        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
    # O(N)
    def __str__(self):
        elems = ''
        current_node = self.head
        while current_node:
            if current_node.next is None:
                elems += str(current_node.data)
            else:
                elems += str(current_node.data) + ', '
            current_node = current_node.next
        return '[' + elems +']'
    # O(1)
    def __len__(self):
        return self.length

    # 連結リストの要素数を数える方法
    # O(N)
    # def __len__(self):
    #     node = self.head
    #     size = 0
    #     while node is not None:
    #         size += 1
    #         node = node.next
    #     return size

    # O(N)
    def insert_last(self, data):
        if self.head is None:
            self.insert_first(data)
        else:
            new_node = Node(data)
            self.length += 1
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next

            current_node.next = new_node
    # O(N)
    def remove(self, data):
        if self.head is None:
            print('リストは空です。')
            return
        current_node = self.head
        previous_node = None
        while current_node.data != data:
            if current_node.next is None:
                print('削除に該当するデータがありません。')
                return
            previous_node = current_node
            current_node = current_node.next

        # 削除ノードが先頭
        if previous_node is None:
            self.head = current_node.next
            self.length -= 1
        else:
            previous_node.next = current_node.next
            self.length -= 1

if __name__ == '__main__':
    linked_list = LinkedList()
