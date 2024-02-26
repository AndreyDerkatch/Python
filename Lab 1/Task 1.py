#Вариант 5
#1 Найти количество делителей числа, не делящихся на 3.
def f1(x):
    k = 0
    for i in range(1, x+1):
        if x%i == 0 and i%3 != 0:
            k+=1
    return k

print(f1(15))

#2 Найти минимальную нечетную цифру числа.
def f2(x):
    min = 10
    while x>0:
        if x%10%2 != 0 and x%10<min and x%10!=1:
            min = x%10
        x//=10
    if min == 10:
        return "Нечетных цифр в числе нет"
    else:
        return min

print(f2(2425))

#3 Найти сумму всех делителей числа, взаимно простых с
#суммой цифр числа и не взаимно простых с произведением цифр числа.
def sum(x):
    s = 0
    while x>0:
        s+=x%10
        x//=10
    return s

def proiz(x):
    p=1
    while x>0:
        p*=x%10
        x//=10
    return p

def prost(x,y):
    m = min(x,y)
    for i in range(2, m+1):
        if x%i==0 and y%i==0:
            return True
            break
    return False

def result(x):
    s = 0
    for i in range(1,x+1):
        if (x%i==0 and prost(i,sum(x)) and not prost(i,proiz(x))):
            s+=i
    return s

print("Введите х:")
x = int(input())
print(result(x))
