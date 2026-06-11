def calculator():
    print("=" * 30)
    print("  简单计算器")
    print("=" * 30)
    print(": +  -  *  /")
    print("序")
    print("=" * 30)

    while True:
        try:
            # 输入第一个数字
            first = input("\n请输入第一个数字: ")
            if first.lower() == 'q':
                print("再见！")
                break
            num1 = float(first)

            # 输入运算符
            op = input("请输入运算符 (+ - * /): ")
            if op.lower() == 'q':
                print("再见！")
                break

            # 输入第二个数字
            second = input("请输入第二个数字: ")
            if second.lower() == 'q':
                print("再见！")
                break
            num2 = float(second)

            # 计算结果
            if op == '+':
                result = num1 + num2
                print(f"{num1} + {num2} = {result}")
            elif op == '-':
                result = num1 - num2
                print(f"{num1} - {num2} = {result}")
            elif op == '*':
                result = num1 * num2
                print(f"{num1} × {num2} = {result}")
            elif op == '/':
                if num2 == 0:
                    print("错误：除数不能为 0！")
                else:
                    result = num1 / num2
                    print(f"{num1} ÷ {num2} = {result}")
            else:
                print("不支持的运算符，请使用 + - * /")

        except ValueError:
            print("输入无效，请输入数字！")
        except Exception as e:
            print(f"发生错误: {e}")

if __name__ == "__main__":
    calculator()
