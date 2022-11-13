from paint import *
from algorisme import *
from read_write import *
# from algorisme2 import *
# from algorisme4 import *


def main():
    ldri, lpin = read_input('inputs.def')
    lpath = gen(lpin, ldri)

    ntest: int = 0
    for test in ['testcase0.def', 'testcase1.def', 'testcase2.def', 'testcase3.def', 'testcase4.def']:
        ldri, lpin = read_input(test, './testCases/')
        paths = gen(lpin, ldri)
        write_output(paths, './solCases/output' + str(ntest) + '.def')
        ntest += 1
        add_nodes_and_edges(paths)
        paint_nodes_and_show('./solCases/output_img' + str(ntest) + '.png')
        print('si', ntest)


if __name__ == '__main__':
    main()