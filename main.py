#! /usr/bin/env python3

import day1, day2

def main():
    day1a = day1.part1.answer()
    print(f'day1 part1 = {day1a}')
    assert(day1a == 54239)

    day1b = day1.part2.answer()
    print(f'day1 part2 = {day1b}')
    assert(day1b == 55343)

    day2b = day2.part1.answer()
    print(f'day2 part1 = {day2b}')
    assert(day2b == 1853)


if __name__ == "__main__":
    main()