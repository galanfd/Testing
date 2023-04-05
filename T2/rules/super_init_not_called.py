from . rule import *


class SuperNotCalledVisitor(WarningNodeVisitor):
    def __init__(self):
        super().__init__()
        self.currentClass = None
        self.line = None

    def visit_ClassDef(self, node: ClassDef):
        self.currentClass = node.name
        self.line = node.lineno
        if node.bases == []:
            return
        NodeVisitor.generic_visit(self, node)
        self.currentClass = None
        # for child in node.body:
        #     if isinstance(child, FunctionDef):
        #         if child.name == '__init__':
        #             for child_ in child.body:
        #                 if isinstance(child_, Expr):
        #                     if isinstance(child_.value, Call):
        #                         if isinstance(child_.value.func, Attribute):
        #                             if child_.value.func.attr == '__init__':
        #                                 return
        #             self.addWarning('SuperInitNotCalled', node.lineno, 'subclass ',node.__class__ ,' does not call to super().__init__()')

    def visit_Call(self, node: Call):
        if self.currentClass != None:
            if isinstance(node.func, Attribute) and \
                    isinstance(node.func.value, Call) and \
                    isinstance(node.func.value.func, Name) and \
                    node.func.value.func.id == 'super' and \
                    node.func.attr == '__init__':
                #self.called_super = True
                return
            print('SuperInitNotCalled'+ str(self.line)+ 'subclass '+self.currentClass +' does not call to super().__init__()')
            self.addWarning('SuperInitNotCalled', self.line, 'subclass '+self.currentClass +' does not call to super().__init__()')
        
        NodeVisitor.generic_visit(self, node)




class SuperInitNotCalledRule(Rule):
    def analyze(self, ast):
        visitor = SuperNotCalledVisitor()
        visitor.visit(ast)
        return visitor.warningsList()