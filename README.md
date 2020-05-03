# PyGraver

[EzGraver](https://github.com/camrein/EzGraver) migration to python using
`pyserial` and `pillow`.

![Picture of the owner of the METERK I used for the tests](homage.jpg)

## Running

Use the command line to ask the program. It uses `argparse` and has an easy to
read help. Or read the examples below.

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

### Usage example

``` bash
$ python pygraver available                         # Get available ports
/dev/ttyUSB0
$ python pygraver upload /dev/ttyUSB0 v3 image.png  # Upload image
$ python pygraver start /dev/ttyUSB0 v3 50          # 50 is ok for balsa wood
```

### Image preparation

Images don't need to have an specific format, `upload` command is able to
convert from most common formats (`jpg`, `png`...).

Images are converted to black and white. The **white** part is going to be
burned by the engraver. Make sure you got that correctly.

### Recommended burning times

These burning times have been tested successfully:

| Material   | Burning time (ms) |
|------------|------------------:|
| Balsa wood |                50 |
| Cardboard  |                25 |


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

