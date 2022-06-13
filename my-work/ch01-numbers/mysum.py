def main():
    #print(mysum(1, 2, 3, start=40))
    print(mysum([1, 2, 3], start=5))
    print(average(1, 2, 3, 6))


def mysum(numbers, start=0):
    output = 0 + start
    for num in numbers:
        output += num

    return output


def average(*numbers):
    total = 0
    for num in numbers:
        total += num

    return total / len(numbers)


if __name__ == '__main__':
    main()
