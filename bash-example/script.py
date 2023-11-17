import os
import requests
from time import sleep


def main():
    print(os.environ["NAME"])

    while True:
        print(requests.get("https://google.com").status_code)
        sleep(5)


if __name__ == "__main__":
    main()
