from model import *

# Modulo que contiene los visitors creados y cada uno computa una metrica

# Visitador que cuenta la cantidad de nodos de tipo NumberNode que existen en el arbol
class NumberCounter(Visitor):
    def __init__(self):
        self.counter = 0

    def visit_Number(self, node):
        self.counter = self.counter + 1

    def total(self):
        return self.counter


# Visitador que cuenta la cantidad de nodos de tipo AdditionNode que existen en el arbol
class AdditionCounter(Visitor):
    def __init__(self):
        self.counter = 0

    # Los nodos compuestos deben propagar la visita
    def visit_Addition(self, node):
        node.leftNode.accept(self)
        node.rightNode.accept(self)
        self.counter = self.counter + 1

    def total(self):
        return self.counter


##########################################################################
class UnaryOperatorCounter(Visitor):
    def __init__(self):
        self.count = 0

    def total(self):
        return self.count

    def visit_PlusPlus(self, node):
        self.count = self.count + 1
        super().visit_PlusPlus(node)

    def visit_MinusMinus(self, node):
        self.count = self.count + 1
        super().visit_MinusMinus(node)
##########################################################################

class ModuloOperatorCounter(Visitor):
    def __init__(self):
        self.count = 0

    def total(self):
        return self.count

    def visit_Addition(self, node):
        self.count = self.count + 1
        node.leftNode.accept(self)
        node.rightNode.accept(self)

    def visit_Subtract(self, node):
        self.count = self.count + 1
        node.leftNode.accept(self)
        node.rightNode.accept(self)
##########################################################################