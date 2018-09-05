class Books:
    def __init__(self,title, author, pages, book_status):
        self.title = title
        self.author = author
        self.pages = pages
        self.book_status = book_status

    def __str__(self):
        return "{:54} by {:<20} {:>3} pages. Completed: {}".format(self.title, self.author, self.pages,
                                                                   self.book_status)

    def is_completed(self):
        return self.book_status == "r"
