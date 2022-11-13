import os
from dataclasses import dataclass
from typing_extensions import TypeAlias
from typing import List, Tuple, Optional


Coord: TypeAlias = Tuple[float, float]


@dataclass
class Driver:
    id: int
    name: str
    input: bool
    pos: Coord


@dataclass
class Pin:
    id: int
    name: str
    pos: Coord


@dataclass
class Path:
    id: int
    pins: List[Pin]
    dri_in: Optional[Driver]
    dri_out: Optional[Driver]


def sort_pins_x(pins: List[Pin]) -> List[Pin]:
    """ Returns a list of pins sorted by the x coordenates."""
    S = sorted(pins, key=lambda Pin: Pin.pos[0])
    return S


def sort_pins_y(pins: List[Pin]) -> List[Pin]:
    """ Returns a list of pins sorted by the y coordenates."""
    S = sorted(pins, key=lambda Pin: Pin.pos[1])
    return S


def sort_drivers_y(drivers: List[Driver]) -> List[Driver]:
    """ Returns a list of drivers sorted by the y coordenates."""
    S = sorted(drivers, key=lambda Driver: Driver.pos[1])
    return S


def write_connection(v1: str, v2: str, filename: str) -> None:
    """Writes each connection of a path in the especified format."""
    filename.write("- BOGUS NET NAME \n")
    filename.write("  ( " + v1 + " conn_in ) \n")
    filename.write("  ( " + v2 + " conn_out )\n")
    filename.write("; \n")


def write_output(paths: List[Path], file_name: str) -> None:
    """Writes the output net connections as the especified format in a .def file."""
    with open(file_name, "w") as out_file:
        for path in paths:
            write_connection(path.dri_in.name, path.pins[0].name, out_file)
            n = len(path.pins)
            for i in range(n-1):
                write_connection(path.pins[i].name, path.pins[i+1].name, out_file)
            write_connection(path.pins[-1].name, path.dri_out.name, out_file)


def read_input(file_name: str, path_name: str = './') -> Tuple[List[Driver], List[Pin]]:
    """Reads the drivers and prins from a .def file. Returns a tuple with the list of
    all the drivers and the list of all the pins. Each Driver and Pin with it's respective
    atributes."""

    id_pin: int = 0
    id_driver: int = 0
    pins: List[Pin] = []
    drivers: List[Driver] = []

    with open(os.path.join(path_name, file_name)) as file:
        for _, line in enumerate(file):
            line_str = line.split()
            if len(line_str) and line_str[0] == '-':  # driver line
                driver = Driver(id_driver, line_str[1], bool(
                    line_str[7] == 'INPUT'), [0, 0])
                drivers.append(driver)
            elif len(line_str) > 1 and line_str[1] == 'FIX':  # driver coordinates
                drivers[id_driver].pos = tuple(
                    [float(line_str[3]), float(line_str[4])])
                id_driver += 1
            elif len(line_str) > 1 and line_str[-1] == 'N;':  # pin line
                pin = Pin(id_pin, line_str[0], tuple(
                    [float(line_str[5]), float(line_str[6])]))
                pins.append(pin)
                id_pin += 1

    return drivers, pins
