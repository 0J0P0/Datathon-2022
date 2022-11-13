from paint import *
from algorisme import *
from read_write import *


def main():
    ntest: int = 0
    for test in ['priv_testcase0.def', 'priv_testcase1.def', 'priv_testcase2.def', 'priv_testcase3.def']:
        ldri, lpin = read_input(test, './testCases/')
        paths = gen(lpin, ldri)
        write_output(paths, './solCases/output' + str(ntest) + '.0.def')
        add_nodes_and_edges(paths)
        paint_nodes_and_show('./solCases/output_img' + str(ntest) + '.png')
        ntest += 1


if __name__ == '__main__':
    main()