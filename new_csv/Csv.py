class New_csv:

    def __init__(self, fail_name, new_colun):
        self.fail_name = fail_name
        self.new_colun = new_colun
        self.lines = []

    def open(self, file):
        with open(file, 'r', encoding='utf-8') as f:
            f.read(file)

    def seve(self, file):
        self.add()
        with open(file, 'w', encoding='utf-8') as f:
            f.write(self.lines)
            f.close(file)

    def add(self):
        new_lin = input("Enter lines ,: ").strip().split(',')
        self.lines = new_lin

    def del_lines(self):
        pass

    def delete_column(self):
        pass

    def add_column(self):
        pass

    def print(self):
        pass

    def __str__(self):
        return f"{self.fail_name} {self.new_colun}"

