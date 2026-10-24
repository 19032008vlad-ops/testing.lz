from function import task

list_test = [(3, 4, 7, 1, 7), (-0.1, 2, '12', 22, 2.9),(32, 'poiuytr', 9, -1, 4),(-14, -21, 98, 2, -2), (-1, -1, -1, 1, 2)]
def tests(testing):
    for i in testing:
       task(*i)


def main():
    tests(list_test)

if __name__ == '__main__':
    main()