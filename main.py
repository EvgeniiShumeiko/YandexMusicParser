import sys
import argparse
import config
import modules.ymparser as ymparser


def argument_parser():
    """
    Парсер входных аргументов
    :return: Arguments
    """

    parser = argparse.ArgumentParser()

    parser.add_argument('-a', '--artists', action="store_true", help="Парсинг списка артистов", default=False)
    parser.add_argument('-i', '--info', action="store_true", help="Парсинг информации об артистах", default=False)
    parser.add_argument('-v', '--version', action='store_true', help="Вывод весии скрипта", default=False)

    return parser.parse_args()


def main():
    args = argument_parser()

    if args.version:
        print(config.version)
        sys.exit()

    if args.info:
        ymparser.parse_info()

    if args.artists:
        ymparser.parse_artists()


if __name__ == "__main__":
    main()
