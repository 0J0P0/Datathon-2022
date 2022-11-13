# Datathon-2022

## Introduction
We are four second-year students studying _Data Science and Engineering_ in UPC.
We have chosen the [Qualcomm challenge](https://github.com/data-students/datathonfme2022/tree/main/qualcomm_challenge) of the Datathon.

From our point of view, we are trying to:
- Create a chip, in which we have to deliver the power to all the pins in the fastest way possible (minimize the time).
- Find paths of pins that, ideally have a similar lenght, thus we try to minimize the standard desviation of the pins in the path.


## Description of the algorithm
The algorithm which we have build consists in the following steps:
- Then we call the `gen` function
    ```python3
    def gen(lpin: List[Pin], ldri: List[Driver]) -> List[Path]:
    ```
   that it is the main function in our algorithm. Fisrt of all, we sort drivers by y-axis and pins by x-axis.
   
   This function is composed by 3 parts:
  - Function 
    ```python3
    def gen_base(lpath: List[Path], lpins: List[Pin], ldri: List[Driver]) -> None:
    ```
    this function join each driver (does not matter if is an input or output driver) with the first pin (we sort the pins by y-axis). 
    As we have the pins sorted by y-axis and the drivers too we join the lower driver with the lower pin
  - Function 
    ```python3
    def gen_bloc(lpath: List[Path], lpin: List[Pin]) -> None:
    ```
    we join the following pins, manteining this criterion doing it by groups until we arrive at the last pin, since we can find
    a lenght of pins lower than the the lenght of the groups. So we have cretaed a function to treat this case.
  - Function
    ```python3
    def gen_fin(lpath: List[Path], lpin: List[Pin]) -> None:
    ```
    Finally, as we hace the residual pins sorted by the y-axis, we only join the first "last pint" with the residual pins.
- Finally, we have to join each path of pins with their drivers, so as at the beginning we have selected all the drivers, we did not know which drivers were
input drivers or output dirvers, so now we have to prove if we are joining an input driver with an output driver.
