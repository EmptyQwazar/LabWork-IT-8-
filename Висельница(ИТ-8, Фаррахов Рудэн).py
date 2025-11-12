slovo1 = str(input("Введите слово которое вы загадали: "))
slovo2 = []

for i in range(len(slovo1)):
    slovo2.append(slovo1[i])
b = [0]*(len(slovo2))
print('Угадай слово')
print('В слове:',len(slovo2),'букв')
k = 0
while (0 in b):
    print(b)
    s = str(input("Введи букву "))
    if s in slovo2:
        for i in range(len(slovo2)):
            if s == slovo2[i]:
                print("Ты угадал букву!")
                b[i] = s
    else:
        print("Ты не угадал букву!")
        print("У тебя осталось ", 6-k," попыток")
        k+=1
    if k == 7:
        break

if not(0 in b):
    print('Ты угадал слово!')
    print(b)
if k == 7:
    print("Тебя повесили!")
