class Computer:
    class CPU:
        def __init__(self, make: str):
            self.make: str = make

        def get_make(self):
            return self.make

    class OS:
        def __init__(self, name: str):
            self.name: str = name

        def get_name(self):
            return self.name

    name: str
    cpu: CPU
    os: OS

    def __init__(self, name: str, cpu: CPU, os: OS):
        self.name = name
        self.cpu = cpu
        self.os = os

    def __str__(self):
        return (f"computer -> {self.name}\n"
                f"cpu -> {self.cpu.get_make()}\n"
                f"os -> {self.os.get_name()}")


com = Computer("Lenovo", Computer.CPU("i5 intel"), Computer.OS("Ubuntu"))

print(com)
