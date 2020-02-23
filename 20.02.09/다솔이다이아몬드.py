T = int(input())
for n in range(T):
    string = input()
    print('..#..' + '.#..' * int(len(string)-1))
    print('.#' * (len(string) * 2) + '.')
    for i in string:
        print(('#.' + i) + '.', end='')
    print('#')
    print('.#' * (len(string) * 2) + '.')
    print('..#..' + '.#..' * int(len(string)-1))