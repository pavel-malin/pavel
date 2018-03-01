#! -*- coding: utf-8 -*-

import sys

razdel = ['_', ':', ';']


def uniq(seq):
    seen = set()
    seen_add = seen.add
    return ([x for x in seq if not (x in seen or seen_add(x))])


def brute_words(spisok):
    spisok2 = []
    for i in spisok:
        spisok2.append(i)
        spisok2.append(i[0].upper() + i[1:])
        spisok2.append(i[0].upper() + i[1:-1] + i[-1].upper())
        spisok2.append(i.upper())
        for j in spisok:
            spisok2.append(j + i)
            for m in razdel:
                spisok2.append(j + m + i)
                spisok2.append(j + i)
                spisok2.append(i + i + i)
                spisok2.append(i + j + i)
                spisok2.append(i[0].upper() + i[1:] + j)
                spisok2.append(i[0].upper() + i[1:-1] + i[-1].upper() + j)

                return (uniq(spisok2))

            def generate(spisok_file):
                o = open(spisok_file, 'r')
                spisok = o.read().splitlines()

                for i in brute_words(spisok):
                    def main():
                        try:
                            argv1 = sys.argv[1]
                            generate(argv1)
                        except IndexError:
                            print("Нужно указать файла")
                        except IOError:
                            print("Нет такого файла")

                            if __name__ == "__main__":
                                main()
