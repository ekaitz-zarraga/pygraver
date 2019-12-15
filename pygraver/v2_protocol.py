from base_protocol import BaseProtocol

class V2Protocol(BaseProtocol):

    version = "v2"

    def up(self):
        self._transmit(b"\xF5\x01")

    def down(self):
        self._transmit(b"\xF5\x02")

    def left(self):
        self._transmit(b"\xF5\03")

    def right(self):
        self._transmit(b"\xF5\04")
