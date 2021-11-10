import traceback

import sys

try:
    print(1/0)
except Exception as e:
    traceback.print_exc()
    print(e)

