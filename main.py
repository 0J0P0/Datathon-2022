from paint import *
from algorisme import *
from read_write import *
# from algorisme2 import *
# from algorisme4 import *


def main():
    ntest: int = 0.
    for test in ['priv_testcase0.def', 'priv_testcase1.def', 'priv_testcase2.def', 'priv_testcase3.def']:
        ldri, lpin = read_input(test)
        paths = gen(lpin, ldri)
        write_output(paths, './output' + str(ntest) + '.def')
        ntest += 1
        # add_nodes_and_edges(paths)
        # paint_nodes_and_show()


if __name__ == '__main__':
    main()
