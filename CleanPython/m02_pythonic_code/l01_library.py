class MagicLibrary:
    def __init__(self, books):
        """
        Construct a library based on a collection of books.

        Params
        ---
        book : str array
            Array of books to consider
        """
        self.books = books
        self._index = 0
        self.is_open = False

    def __enter__(self):
        """
        Method to be used when entering the 'with' statement.

        Returns
        ---
        self : MagicLibrary
            Returns the library accessed
        """
        print("The library is now open.")
        self.is_open = True
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """
        Method to be used when exiting the 'with' statement.

        Params
        ---
        exc_type : Exception Type
            Exception type received

        exc_value : Exception Value
            Exception value received

        traceback : String
            Traceback related with the exception.
        """
        print("\nThe library is now closed.")
        self.is_open = False
        self._index = 0

    def __getitem__(self, index):
        """
        Access the item on the index passed

        Params
        ---
        index : Int
            Index to access

        Returns
        ---
        Book at the given index
        """
        return self.books[index]

    def __len__(self):
        """
        Obtain the length (size) in the library.

        Returns
        ---
        Integer that reflects the quantity of books.
        """
        return len(self.books)

    def __iter__(self):
        """
        Iterator implementation that resets the private index position

        Returns
        ---
        Self element and update of index
        """
        self._index = 0
        return self

    def __next__(self):
        """
        Implement the next object of a iteration loop.

        Returns
        ---
        Book at the next element based on the private index
        """
        if self._index >= len(self.books):
            raise StopIteration
        book = self.books[self._index]
        self._index += 1
        return book

    def __getattr__(self, name):
        """
        To obtain info of the attributes on the categories of fantasy, science
        or history

        Params
        ---
        name : String
            Category of interest

        Returns
        ---
        All the books in the given category

        Raise
        ---
        AttributeError if not category is found
        """
        if name in ["fantasy", "science", "history"]:
            return [b for b in self.books if name in b.lower()]
        raise AttributeError(f"No category named '{name}'")


    def __call__(self, keyword):
        """
        Call method that will search for the given keyword

        Params
        ---
        keyword : String
            Pattern of interest to search

        Returns
            Books that matched pattern of interest
        """
        return [b for b in self.books if keyword.lower() in b.lower()]


def main():
    books = [
        "A Brief History of Time",
        "The Science of Interstellar",
        "Minecraft Fantasy",
        "C++ Science",
        "Python History"
    ]

    with MagicLibrary(books) as library:
        print(f"\nTotal books: {len(library)}")

        print("\nOne book by index:", library[2])

        print("\nIterating through the library:")
        for b in library:
            print("  -", b)

        print("\nBooks in 'fantasy' category:", library.fantasy)

        print("\nSearch for 'python':", library("python"))

if __name__ == "__main__":
    main()

