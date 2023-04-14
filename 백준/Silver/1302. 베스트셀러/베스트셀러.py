books = {}

for _ in range(int(input())):
    book = input()
    if books.get(book) is None:
        books[book] = 1
    else:
        books[book] += 1

print(sorted(books.items(), key=lambda x: (-x[1], x[0]))[0][0])
