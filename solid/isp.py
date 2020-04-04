from abc import abstractmethod

"""You aren't gonna need it"[1][2] (YAGNI)[3] is a principle of extreme programming (XP) 
that states a programmer should not add functionality until deemed necessary.[4] XP 
co-founder Ron Jeffries has written: "Always implement things when you actually need them, 
never when you just foresee that you need them."[5] Other forms of the phrase include 
"You aren't going to need it"[6][7] and "You ain't gonna need it".[8]"""

"""Interface Segregation Principle
        El principio de segregación de la interfaz (ISP, por sus siglas del inglés «Interface Segregation Principle») 
        establece que los clientes de un programa dado sólo deberían conocer de éste aquellos métodos que realmente 
        usan, y no aquellos que no necesitan usar."""

class Machine:
    def print(self, document):
        raise NotImplementedError()

    def fax(self, document):
        raise NotImplementedError()

    def scan(self, document):
        raise NotImplementedError()


# ok if you need a multifunction device
class MultiFunctionPrinter(Machine):
    def print(self, document):
        pass

    def fax(self, document):
        pass

    def scan(self, document):
        pass


class OldFashionedPrinter(Machine):
    def print(self, document):
        # ok - print stuff
        pass

    def fax(self, document):
        pass  # do-nothing

    def scan(self, document):
        """Not supported!"""
        raise NotImplementedError('Printer cannot scan!')


class Printer:
    @abstractmethod
    def print(self, document): pass


class Scanner:
    @abstractmethod
    def scan(self, document): pass


# same for Fax, etc.

class MyPrinter(Printer):
    def print(self, document):
        print(document)


class Photocopier(Printer, Scanner):
    def print(self, document):
        print(document)

    def scan(self, document):
        pass  # something meaningful


class MultiFunctionDevice(Printer, Scanner):  # , Fax, etc
    @abstractmethod
    def print(self, document):
        pass

    @abstractmethod
    def scan(self, document):
        pass


class MultiFunctionMachine(MultiFunctionDevice):
    def __init__(self, printer, scanner):
        self.printer = printer
        self.scanner = scanner

    def print(self, document):
        self.printer.print(document)

    def scan(self, document):
        self.scanner.scan(document)


printer = OldFashionedPrinter()
printer.fax(123)  # nothing happens
printer.scan(123)  # oops!