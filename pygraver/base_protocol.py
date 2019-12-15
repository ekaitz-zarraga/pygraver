import serial
import PIL
from time import sleep

class BaseProtocol:
    image_width  = 512
    image_height = 512
    version      = None

    def __init__(port, baudrate=57600,
                       parity=serial.PARITY_NONE,
                       databits=serial.EIGHTBITS,
                       stopbits=serial.STOPBITS_ONE,
                       timeout=None):
        ser = serial.Serial()
        ser.baudrate = baud_rate
        ser.port     = port
        ser.parity   = parity
        ser.databits = databits
        ser.stopbits = stopbits
        ser.timeout  = timeout

        self._serial = ser

        ser.open()

    def __del__(self):
        if self._serial.is_open:
            self._serial.close()

    def __repr__(self):
        return self.version

    def start(self, burn_time):
        self._set_burn_time(burn_time)
        self._transmit(b"\xF1")

    def pause(self):
        self._transmit(b"\xF2")

    def reset(self):
        self._transmit(b"\xF9")

    def home(self):
        self._transmit(b"\xF3")

    def center(self):
        self._transmit(b"\xFB")

    def preview(self):
        self._transmit(b"\xF4")

    def erase(self):
        """
        Erases the EEPROM of the engraver. This is necessary before uploading
        any new image to it.
        Erasing the EEPROM takes a while. Sending image data to early causes
        that some of the leading pixels are lost. Waiting for about 5 seconds
        seems to be sufficient.
        Returns the recommended time in ms to wait until uploading the image.
        """
        _transmit(b"\xFE"*8);
        return 6000 # NOTE: I don't like this.

    def upload_image(self):
        # TODO
        raise NotImplementedError()

    def await_tx(self, msecs):
        sleep_time = 0.5 / 1000 # 0.5 msecs
        while msecs > 0:
            if self._serial.out_waiting() == 0:
                return 0
            sleep(sleep_time)
            msecs -= sleep_time
        return -1 # Timed out


    def _transmit(self, data, chunk_size=None):
        pass

    def _set_burn_time(self, burn_time):
        "Receives burn_time as an integer between 1 and 240"
        if burn_time < 0x01 or burn_time > 0xF0:
            raise ValueError("Burn time out of range: [1 (0x01), 240 (0xF0)]")
        _transmit(bytes(burn_time,)) # Converts to byte

    # Abstract functions
    def up(self):
        raise NotImplementedError()

    def down(self):
        raise NotImplementedError()

    def left(self):
        raise NotImplementedError()

    def right(self):
        raise NotImplementedError()

