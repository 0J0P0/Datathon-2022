# Datathon-2022

## Introduction
We are four second-year students studying _Data Science and Engineering_ in UPC.
We have chosen the [Qualcomm challenge](https://github.com/data-students/datathonfme2022/tree/main/qualcomm_challenge) of the Datathon.

From our point of view, we are trying to:

- Create a chip, in which we have to deliver the power to all the pins in the fastest way possible (minimize the time).

- Find paths of pins that, ideally have a similar lenght, thus we try to minimize the standard desviation of the pins in the path.


## Description of the algorithm

### Definition of Data Types

Our definition of a Driver, Pin and Path states as follows:
```python3
Coord: TypeAlias = Tuple[float, float]


@dataclass
class Driver:
    """Class definition of a Driver. Each driver has a unique id and a boolean variable
    specifing if it's an input or output Driver, along other attributes."""
    id: int
    name: str
    input: bool
    pos: Coord


@dataclass
class Pin:
    """Class definition of a Pin. Each driver has a unique id, along other attributes."""
    id: int
    name: str
    pos: Coord


@dataclass
class Path:
    """Class definition of a Path. A path consists of a list of Pins, the first one 
    connected with an input Driver (dri_in) and the last Pin connected with an output
    Driver (dri_out)."""
    id: int
    pins: List[Pin]
    dri_in: Optional[Driver]
    dri_out: Optional[Driver]
```

### Specification of the Algorithm

The algorithm which we have build consists in the following steps:
- The main function `gen`
    ```python3
    def gen(lpin: List[Pin], ldri: List[Driver]) -> List[Path]:
    ```
   Finds the optimal list of Path. Firstly sortering the list of Pin and the list of Path respect to the y coordinates in ascending order.

   Following with 3 steps to build the list of Path:
      
  - `gen_base` connnects the first 32 Pins with the Drivers, indicating if the Dirver is an input or output one. Using the next criteria: the lowest Driver is always connected to the lowest Pin.
    ```python3
    def gen_base(lpath: List[Path], lpins: List[Pin], ldri: List[Driver]) -> None:
    ```
  - For the rest of Pins, each set of the 32 closest Pins   `gen_bloc` conncets to the last Pin in each Path, based on the same criteria of the previous function.
    ```python3
    def gen_bloc(lpath: List[Path], lpin: List[Pin]) -> None:
    ```
    in each iteration the number of Pins in each Path increases by one unit, keeping more or less the same distance for each Path. 
  - When the number of Pins not connected to a Path is less than the number of Drivers, `gen_fin` is called.
    ```python3
    def gen_fin(lpath: List[Path], lpin: List[Pin]) -> None:
    ```
    Each residual Pin is connected to a Path in ascending order.
  
  - We end up with the same number of Paths as Drivers, so we need to connect a Path starting with a input Diver with a Path starting with a output Driver, using the `path_union` function.
    ```python3
    def path_union(paths: List[Path]) -> List[Path]:
    ```
