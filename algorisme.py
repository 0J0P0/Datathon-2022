import math
from read_write import *
from dataclasses import dataclass
from typing_extensions import TypeAlias
from typing import List, Tuple, Optional


def path_union(paths: List[Path]) -> List[Path]:
    """Unifies a path starting with an input Driver and a path starting with an output Driver.
    Returns the final list of paths and the total Manhattan distance."""

    in_paths: List[Path] = [path for path in paths if path.dri_in is not None]
    out_paths: List[Path] = [path for path in paths if path.dri_out is not None]

    unified_paths: List[Path] = []
    id: int = 0

    for i, j in zip(in_paths, out_paths):
        in_path = i.pins
        out_path = j.pins[::-1]
        up = Path(id, in_path + out_path, i.dri_in, j.dri_out)
        unified_paths.append(up)
        id += 1

    return unified_paths


def gen_fin(lpath: List[Path], lpin: List[Pin]) -> None:
    """Given a list of paths and a list of pins, adds the pins that minimizes the total
    distance to the lpaths.pins.
    Prec: len(lpath) == 32 and 0 < len(lpin) < 32
    """
    for i in range(len(lpin)):
        pin: Pin = lpin[i]
        lpath[i].pins.append(pin)


def gen_bloc(lpath: List[Path], lpin: List[Pin]) -> None:
    """Given a partial list of paths of size 32 and a list of pins of size 32
    sorted for the y-axis, adds one pin in each path of the lpath."""
    for i in range(0, 32):
        pin: Pin = lpin[i]
        path: Path = lpath[i]
        path.pins.append(pin)
        lpath[i] = path


def gen_base(lpath: List[Path], lpins: List[Pin], ldri: List[Driver]) -> None:
    """Given a null list of paths, a partial list of sorted pins (32 pins) resperct to the y-axis and a list
    of drivers, returns a list of partial paths (only the connection between one driver and the first pin)"""
    for i in range(0, 32):
        partial_lpin = [lpins[i]]
        dri_in = Optional[Driver]
        dri_out = Optional[Driver]
        dist: int = 0
        if ldri[i].input:
            dri_in = ldri[i]
            dri_out = None
        else:
            dri_in = None
            dri_out = ldri[i]
        path: Path = Path(i, partial_lpin, dri_in, dri_out)
        lpath.append(path)


def gen(lpin: List[Pin], ldri: List[Driver]) -> List[Path]:
    """Given a list of pins and list of drivers, returns a list of optimal paths."""
    slpin = sort_pins_x(lpin)
    sldri = sort_drivers_y(ldri)

    lpath: List[Path] = []
    assert(len(slpin) >= len(sldri))
    gen_base(lpath, sort_pins_y(slpin[0: 32]), sldri)

    for i in range(32, len(slpin), 32):
        gen_bloc(lpath, sort_pins_y(slpin[i: i+32]))

    j: int = len(slpin) % 32
    gen_fin(lpath, sort_pins_y(slpin[len(slpin)-j: len(slpin)]))
    return path_union(lpath)

