import csv
import itertools
from collections import Counter
import string

def convert_base(number, base):
    digits = string.digits + string.ascii_letters
    digitslist = []
    while number > 0:
        digitslist.append(digits[int(number % base)])
        number = int(number/base)
    digitslist.reverse()
    return ''.join(digitslist)

def allcombos(number_str):
    possibilities = [['',digit] for digit in number_str]
    list_of_digits = list(itertools.product(*possibilities))
    list_of_digits.pop(0)
    return [''.join(x) for x in list_of_digits]

def cancellations(base):
    maxparam = int('100000', base)
    numerlist = list(range(base, maxparam))
    denomlist = list(range(base, maxparam))
    #print(base)
    for x in numerlist:
        for y in denomlist:
            if y > x and x % base != 0 and y % base != 0:
                xbaselist = list(dict.fromkeys(allcombos(convert_base(x, base))))
                ybaselist = list(dict.fromkeys(allcombos(convert_base(y, base))))
                for i in xbaselist:
                    for j in ybaselist:
                        try:
                            if int(i, base)/int(j, base) == x/y:
                                xdigits = list(convert_base(x, base))
                                ydigits = list(convert_base(y, base))
                                idigits = list(i)
                                jdigits = list(j)
                                xdiff = list((Counter(xdigits) - Counter(idigits)).elements())
                                ydiff = list((Counter(ydigits) - Counter(jdigits)).elements())
                                xdiff.sort()
                                if Counter(xdiff) == Counter(ydiff) and len(xdiff) > 0:
                                    with open('More Cancellations' + '\\anomalouscancellationsinbase' + str(base) + '.csv', 'a', newline='') as csvFile:
                                        removedlist = str(xdiff)
                                        removedlist = removedlist.replace('\'', '')
                                        row = [convert_base(x, base), convert_base(y, base), str(i), str(j), removedlist]
                                        writer = csv.writer(csvFile)
                                        writer.writerow(row)
                                    csvFile.close()
                                    print('Remove ' + str(removedlist) + ': ' + convert_base(x, base) + '/' + convert_base(y, base) + ' equals ' + str(i) + '/' + str(j))
                        except ZeroDivisionError:
                            pass

if __name__ == "__main__":
    cancellations(7)