import csv
from random import randint
from timeit import default_timer as timer
from multiprocessing import Process
# Import funkcji sortujących z pliku wcześniej napisanego
from Sortowania import *


def writeMeasurments(measurements, filename='measurments.csv'):
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f, delimiter='\t')
        writer.writerows(measurements)


def measure(function, arr):
    arr_cpy = arr.copy()
    start = timer()
    function(0, len(arr_cpy) - 1,arr_cpy)
    end = timer()
    return "%.8f" % (end - start)


def measureSingle(function, breakpoints):
    measurments = []

    for breakpoint in breakpoints:
        original = [randint(1, breakpoint) for x in range(breakpoint)]
        print("Measuring brakpoint %s for function %s" %
              (breakpoint, function.__name__))
        measurments.append(measure(function, original))

    measurments.insert(0, "time")
    breakpoints.insert(0, "num")
    writeMeasurments(zip(breakpoints, measurments), "%s.csv" % function.__name__)


def measureMultiple(functions, breakpoints):
    processes = []

    for function in functions:
        print("Measuring function %s ..." % function.__name__)
        p = Process(target=measureSingle, args=(function, breakpoints))
        processes.append(p)
        p.start()

    for process in processes:
        process.join()


if __name__ == "__main__":
    measureMultiple([szybkie], [100, 500, 1000, 5000, 10000, 20000, 30000, 50000, 75000, 100000])