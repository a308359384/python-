def get_valid_score():
    while True:
        try:
            score = int(input("请输入成绩 (1-100)："))
            if 1 <= score <= 100:
                return score
            else:
                print("成绩必须在1到100之间，请重新输入。")
        except ValueError:
            print("输入无效，请输入一个整数。")

score = get_valid_score()
print(f"你输入的成绩是: {score}")
