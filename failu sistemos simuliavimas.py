import os


class FileSystemComponent:
    def __init__(self, name):
        self.name = name

    def display_info(self):
        raise NotImplementedError()

    def add(self, component):
        raise NotImplementedError()

    def remove(self, component):
        raise NotImplementedError()

    def search(self, name):
        raise NotImplementedError()


class File(FileSystemComponent):
    def display_info(self):
        print("Failas:", self.name)

    def add(self, component):
        print("Negalima pridėti prie failo.")

    def remove(self, component):
        print("Negalima pašalinti iš failo.")

    def search(self, name):
        if name == self.name:
            return self
        return None


class Directory(FileSystemComponent):
    def __init__(self, name):
        super().__init__(name)
        self.children = []

    def display_info(self):
        print("Katalogas:", self.name)

    def add(self, component):
        self.children.append(component)

    def remove(self, component):
        self.children.remove(component)

    def search(self, name):
        if name == self.name:
            return self

        for child in self.children:
            result = child.search(name)
            if result:
                return result

        return None


class FileSystemExplorer:
    def __init__(self):
        self.root = Directory("root")
        self.current_directory = self.root

    def display_current_directory(self):
        self.current_directory.display_info()

    def change_directory(self, name):
        if name == "..":
            if self.current_directory != self.root:
                self.current_directory = os.path.dirname(self.current_directory.name)
        else:
            result = self.current_directory.search(name)
            if isinstance(result, Directory):
                self.current_directory = result
            else:
                print("Katalogas nerastas.")

    def create_file(self, name):
        file = File(name)
        self.current_directory.add(file)

    def create_directory(self, name):
        directory = Directory(name)
        self.current_directory.add(directory)

    def delete(self, name):
        result = self.current_directory.search(name)
        if result:
            self.current_directory.remove(result)
            print(f"{name} ištrintas.")
        else:
            print(f"{name} nerastas.")

    def search(self, name):
        result = self.root.search(name)
        if result:
            print(f"{name} rastas.")
        else:
            print(f"{name} nerastas.")


# Pavyzdžio naudojimas
if __name__ == "__main__":
    explorer = FileSystemExplorer()

    while True:
        print("\n=== Failų Sistema ===")
        print("1. Rodyti esamą katalogą")
        print("2. Pakeisti katalogą")
        print("3. Sukurti failą")
        print("4. Sukurti katalogą")
        print("5. Ištrinti failą ar katalogą")
        print("6. Ieškoti failo ar katalogo")
        print("0. Išeiti")

        choice = input("Įveskite pasirinkimą: ")

        if choice == "1":
            explorer.display_current_directory()
        elif choice == "2":
            name = input("Įveskite katalogo pavadinimą: ")
            explorer.change_directory(name)
        elif choice == "3":
            name = input("Įveskite failo pavadinimą: ")
            explorer.create_file(name)
        elif choice == "4":
            name = input("Įveskite katalogo pavadinimą: ")
            explorer.create_directory(name)
        elif choice == "5":
            name = input("Įveskite failo ar katalogo pavadinimą: ")
            explorer.delete(name)
        elif choice == "6":
            name = input("Įveskite failo ar katalogo pavadinimą: ")
            explorer.search(name)
        elif choice == "0":
            break
        else:
            print("Neteisingas pasirinkimas.")