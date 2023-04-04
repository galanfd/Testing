from . rule import *


class SuperNotCalledVisitor(WarningNodeVisitor):
    def __init__(self):
        super().__init__()

    def visit_ClassDef(self, node: ClassDef):
        for child in node.body:
            if isinstance(child, FunctionDef):
                if child.name == '__init__':
                    for child_ in child.body:
                        if isinstance(child_, Expr):
                            if isinstance(child_.value, Call):
                                if isinstance(child_.value.func, Attribute):
                                    if child_.value.func.attr == '__init__':
                                        return
                    self.addWarning('SuperInitNotCalled', node.lineno, 'subclass ',node.__class__ ,' does not call to super().__init__()')

        NodeVisitor.generic_visit(self, node)



class SuperInitNotCalledRule(Rule):
    def analyze(self, ast):
        visitor = SuperNotCalledVisitor()
        visitor.visit(ast)
        return visitor.warningsList()