for _ in range(int(input())):
    data = input().lower()
    print('Yes' if data == data[::-1] else 'No')
