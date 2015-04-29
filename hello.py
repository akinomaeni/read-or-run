# -*- coding: utf-8 -*-
import sys
def hello():
    print("read or run")

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        if sys.argv[1] == "run":
            print("run")
        elif sys.argv[1] == "read":
            print("read")
        else:
            hello()
    else:
        hello()
