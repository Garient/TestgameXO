def start():
    print("---------------------------")
    print("|  Игра 'Крестики-Нолики' |")
    print("|                         |")
    print("|      Правила игры:      |")
    print("| Игроки ходят по очереди |")
    print("|  Три в ряд выигрывают   |")
    print("|    Чтобы сделать ход:   |")
    print("| Введите координаты x y: |")
    print("|   x строка, y столбец   |")
    print("---------------------------")

def print_field():
    print()
    print("    | 1 | 2 | 3 | ")
    print("  --------------- ")
    for i, row in enumerate(field):
        stroka = f"  {i+1} | {' | '.join(row)} | "
        print(stroka)
        print("  --------------- ")
    print()

def hod():
    while True:
        cords = input("         Ваш ход: ").split()

        if len(cords) != 2:
            print(" Введите 2 координаты! ")
            continue

        x, y = cords

        if not (x.isdigit()) or not (y.isdigit()):
            print(" Введите числа! ")
            continue

        x, y = int(x)-1, int(y)-1

        if 0 > x or x > 2 or 0 > y or y > 2:
            print(" Координаты вне диапазона! ")
            continue

        if field[x][y] != " ":
            print(" Клетка занята! ")
            continue

        return x, y

def win_logic():
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("Выиграл X!!!")
            return True
        if symbols == ["0", "0", "0"]:
            print("Выиграл 0!!!")
            return True
    return False

start()
field = [[" "] * 3 for i in range(3)]
count = 0
while True:
    count += 1
    print(f'      Это {count} ход.')
    print_field()
    if count % 2 == 1:
        print(" Ходит крестик!")
    else:
        print(" Ходит нолик!")

    x, y = hod()

    if count % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"

    if win_logic():
        break

    if count == 9:
        print(" Ничья!")
        break