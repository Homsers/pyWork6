numbers = list(range(1, 10))
victory_comb = [(1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7)]

def map():
    for i in range(3):
        print()
        print(numbers[0+i*3] , '', numbers[1+i*3], '', numbers[2+i*3])
    print()


def inputs(choices):
    while True:
        value = input('Выберите цифру: '+ choices)
        if not (value in '123456789'):
            print('Это не цифра! ')
            continue
        value = int(value)
        if str(numbers[value -1]) in 'XO':
            print('Эта цифра уже выбрана! ')
            continue
        numbers[value-1] = choices
        break



def winning_comb():
    for i in victory_comb:
        if (numbers[i[0]-1]) == (numbers[i[1]-1]) == (numbers[i[2]-1]):
            return numbers[i[1]-1]
    return False

def main():
    count = 0
    while True:
        map()
        if count % 2 == 0:
            inputs ('X')
        else:
            inputs ('O')
        if count > 3:
            winner = winning_comb()
            if winner:
                map()
                print(winner + ' Победил!')
                break
        count +=1
        if count == 9:
            map()
            print('Ничья!!!')
            break

main()