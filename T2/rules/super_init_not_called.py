from . rule import *


class SuperNotCalledVisitor(WarningNodeVisitor):
    def __init__(self):
        super().__init__()
        self.currentClass = None
        self.line = None
        self.called_super = False

    def visit_ClassDef(self, node: ClassDef):
        self.currentClass = node.name
        self.line = node.lineno
        if node.bases == []:
            return
        NodeVisitor.generic_visit(self, node)
        self.currentClass = None

    def visit_FunctionDef(self, node: FunctionDef):
        if self.currentClass != None and node.name == '__init__':
            self.called_super = False
            NodeVisitor.generic_visit(self, node)
            if not self.called_super:
                #print("SuperInitNotCalled" + str(self.line) + 'subclass ' + self.currentClass + ' does not call to super().__init__()')
                self.addWarning('SuperInitNotCalled', self.line, 'subclass '+ self.currentClass+ ' does not call to super().__init__()')

    def visit_Call(self, node: Call):
        if isinstance(node.func, Name) and node.func.id == "super" and self.currentClass != None:
            self.called_super = True
        else:
            NodeVisitor.generic_visit(self, node)



class SuperInitNotCalledRule(Rule):
    def analyze(self, ast):
        visitor = SuperNotCalledVisitor()
        visitor.visit(ast)
        return visitor.warningsList()