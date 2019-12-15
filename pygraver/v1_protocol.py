from base_protocol import BaseProtocol

class V1Protocol(BaseProtocol):

    version = "v1"

    def up(self):
        self._transmit(b"\xF5")

    def down(self):
        self._transmit(b"\xF6")

    def left(self):
        self._transmit(b"\xF7")

    def right(self):
        self._transmit(b"\xF8")
