# -*- coding:utf-8 -*-
"""最大堆
"""


class MaxHeap(object):
    """最大堆
    """
    def __init__(self, arr=None):
        """构造函数

        Args:
            arr(list): 通过数组元素初始化大根堆
        """
        self.data = [0]
        self._size = 0
        if arr:
            # 先把_size赋值，否则build()时_size还没有修改，会出现bug。
            self._size = len(arr)
            self.data.extend(arr)
            self.build()

    def __len__(self):
        return self._size

    def size(self):
        """返回堆大小

        Returns:
            size(int): 堆大小
        """
        return self._size

    def swim(self, i):
        """元素向上调整

        Args:
            i(int): 元素下标
        """
        while i > 1 and self.data[i] > self.data[i//2]:
            self.data[i], self.data[i//2] = self.data[i//2], self.data[i]
            i //= 2

    def sink(self, i):
        """元素向下调整

        Args:
            i(int): 元素下标
        """
        while 2 * i <= self._size:
            j = 2 * i
            if j < self._size and self.data[j] < self.data[j+1]:
                j += 1
            if self.data[j] <= self.data[i]:
                return
            self.data[j], self.data[i] = self.data[i], self.data[j]
            i = j

    def heapify(self, i):
        """维护堆性质

        Args:
            i(int): 位置下标
        """
        while True:
            left_child = i * 2
            right_child = i * 2 + 1

            if left_child <= self._size and self.data[left_child] > self.data[i]:
                largest = left_child
            else:
                largest = i

            if right_child <= self._size and self.data[right_child] > self.data[largest]:
                largest = right_child

            if largest != i:
                self.data[i], self.data[largest] = self.data[largest], self.data[i]
                i = largest
            else:
                return

    def build(self):
        """建堆
        """
        for i in range(len(self)//2, 0, -1):
            self.sink(i)

    def sort(self):
        """堆排序
        """
        for i in range(self._size, 0, -1):
            self.data[1], self.data[i] = self.data[i], self.data[1]
            self._size -= 1
            self.sink(1)

    def maximum(self):
        """返回最大元素

        Returns:
            maximum(int): 堆中最大元素
        """
        return self.data[1]

    def insert(self, x):
        """向堆中插入元素

        Args:
            x(int): 待插入元素
        """
        self.data.append(x)
        self._size += 1
        self.swim(self._size)


if __name__ == '__main__':
    heap = MaxHeap([16, 4, 9, 1, 7, 10, 3, 2, 8, 14])
    print(heap.size())
    print(heap.data)

    print(heap.maximum())
    heap.insert(20)
    print(heap.maximum())
    print(heap.data)
