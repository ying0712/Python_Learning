import random

def guess_number():
    """
    猜数字游戏（1-100）
    练习点：随机数、循环、条件判断、类型转换、用户输入
    """
    secret_number = random.randint(1,100)  # 生成1-100的随机整数
    attempts = 0
    max_attempts = 10

    print('欢迎来到猜数字游戏！我想了一个1-100的数字，你有十次机会猜哦~')

    while attempts < max_attempts:
        try:
            guess = int(input(f'第{attempts + 1}次尝试，请输入你的猜测：'))
        except ValueError:  #处理非数字输入
            print('请输入一个有效的整数！')
            continue

        attempts += 1
        #判断猜测结果
        if guess < secret_number:
            print("太小了，再试一次。")
        elif guess > secret_number:
            print("太大了，再试一次。")
        else:
            print(f"恭喜 你！你用了{attempts}次猜中了数字 {secret_number} !")
            break  # 猜对了跳出循环

    if attempts == max_attempts and guess != secret_number:
        print(f"很遗憾，机会用完了。正确答案是{secret_number}。")
    #调用函数开始游戏
if __name__=='__main__':
        guess_number()