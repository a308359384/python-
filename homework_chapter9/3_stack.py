# 定义一个Stack类，实现数据的出栈、入栈、判空、判满、查找位置、返回栈顶
class Stack:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.items = []

    # 判满
    def Isfull(self):
        return len(self.items) == self.maxsize

    # 判空
    def Isempty(self):
        return len(self.items) == 0

    # 入栈
    def Push(self, item):
        if not self.Isfull():
            self.items.append(item)
        else:
            print("栈满，入栈失败！")

    # 出栈
    def Pop(self):
        if not self.Isempty():
            pop_item = self.items.pop()
            return pop_item
        else:
            print("栈已空，无法出栈")

    # 查找位置
    def Find(self, item):
        if item in self.items:
            index = len(self.items) - 1 - self.items[::-1].index(item)
            print(f"{item} 的位置在栈中的第 {index + 1} 个位置（从栈底开始计数）")
        else:
            print(f"{item} 不在栈中")

    # 返回栈顶
    def Peek(self):
        if not self.Isempty():
            return self.items[-1]
        else:
            print("栈已空，无栈顶元素")

    # 显示栈内元素
    def Display(self):
        print("栈中元素:", self.items)


# 测试
if __name__ == "__main__":
    stack = Stack(maxsize=5)

    stack.Push(1)
    stack.Push(2)
    stack.Push(3)
    stack.Display()

    stack.Pop()
    stack.Display()

    stack.Push('a')
    stack.Push('b')
    stack.Push('c')
    stack.Display()

    stack.Push("123")  # 测试栈已满的情况
    print("栈顶元素:", stack.Peek())

    stack.Find('a')
    stack.Find(6)  # 测试查找不在栈中的元素
