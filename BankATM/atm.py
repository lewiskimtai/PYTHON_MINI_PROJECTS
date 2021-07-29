m = 0
user_list = []
password_list = []
verify = "M"
info_list = []
answer = ""
x = 0
while(m < 100000):
    user_list.append(0)
    password_list.append(0)
    info_list.append(0)
    m += 1


class accounts:
    __username = ""
    __balance = 0
    __password = ""

    def __init__(self, username, password):

        self.__username = username
        self.__password = password

    def setuser(self, username):
        self.__username = username

    def getuser(self):
        return self.__username

    def set_passowrd(self, password):
        self.__password = password

    def get_password(self):
        return self.__password

    def withdraw(self, amount):
        if(amount >= 0):
            self.__balance -= amount
            print("Action completed, withdrawn %s $ " % (amount))
        else:
            print("Please enter a number which is less than 0 ")

    def deposit(self, amount):
        if (amount >= 0):
            self.__balance += amount
            print("Action completed, depoisted %s $ " % (amount))
        else:
            print("Please enter a number greater than 0 ")

    def get_balance(self):
        print("Balance is : %s" % (self.__balance))

    def get_info(self):
        print("User name is: {} \n Password is : {} \n Balance is : {} $" .format(
            self.__username, self.__password, self.__balance))


index_confirmed = 0


def create_user(name, password, index_number):
    user_list.insert(int(index_number), name)
    password_list.insert(int(index_number), password)
    info_list.insert(int(index_number), accounts(
        user_list[int(index_number)], password_list[int(index_number)]))
    info_list[int(index_number)].get_info()
    print(" Index number: %s" % (index_number))


def login(name, password, index):
    global verify
    global index_confirmed
    if(name == user_list[int(index)] and password == password_list[int(index)]):
        print("You have logged in!")
        verify = "Q"
        index_confirmed = int(index)
    else:
        print("You have failed to log in")


def default():
    global answer
    while((answer != "Q") and (verify != "Q")):
        answer = input(
            "To create an account type C. to login into an account type L. To leave type Q ")
        if(answer == "C"):
            name = input("Enter name ")
            password = input("Enter password ")
            index = input(
                "Enter an index number. Dont forget it! only a number! ")
            create_user(name, password, index)
        if(answer == "L"):
            login(input("Enter name "), input("Enter password "),
                  input("Enter index number "))


def info():
    info_list[index_confirmed].get_info()


def withdraw():
    amount = int(input("how much would you like to withdraw? "))
    info_list[index_confirmed].withdraw(amount)


def deposit():
    amount = int(input("How much would you like to deposit? "))
    info_list[index_confirmed].deposit(amount)


def info_balance():
    info_list[index_confirmed].get_balance()


def transfer(index, amount):
    info_list[int(index_confirmed)].withdraw(amount)
    info_list[index].deposit(amount)


def functions():
    global answer
    global verify
    while(answer != "Q"):
        answer = input(
            "Choose action: \n \"withdraw\" \"deposit\" \"balance info\" \"quit\" \"transfer\" \"overall info\" \"log out\" ")
        if(answer == "withdraw"):
            withdraw()

        if(answer == "deposit"):
            deposit()

        if(answer == "log out"):
            verify = ""
            break

        if(answer == "quit"):
            print("Good bye!")
            break

        if(answer == "balance info"):
            info_balance()

        if (answer == "transfer"):
            transfer(int(input("Enter your friends index ")),
                     int(input("Enter amount ")))

        if(answer == "overall info"):
            info()


check = "Y"
while(check != "N"):
    default()
    functions()
    check = input(
        "Would you like to keep using the program? If so type [Y] else type [N] ")
