from paint import *
from algorisme import *
from read_write import *
# from algorisme2 import *
# from algorisme4 import *


def main():
    ldri, lpin = read_input('inputs.def')
    lpath = gen(sort_pins_x(lpin), ldri)
    
    npins = 0
    for path in lpath:
        npins += len(path.pins)
    print('Numero total de pins', npins, len(lpin))

    ntest: int = 0
    for test in ['testcase0.def', 'testcase1.def', 'testcase2.def', 'testcase3.def', 'testcase4.def']:
        ldri, lpin = read_input(test, './testCases/')
        paths = gen(lpin, ldri)
        write_output(paths, './solCases/output' + str(ntest) + '.def')
        ntest += 1
        #add_nodes_and_edges(paths)
        #paint_nodes_and_show()


if __name__ == '__main__':
    main()