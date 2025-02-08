class CommandReader:
    def __init__(self, indicator="next command: ") -> None:
        cmd = ""
        indicator = indicator

    def run(self) -> None:
        while True:
            self.cmd = input(self.indicator)
            if "exit" == self.cmd:
                break
            else:
                self.handle()

    def handle(self):
        print(self.cmd)
