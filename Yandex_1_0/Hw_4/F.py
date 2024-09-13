def get_buyers_list(operations):
    buyers = {}
    for operation in operations:
        name, product, count = operation.split()
        buyers[name] = buyers.get(name, {})
        buyers[name][product] = buyers[name].get(product, 0) + int(count)
    for buyer in sorted(buyers.keys()):
        print(f"{buyer}:")
        for product, count in sorted(buyers[buyer].items()):
            print(f"{product} {count}")


with open('input.txt', 'r') as file:
    operations = [line for line in file.readlines()]
    get_buyers_list(operations)