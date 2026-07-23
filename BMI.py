weight = float(input('请输入体重kg'))
height = float(input('请输入身高m'))
bmi = weight / height**2

if bmi < 18.5:
    print(f'{bmi=}体重过低')
elif 18.5 <= bmi < 24:
    print(f'{bmi=}正常')
elif 24 <= bmi <= 28:
    print(f'{bmi=}超重')
else:
    print(f'{bmi=}肥胖')



