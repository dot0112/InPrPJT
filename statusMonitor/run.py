from monitor import monitor
import sys
import re

addrPattern = r"^(\d{1,3}\.){3}\d{1,3}:\d{1,5}$"


def main():
    if len(sys.argv) < 2:
        print("empth address")
    else:
        addr = sys.argv[1]

        if re.match(addrPattern, addr):
            monitor(addr)
        else:
            print("incorrect address type")


if __name__ == "__main__":
    main()
