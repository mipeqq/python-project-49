#!/usr/bin/env python 3
from brain_games.cli import welcome_user


def main():
    print('Welcome to the Brain Games!')
    name = welcome_user()


if __name__ == '__main__':
    main()
