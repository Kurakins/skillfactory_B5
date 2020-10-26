# Создадим глобальную переменную со списком чисел от 1 до 9
# Erstellung einer globalen Variablen mit den Zahlen 1 bis 9
board = list(range(1, 10))

# Создадим переменную с выигрышными комбинациями (список кортежей)
# Erstellung einer Variablen mit Gewinnkombinationen (Liste mit Abfolgen)
win_combo = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]

# Функция для отрисовки игрового поля 3x3
# Zeichenfunktion für das Spielfeld 3x3
def draw_board():
    print("_____________")
    for i in range(3):
        print("|", board[0 + i * 3], "|", board[1 + i * 3], "|", board[2 + i * 3], "|")
        print("_____________")

# Функция для взаимодействия игроков с полем, проверяет условия ввода нужного числа от 1 до 9 и занято поле или нет
# Interaktionsfunktion der Spieler mit dem Spielfeld. Prüft Eingabe der richtigen Zahl 1 bis 9 und ob das Feld frei ist.
def take_input(player_token):
    while True:
        value = input("Please place " + player_token + " ")
        if not (value in '123456789'):
            print("Wrong input, please retry.")
            continue
        value = int(value)
        if str(board[value - 1]) in "XO":
            print("The field is occupied")
            continue
        board[value - 1] = player_token
        break

# Функция проверки выигрышных комбинаций. Возвращает False если нет совпадений.
# Funktion zur Prüfung der Gewinnerkombination. Gibt False zurück, wenn es keine Übereinstimmung gibt.
def check_win():
    for each in win_combo:
        if (board[each[0] - 1]) == (board[each[1] - 1]) == (board[each[2] - 1]):
            return board[each[1] - 1]
    else:
        return False

# Задаем главную функцию
# Hauptfunktion
def main():
    counter = 0  # Переменная-счетчик для подсчета количества ходов
    # Variable-Zähler für die Berechnung der Züge
    while True:
        draw_board()
        if counter % 2 == 0:
            take_input("X")
        else:
            take_input("O")
        if counter > 3:  # Если ходов больше 3, проверка на выигрышные комбинации
            # Bei über drei Zügen Prüfung auf Gewinnerkombination
            winner = check_win()
            if winner:  # Объявлем победителя если есть совпадения с выигрышными комбинациями
                # Gewinner wird erklärt, wenn es Übereinstimmung mit Gewinnerkombinationen gibt.
                draw_board()
                print(winner, "won!")
                break
        counter += 1
        if counter > 8:  # Если ходов больше и победителя нет, объявление ничьей
            # Unentschieden, wenn es weitere Züge gibt, jedoch keinen Gewinner
            draw_board()
            print("Remis!")
            break

main()
