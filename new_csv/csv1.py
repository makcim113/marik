class Csv:

    def __init__(self):
        pass

    def open(self):
        with open("products.csv", "r") as f:
            for line in f:
                print('_' * 100)
                str1 = line.strip().split(',')
                print('|' + ''.join(str1) + '|')

file = Csv.open("products.csv")
