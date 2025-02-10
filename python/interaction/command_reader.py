class CommandReader:
    def __init__(self, indicator="next command: ") -> None:
        self.cmd = ""
        self.indicator = indicator

    def run(self) -> None:
        while True:
            self.cmd = input(self.indicator)
            if "exit" == self.cmd or "q" == self.cmd:
                break
            else:
                self.handle()

    def handle(self):
        print(self.cmd)


# cr = CommandReader("abc: ")
# cr.run()
