import argparse
from time import sleep
from collections import OrderedDict
from serial.tools.list_ports import comports
from v1_protocol import V1Protocol
from v2_protocol import V2Protocol
from v3_protocol import V3Protocol
from PIL import Image

protocols = {i.version: i for i in [ V1Protocol, V2Protocol, V3Protocol ] }

versions = tuple(protocols.keys())

def create(port, protocol_version="v3"):
    try:
        prot = protocols[protocol_version](port) # TODO check parameters
    except KeyError:
        raise ValueError("Unsupported protocol")
    return prot


def port_and_protocol_args(parser):
    """
    Adds arguments every command has.
    """
    parser.add_argument('port', type=str, default=None, help='Port')
    parser.add_argument('protocol', type=str, choices=versions,
                                default=versions[-1], help='Protocol version',)

def create_argument_parser():
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(
            title="Commands",
            description="Valid commands for the engraver",
            dest="command"
            )

    version = sub.add_parser("version", help="Show version information")

    available = sub.add_parser("available", help="Show available ports")

    home = sub.add_parser("home", help="Move engraver to home")
    port_and_protocol_args(home)

    start = sub.add_parser("start",
                           help="Start engraving with burn time [Default 60]")
    port_and_protocol_args(start)
    start.add_argument('burn_time', type=int, default=60, help='Burn time')

    pause = sub.add_parser("pause", help="Pause engraver")
    port_and_protocol_args(pause)

    reset = sub.add_parser("reset", help="Reset engraver")
    port_and_protocol_args(reset)

    upload = sub.add_parser("upload", help="Upload image to engraver")
    port_and_protocol_args(upload)
    upload.add_argument('image', default=None, help='Image')
    return parser



# Tools
def version():
    print("v0.0.1") # TODO: Unhardcode this
def available():
    """
    NOTE:
    Support is limited to a number of operating systems. On some systems
    description and hardware ID will not be available (None).
    """
    for i in comports():
        print(i)
        # Use this to print nicely
        # https://pythonhosted.org/pyserial/tools.html#serial.tools.list_ports.ListPortInfo

tools = {
    "available": available,
    "version":   version
}

# Commands
def home(engraver):
    engraver.home()
def start(engraver, burn_time=60):
    engraver.start(burn_time)
def pause(engraver):
    engraver.pause()
def reset(engraver):
    engraver.reset()
def upload(engraver, image=None):
    msecs = engraver.erase()
    engraver.await_tx(msecs)

    # NOTE: Wait ten times what the erase needed: empirically tested.
    # if we don't wait the resulting image is a square full of ones.
    sleep(float(msecs)/1000 * 10)

    engraver.upload_image(Image.open(image))


commands = {
    "home": home,
    "start": start,
    "pause": pause,
    "reset": reset,
    "upload": upload
}

# https://github.com/camrein/EzGraver/issues/43
if __name__ == "__main__":
    args = vars(create_argument_parser().parse_args())

    command = args["command"]


    if command in commands.keys():
        engraver = create(args["port"], protocol_version=args["protocol"])
        del args["command"]
        del args["port"]
        del args["protocol"]
        commands[command](engraver, **args)
    elif command in tools.keys():
        tools[command]()
    else:
        ValueError("Unknown command")
