from command_reader import CommandReader
import serial
import sys

args = sys.argv


class SerialIo(CommandReader):
    def __init__(self, port, timeout, indicator="next command: ") -> None:
        super().__init__(indicator)
        self.port = port
        self.timeout = timeout
        s = None

    def before(self) -> None:
        self.s = serial.Serial(port=self.port, timeout=self.timeout)

    def after(self) -> None:
        self.s.close()

    def handle(self):
        raw = bytes.fromhex(self.cmd)
        self.s.write(raw)
        print(self.s.readall().hex(' '))


timeout = 0.2
if len(args) >= 3:
    timeout = args[2]
si = SerialIo(args[1], timeout)

si.run()
