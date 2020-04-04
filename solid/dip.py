from abc import abstractmethod
from enum import Enum

"""Dependency Inversion Principle
        En el diseño orientado a objetos, el principio de inversión de dependencia es una forma específica de desacoplar
         módulos de software. Al seguir este principio, las relaciones de dependencia convencionales establecidas desde 
         los módulos de alto nivel de establecimiento de políticas a los módulos de dependencia de bajo nivel se 
         invierten, lo que hace que los módulos de alto nivel sean independientes de los detalles de implementación del 
         módulo de bajo nivel. El principio establece:
            
            1. Los módulos de alto nivel no deberían depender de los módulos de bajo nivel. Ambos deberían depender de 
            abstracciones (p.ej., interfaces).
            2. Las abstracciones no deberían depender de los detalles. Los detalles (implementaciones concretas) deben 
            depender de abstracciones."""

class Relationship(Enum):
    PARENT = 0
    CHILD = 1
    SIBLING = 2


class Person:
    def __init__(self, name):
        self.name = name


class RelationshipBrowser:
    @abstractmethod
    def find_all_children_of(self, name): pass


class Relationships(RelationshipBrowser):  # low-level
    relations = []

    def add_parent_and_child(self, parent, child):
        self.relations.append((parent, Relationship.PARENT, child))
        self.relations.append((child, Relationship.CHILD, parent))
            
    def find_all_children_of(self, name):
        for r in self.relations:
            if r[0].name == name and r[1] == Relationship.PARENT:
                yield r[2].name

    def find_all_parent_of(self, name):
        for r in self.relations:
            if r[0].name == name and r[1] == Relationship.CHILD:
                yield r[2].name


class Research:
    # dependency on a low-level module directly
    # bad because strongly dependent on e.g. storage type

    # def __init__(self, relationships):
    #     # high-level: find all of john's children
    #     relations = relationships.relations
    #     for r in relations:
    #         if r[0].name == 'John' and r[1] == Relationship.PARENT:
    #             print(f'John has a child called {r[2].name}.')

    def __init__(self, browser):
        for p in browser.find_all_children_of("John"):
            print(f'John has a child called {p}')


parent = Person('John')
child1 = Person('Chris')
child2 = Person('Matt')

# low-level module
relationships = Relationships()
relationships.add_parent_and_child(parent, child1)
relationships.add_parent_and_child(parent, child2)

Research(relationships)