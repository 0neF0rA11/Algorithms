def deposit(name, amount):
    bank[name] = bank.get(name, 0) + amount


def withdraw(name, amount):
    bank[name] = bank.get(name, 0) - amount


def balance(name):
    print(bank.get(name, 'ERROR'))


def transfer(name_1, name_2, amount):
    bank[name_1] = bank.get(name_1, 0) - amount
    bank[name_2] = bank.get(name_2, 0) + amount


def income(percent):
    for name, amount in bank.items():
        if amount > 0:
            bank[name] += amount * percent // 100


def process_operations(file_path):
    with open(file_path, 'rt', encoding='utf-8') as db:
        for line in db.readlines():
            operation, *other = line.split()
            if operation == 'DEPOSIT':
                deposit(other[0], int(other[1]))
            elif operation == 'WITHDRAW':
                withdraw(other[0], int(other[1]))
            elif operation == 'BALANCE':
                balance(other[0])
            elif operation == 'TRANSFER':
                transfer(other[0], other[1], int(other[2]))
            elif operation == 'INCOME':
                income(int(other[0]))


bank = {}
process_operations('input.txt')
