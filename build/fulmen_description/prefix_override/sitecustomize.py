import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/leonardo-augusto-antunes/fulmen_ws/install/fulmen_description'
