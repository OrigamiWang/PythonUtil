import test1
import sys
# from test_module.test2 import test2
sys.path.append('test_module')
import test2

import pprint

if __name__ == '__main__':
    # examine the system path you had added
    pprint.pprint(sys.path)
    test1.test1()
    test2.test2()