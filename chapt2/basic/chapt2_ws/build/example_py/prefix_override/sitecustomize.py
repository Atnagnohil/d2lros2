import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/andinm/d2lros2/chapt2/basic/chapt2_ws/install/example_py'
