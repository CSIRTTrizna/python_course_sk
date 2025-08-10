

class Book:
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year

    # TODO __repr__ alebo __str__ tak, aby sa kniha zobrazila


class Library:
    def __init__(self):
        self.books: list = []

    def add_book(self, book: Book) -> None:
        self.books.append(book)

    def list_books(self) -> list:
        return self.books

    def find_books_by_author(self, author: str) -> list:
        # TODO: vratit zoznam knih podla mena autora
        return []

    def find_books_after_year(self, year: int) -> list:
        # TODO: vratit knihy vydane po zadanom roku
        return []

    def sort_books(self, key: str = "title", reverse: bool = False) -> list:
        # TODO: zoradit knihy podla kriteria: "title", "author" alebo "year"
        # BONUS ULOHA -> na riesenie sa da pouzit sorted(self.books, key=lambda x: x.title)
        return self.books

    def newest_book(self) -> Book:
        # TODO: vratit najnovsiu knihu (alebo None ak prazdny katalog)
        return None


def generate_library() -> Library:
    lib = Library()
    for author in range(3):
        for year in range(2019, 2026):
            lib.add_book(Book("Kniha", f"author{author}", year))
    return lib


def sample_menu():
    lib = generate_library()

    while True:
        print("\nKniznica - vyber akciu:")
        print("1) Pridat knihu")
        print("2) Zobrazit vsetky knihy")
        print("3) Vyhladavat podla autora")
        print("4) Vyhladavat podla roku")
        print("5) Zoradit knihy")
        print("6) Zobrazit najnovsiu knihu")
        print("0) Koniec")

        choice = input("Volba: ").strip()
        if choice == "1":
            title = input("Nazov: ")
            author = input("Autor: ")
            year = int(input("Rok vydania: "))
            # TODO: vytvorit Book a pridat do lib
        elif choice == "2":
            # TODO: ziskat list_books a vypisat ich
            pass
        elif choice == "3":
            autor = input("\tMeno autora: ")
            # TODO: vyhladanie podla autora a vypis
            pass
        elif choice == "4":
            rok = input("\tRok: ")
            # TODO: vyhladanie podla roku a vypis
            pass
        elif choice == "5":
            kriterium = input("\tKriterium: ")
            # TODO: zvolit kriterium a zavolat sort_books
            pass
        elif choice == "6":
            # TODO: zobrazit najnovsiu knihu
            pass
        elif choice == "0":
            break
        else:
            print("Neplatna volba.")


if __name__ == "__main__":
    sample_menu()
