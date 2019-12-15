import argparse
from collections import OrderedDict
from serial.tools.list_ports import comports
from v1_protocol import V1Protocol
from v2_protocol import V2Protocol
from v3_protocol import V3Protocol

protocols = OrderedDict( (i.version, i) for i in [ V1Protocol,
                                                   V2Protocol,
                                                   V3Protocol ] )
versions = tuple(protocols.keys())

def create(port, protocol_version="v1"):
    try:
        prot = protocols[protocol_version](port) # TODO check parameters
    except KeyError:
        raise ValueError("Unsupported protocol")
    return prot


def port_and_protocol_args(parser):
    """
    Adds arguments every command has.
    """
    parser.add_argument('port', nargs=1, default=None, help='Port')
    parser.add_argument('protocol', nargs=1, choices=versions,
                                default=versions[0], help='Protocol version',)

def create_argument_parser():
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(
            title="Commands",
            description="Valid commands for the engraver",
            dest="command"
            )

    version = sub.add_parser("version", help="Show version information")
    port_and_protocol_args(version)

    available = sub.add_parser("available", help="Show available ports")
    port_and_protocol_args(available)

    home = sub.add_parser("home", help="Move engraver to home")
    port_and_protocol_args(home)

    start = sub.add_parser("start", help="Start engraving with burn time [Default 60]")
    port_and_protocol_args(start)
    start.add_argument('burn_time', nargs=1, default=60, help='Burn time')

    pause = sub.add_parser("pause", help="Pause engraver")
    port_and_protocol_args(pause)

    reset = sub.add_parser("reset", help="Reset engraver")
    port_and_protocol_args(reset)

    upload = sub.add_parser("upload", help="Upload image to engraver")
    port_and_protocol_args(upload)
    upload.add_argument('image', nargs=1, default=None, help='Image')
    return parser


def show_version():
    # TODO Print protocols
    pass
def show_available():
    """
    NOTE:
    Support is limited to a number of operating systems. On some systems
    description and hardware ID will not be available (None). 
    """
    # TODO print comports() nicely
    pass
def show_home():
    # TODO
    pass
def start(port=None, burn_time=60):
    # TODO
    pass
def pause(port=None):
    # TODO
    pass
def reset(port=None):
    # TODO
    pass
def upload(port=None, image=None):
    # TODO
    pass

commands = {
    "version": show_version,
    "available": show_available,
    "home": show_home,
    "start": start,
    "pause": pause,
    "reset": reset,
    "upload": upload
}

# https://github.com/camrein/EzGraver/issues/43
if __name__ == "__main__":
    args = vars(create_argument_parser().parse_args())
    command = args["command"]
    del args["command"]
    commands[command](args)
