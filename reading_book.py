from class.read_file import Books


def main():
    books = []
    in_file = open('books.csv', 'r')
    for line in in_file.readlines():
        parts = line.strip().split(',')
        book_status = parts[-1] == "r"
        book = Books(parts[0], parts[1], int(parts[2]), book_status)
        books.append(book)
    in_file.close()

    for book in books:
        print(book)


main()
