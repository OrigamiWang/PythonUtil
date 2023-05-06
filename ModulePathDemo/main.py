import test1
import sys

# from test_module.test2 import test2
sys.path.append('test_module')
import test2

import pprint


def test_pprint():
    kudamono_dict = {'apple': {'juice': {1: 2, 3: 4, 5: 6},
                               'pie': {1: 3, 2: 4, 5: 7}},
                     'orange': {'cake': {3: 2, 5: 4, 6: 5},
                                'juice': {1: 5, 2: 3, 5: 6}},
                     'pear': {'cake': {1: 6, 6: 1, 7: 8},
                              'pie': {3: 5, 5: 3, 8: 7}}}
    pprint.pprint(kudamono_dict, width=30, indent=10)


if __name__ == '__main__':
    test_pprint()
# examine the system path you had added
# test1.test1()
# test2.test2()
