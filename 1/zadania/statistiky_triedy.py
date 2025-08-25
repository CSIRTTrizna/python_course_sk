class Student:
    def __init__(self, name: str):
        self.name = name
        self.znamky = dict()

    def pridaj_znamku(self, predmet: str, znamka: int) -> None:
        self.znamky[predmet] = self.znamky.get(predmet, list()) + [znamka]

    # TODO __repr__ alebo __str__ aby sa student zobrazil v tvare: "Meno: X, Predmet1: <priemer znamok (sum(list)/len(list))>, ..."
    # TODO metodu na zobrazenie studenta a jeho vysledkov pre poskytnute predmety ako jeden riadok v tabulke


class Classroom:
    def __init__(self):
        self.students: list[Student] = []

    def add_student(self, student: Student) -> None:
        self.students.append(student)

    def list_students_results(self, predmety: list = None) -> None:
        # TODO: vypisat celu triedu a vysledky pre studentov pre dane predmety (v pripade ze predmet je None vypisat pre vsetky predmety)
        return None

    def list_students(self) -> list:
        return self.students

    def find_student(self, name: str) -> Student | None:
        # TODO: najst studenta podla mena (alebo vratit None)
        return None

    def average_grade(self, predmet: str) -> float:
        # TODO: vypocitat priemer vsetkych studentov pre dany predmet
        return 0.0

    def best_student(self, predmet: str) -> Student | None:
        # TODO: najst studenta s najlepsim priemerom pre daney predmet
        return None

    def worst_student(self, predmet: str) -> Student | None:
        # TODO: najst studenta s najhorsim priemerom pre daney predmet
        return None

    def sort_by_average(self, predmet: str, reverse: bool = True) -> list:
        # TODO: zoradit studentov podla priemeru znamok pre dany predmet (default: zostupne)
        return self.students


def generate_classroom() -> Classroom:
    trieda = Classroom()

    predmety = ["slovencina", "matematika", "fyzika", "informatika"]
    ziaci = ["Adam", "Boris", "Cyril", "Dana", "Eva"]

    znamka = 1

    for ziak in ziaci:
        student = Student(ziak)
        for predmet in predmety:
            for _ in range(3):
                student.pridaj_znamku(predmet, znamka)
                znamka %= 5
                znamka += 1

        trieda.add_student(student)
    return trieda


def sample_menu():
    trieda = generate_classroom()

    while True:
        print("\nŠtatistiky triedy - vyber akciu:")
        print("1) Pridať študenta")
        print("2) Zobraziť všetkých študentov")
        print("3) Vyhľadať študenta podľa mena")
        print("4) Vypočítať priemernú známku")
        print("5) Zobraziť najlepšieho študenta")
        print("6) Zobraziť najslabšieho študenta")
        print("7) Zoradiť študentov podľa priemernej známky")
        print("8) Zobraziť všetkých študentov a ich výsledky")
        print("0) Koniec")

        choice = input("Voľba: ").strip()
        if choice == "1":
            meno = input("Meno: ")
            predmet = input("Predmet: ")
            znamka = int(input("Znamka: "))
            # TODO: vytvoriť Studenta a pridať do triedy
        elif choice == "2":
            # TODO: vypísať všetkých študentov
            pass
        elif choice == "3":
            meno = input("\tMeno študenta: ")
            # TODO: vyhľadať a vypísať výsledok
            pass
        elif choice == "4":
            # TODO: zavolať average_grade a vypísať
            predmet = input("Predmet: ")
            pass
        elif choice == "5":
            # TODO: zavolať best_student a vypísať
            predmet = input("Predmet: ")
            pass
        elif choice == "6":
            # TODO: zavolať worst_student a vypísať
            predmet = input("Predmet: ")
            pass
        elif choice == "7":
            # TODO: zavolať sort_by_average a vypísať
            predmet = input("Predmet: ")
            pass
        elif choice == "8":
            # TODO: vypisat zoznam studentov a ich priemer pre pozadovane predmety -> ako tabulku - stlpce budu predmety a riadky ziaci
            predmety = []
            print("[i] Pre ukončenie zoznamu predmetov zadajte q")
            while True:
                predmet = input("Predmet:")
                if predmet == "q":
                    break
                predmety.append(predmet)
            pass
        elif choice == "0":
            break
        else:
            print("Neplatná voľba.")


if __name__ == "__main__":
    sample_menu()
