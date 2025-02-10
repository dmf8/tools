class CommandReader:
    def __init__(self, indicator="next command: ") -> None:
        self.cmd = ""
        self.indicator = indicator

    def before(self) -> None:
        pass

    def after(self) -> None:
        pass

    def run(self) -> None:
        self.before()
        while True:
            self.cmd = input(self.indicator)
            if "exit" == self.cmd or "q" == self.cmd:
                break
            else:
                self.handle()
        self.after()

    def handle(self):
        print(self.cmd)


# cr = CommandReader("abc: ")
# cr.run()
