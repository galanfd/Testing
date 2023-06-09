from .rule import *

# Clases que permiten detectar si algun atributo no fue inicializado.
# A veces se usan algunos atributos que no estan inicializados y esto genera errores.

class AttributeUsageVisitor(WarningNodeVisitor):

    def __init__(self):
        super().__init__()
        self.initialized = []
        self.currentClass = None

    def visit_ClassDef(self, node: ClassDef):
        self.currentClass = node.name
        NodeVisitor.generic_visit(self, node)

        self.currentClass = None
        self.initialized = []

    def visit_Assign(self, node: Assign): #recorrer los argumentos de la funcion
        if self.currentClass != None:
            if isinstance(node.targets[0], Attribute): #si el target es un atributo
                self.initialized.append(node.targets[0].attr)
            NodeVisitor.generic_visit(self, node)
    
    def visit_Attribute(self, node: Attribute):
        if self.currentClass != None:
            if self.initialized.count(node.attr) == 0:
                self.addWarning('UninitilizeAttrWarning', node.lineno, 'attribute '+ node.attr + ' was not initialized')
            NodeVisitor.generic_visit(self, node)


class UninitializedAttributeRule(Rule):

    def analyze(self, ast):
        visitor = AttributeUsageVisitor()
        visitor.visit(ast)
        return visitor.warningsList()

# class UnusedArgumentRule(Rule):

#     def analyze(self, ast):
#         visitor = AttributeUsageVisitor()
#         visitor.visit(ast)
#         return visitor.warningsList()