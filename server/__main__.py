import logging

from server import init_app

logging.basicConfig(level=logging.DEBUG)


def main():
    init_app().run(port=8080)


if __name__ == '__main__':
    main()
