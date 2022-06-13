def main():
    run_timing()


def run_timing():
    number_of_runs = 0
    total_time = 0

    while True:
        one_run = input('Enter 10 km run time (<enter> to quit): ').strip()
        if not one_run:
            break
        number_of_runs += 1
        total_time += float(one_run)

    average_time = total_time / number_of_runs
    print(f'The average 10 km run time is {average_time:.2f}.')


if __name__ == '__main__':
    main()
