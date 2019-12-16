# PyGraver

[EzGraver](https://github.com/camrein/EzGraver) migration to python using
`pyserial` and `pillow`.

## Status

Tested on NEJEv3 but there are some issues that must be solved before
considering it ready.

For B&W images it engraves just a black square.

- Test: B&W a checkerboard: **FAILED** Renders a black square
- Test: A red rectangle: **SUCCESS** Renders the greyscale image it's supposed
  to render.

Needs more debugging

## Development

Considering you have `pipenv` installed and you are located in the project
directory:

Install the dependencies with:

``` bash
pipenv install
```

Run with:

``` bash
pipenv run python pygraver [args]
```

Or activate a shell `pipenv shell` and run it with `python pygraver [args]`

## Command line options

Use the command line to ask the program. It uses `argparse` and has an easy to
read help.

``` bash
PyGraver (master)$ pipenv run python pygraver -h
usage: pygraver [-h] {version,available,home,start,pause,reset,upload} ...

optional arguments:
  -h, --help            show this help message and exit

Commands:
  Valid commands for the engraver

  {version,available,home,start,pause,reset,upload}
    version             Show version information
    available           Show available ports
    home                Move engraver to home
    start               Start engraving with burn time [Default 60]
    pause               Pause engraver
    reset               Reset engraver
    upload              Upload image to engraver
```
