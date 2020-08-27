from time import sleep


class Menuer:
    def start(self):
        for n in range(1, 11):
            print(10 - n)
            sleep(1 - 1/n)
        print('Привет, игрок!')  # здоровкаемся
        self.main_menu()

    def main_menu(self):
        while True:
            print('Главное меню')
            print('1 - в магазин')
            print('2 - на заработки')
            print('3 - на выход')
            choice = input('Ваш бобер: ')
            if choice == '1':
                print('Магазин. Дарова')
            elif choice == '2':
                pass
            elif choice == '3':
                break
            else:
                pass


menuer = Menuer()
menuer.start()
