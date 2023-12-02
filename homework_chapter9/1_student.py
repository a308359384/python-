# 定义一个学生类，包括学号、姓名、出生日期三个属性（数据成员）；
# 包括一个用于给定数据成员初始值的构造函数；
# 包含一个计算学生年龄的方法。编写该类并对其进行测试。
from datetime import datetime
class Student:
    def __int__(self,stu_id,name,birth_day):
        # 构造函数，用于初始化学生对象的属性
        self.stu_id=stu_id
        self.name=name
        self.birth_day=birth_day

    def calculate_age(self):
         # 计算学生年龄的方法
         today = datetime.today()  # 获取当前日期时间
         birth_day = datetime.strptime(self.birth_day, "%Y-%m-%d")  # 将出生日期字符串转换为datetime对象
         age = today.year - birth_day.year - ((today.month, today.day) < (birth_day.month, birth_day.day))
         return age

if __name__ == "__main__":
    # 创建一个学生对象
    student1 = Student(stu_id="S001", name="John Doe", birth_day="2000-01-15")

    # 输出学生信息
    print("学号:", student1.stu_id)
    print("姓名:", student1.name)
    print("出生日期:", student1.birth_day)

    # 计算并输出学生年龄
    age = student1.calculate_age()
    print("年龄:", age)