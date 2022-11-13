from paint import *
from algorithm import *
from read_write import *


"""
Main modul. For each selected input file, finds the most optimal solution of paths, writes
the paths as the desired format in an output file and creates an image visualizing the path solutions.
"""


def main():
    ntest: int = 0
    for test in ['priv_testcase0.def', 'priv_testcase1.def', 'priv_testcase2.def', 'priv_testcase3.def']:
        ldri, lpin = read_input(test)
        paths = gen(lpin, ldri)
        write_output(paths, 'f_output' + str(ntest) + '.def')
        add_nodes_and_edges(paths)
        paint_nodes_and_show('f_pic' + str(ntest) + '.png')
        ntest += 1


if __name__ == '__main__':
    main()
