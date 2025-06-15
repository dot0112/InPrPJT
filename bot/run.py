from app import create_app
import sys

test = False

if len(sys.argv) > 1:
    if sys.argv[1].lower() in ["true", "t"]:
        test = True

app = create_app(test)

if __name__ == "__main__":
    None
