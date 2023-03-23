# Sintaxis concreta usada para escribir expresiones aritmeticas:
# <expr> = <num>
#        | (+ <expr> <expr>)
#        | (- <expr> <expr>)

class Node:
    # Formatea la expresion en un string
    def to_string(self):
        pass

    # Evalua la expresion
    def eval(self):
        pass

    # Acepta la visita de un visitor
    def accept(self, visitor):
        pass

    # Verifica si un nodo es igual a otro
    def __eq__(self, other):
        return self.__class__ == other.__class__


# Nodos literales normalmente son los valores primitivos (string, entero, boolean)
# En este caso solo consideramos un numero entero
class LiteralNode(Node):
    def __init__(self, val):
        self.value = val

    def to_string(self):
        pass

    def eval(self):
        return self.value

    def accept(self, visitor):
        visitor.visit_Literal(self)

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.value == other.value


# Numero
class NumberNode(LiteralNode):
	
    def accept(self, visitor):
        visitor.visit_Number(self)

    def to_string(self):
        return "" + str(self.value)


# Operadores
class OperatorNode(Node):
    def __init__(self, sym):
        self.symbol = sym

    def accept(self, visitor):
        visitor.visit_Operator(self)

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.symbol == other.symbol


# Operador binario
class BinaryOperatorNode(OperatorNode):
    def __init__(self, leftNode, rightNode, sym):
        super().__init__(sym)
        self.leftNode = leftNode
        self.rightNode = rightNode

    def to_string(self):
        return "(" + self.symbol + " " + self.leftNode.to_string() + " " + self.rightNode.to_string() + ")"

    def accept(self, visitor):
        visitor.visit_BinaryOperator(self)

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.leftNode == other.leftNode and self.symbol == other.symbol and self.rightNode == other.rightNode

########################################################################33
class ModuloNode(BinaryOperatorNode):
    def __init__(self, leftNode, rightNode):
        super().__init__(leftNode, rightNode, "%")

    def to_string(self):
        return "(" + self.symbol + " " + self.leftNode.to_string() + " " + self.rightNode.to_string() + ")"

    def accept(self, visitor):
        visitor.visit_Modulo(self)
    
    def eval(self):
        return self.leftNode.eval() % self.rightNode.eval()
    # def __eq__(self, other):
    #     return self.__class__ == other.__class__ and self.leftNode == other.leftNode and self.symbol == other.symbol and self.rightNode == other.rightNode
##########################################################################

# Operador suma
class AdditionNode(BinaryOperatorNode):
    def __init__(self, leftNode, rightNode):
        super(AdditionNode, self).__init__(leftNode, rightNode, "+")

    def eval(self):
        return self.leftNode.eval() + self.rightNode.eval()

    def accept(self, visitor):
        visitor.visit_Addition(self)


# Operador resta
class SubtractionNode(BinaryOperatorNode):
    def __init__(self, leftNode, rightNode):
        super(SubtractionNode, self).__init__(leftNode, rightNode, "-")

    def eval(self):
        return self.leftNode.eval() - self.rightNode.eval()

    def accept(self, visitor):
        visitor.visit_Subtract(self)


# Visitor
class Visitor:
    # Los nodos compuestos deben propagar la visita a los subnodos
    def visit_Addition(self, node):
        node.rightNode.accept(self)
        node.leftNode.accept(self)

    def visit_Subtract(self, node):
        node.rightNode.accept(self)
        node.leftNode.accept(self)

    def visit_Modulo(self, node):
        node.leftNode.accept(self)
        node.rightNode.accept(self)

    def visit_Number(self, node):
        pass

    def visit_MinusMinus(self, node):
        node.node.accept(self)

    def visit_PlusPlus(self, node):
        node.node.accept(self)

##########################################################################
class UnaryOperatorNode(OperatorNode):
    def __init__(self, node, sym):
        super().__init__(sym)
        self.node = node

    def to_string(self):
        return "(" + self.symbol + " " + self.node.to_string() + ")"

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.node == other.node and self.symbol == other.symbol

    def eval(self):
        pass
##########################################################################

##########################################################################
class PlusPlusNode(UnaryOperatorNode):
    def __init__(self, node):
        super().__init__(node, "++")

    # def to_string(self):
    #     return "(" + self.symbol + " " + self.node.to_string() + ")"

    def accept(self, visitor):
        visitor.visit_PlusPlus(self)

    def eval(self):
        return self.node.eval() + 1

    # def __eq__(self, other):
    #     return self.__class__ == other.__class__ and self.node == other.node and self.symbol == other.symbol
##########################################################################

##########################################################################
class MinusMinusNode(UnaryOperatorNode):
    def __init__(self, node):
        super().__init__(node, "--")

    # def to_string(self):
    #     return "(" + self.symbol + " " + self.node.to_string() + ")"

    def accept(self, visitor):
        visitor.visit_MinusMinus(self)

    # def __eq__(self, other):
    #     return self.__class__ == other.__class__ and self.node == other.node and self.symbol == other.symbol

    def eval(self):
        return self.node.eval()-1
##########################################################################
