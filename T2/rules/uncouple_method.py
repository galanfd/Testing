from .rule import *

# Clases que permiten detectar si algun metodo definido no usa los atributos de la clase.
# A veces se tienen metodos definidos en una clase que no usan los atributos de la clase, lo cual podria ser una señal para reflexionar de si ese metodo realmente debe definirse en esa clase.

class AttributeNodeCounterVisitor(NodeVisitor):
    def __init__(self):
        self.attrs = 0

    def visit_Attribute(self, node: Attribute):
        self.attrs = self.attrs + 1
        
    def total(self):
        return self.attrs


class UncoupledMethodVisitor(WarningNodeVisitor):

    def __init__(self):
        super().__init__()
        self.currentClass = None

    def visit_ClassDef(self, node: ClassDef):
        self.currentClass = node.name
        NodeVisitor.generic_visit(self, node)
        self.currentClass = None

    
    def visit_FunctionDef(self, node: FunctionDef):
        if self.currentClass != None:
            visitor = AttributeNodeCounterVisitor()
            visitor.visit(node)
            if visitor.total() == 0:
                self.addWarning('UncoupledMethodWarning', node.lineno, 'method ' + node.name + ' does not use any attribute')
            NodeVisitor.generic_visit(self, node)


class UncoupledMethodRule(Rule):
    def analyze(self, ast):
        visitor = UncoupledMethodVisitor()
        visitor.visit(ast)
        return visitor.warningsList()
    

# class SuperInitNotCalledRule(Rule):
#     def analyze(self, ast):
#         visitor = UncoupledMethodVisitor()
#         visitor.visit(ast)
#         return visitor.warningsList()