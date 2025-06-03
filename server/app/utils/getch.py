import sys
import os


def flush_input():
    try:
        import msvcrt

        while msvcrt.kbhit():
            msvcrt.getch()
    except ImportError:
        import termios, fcntl

        fd = sys.stdin.fileno()
        oldterm = termios.tcgetattr(fd)
        newattr = termios.tcgetattr(fd)
        newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
        termios.tcsetattr(fd, termios.TCSANOW, newattr)
        oldflags = fcntl.fcntl(fd, fcntl.F_GETFL)
        fcntl.fcntl(fd, fcntl.F_SETFL, oldflags | os.O_NONBLOCK)
        try:
            while True:
                try:
                    c = sys.stdin.read(1)
                    if c == "":
                        break
                except IOError:
                    break
        finally:
            termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
            fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)


def getch(msg=""):
    flush_input()
    print(msg, end="", flush=True)

    if os.name == "nt":
        import msvcrt

        while True:
            key = msvcrt.getch()
            if key in (b"\x00", b"\xe0"):
                msvcrt.getch()
                continue
            try:
                flush_input()
                return key.decode()
            except UnicodeDecodeError:
                continue
    else:
        import tty
        import termios

        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            key = sys.stdin.read(1)
            if ord(key) in (0, 224):
                sys.stdin.read(1)
                return None
            flush_input()
            return key
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
