name = 'wonsang'
age = 21
eyes_color = 'black'

print(f'hi! my name is {name}, I am {age} years old. my eyes have {eyes_color} colors.')

def make_juice(fruit):
    return f"{fruit} + juice"

def add_ice(juice):
    return f"{juice} + ice"

def add_sugar(cold_juice):
    return f"{cold_juice} + sugar"

juice = make_juice('apple')
cold_juice = add_ice(juice)
perfect_juice = add_sugar(cold_juice)

print(perfect_juice)

# return 후 함수는 종료된다 = return 뒤의 문장은 실행되지 않음