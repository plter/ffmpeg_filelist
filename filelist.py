import os
import sys


def main():
    if len(sys.argv) != 2:
        print("Usage: filelist /path/to/your/dirctory > filelist.txt")
        return
    for filename in os.listdir(sys.argv[1]):
        if filename.lower().endswith(".mp4"):
            print(f"file '{filename}'")


if __name__ == '__main__':
    main()
