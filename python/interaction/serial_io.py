from command_reader import CommandReader


class SerialIo(CommandReader):
    def handle(self):
        print(f"new {self.cmd}")

        pass


# si = SerialIo()
# si.run()

a = int("12")
# b = int("12")
h = hex(a)
print(a)
print(h)
