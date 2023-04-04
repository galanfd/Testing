from . rule import *


class VarVisitor(WarningNodeVisitor):
    def __init__(self):
        super().__init__()

    def visit_FunctionDef(self, node: FunctionDef):
        for arg in node.args.args:
            if len(arg.arg) > 15:
                self.addWarning('VariableLongName', node.lineno, 'variable '+ arg.arg + ' has a long name')

        NodeVisitor.generic_visit(self, node)

    def visit_Assign(self, node: Assign):
        var = node.targets[0]

        if isinstance(var, Name):
            if len(var.id) > 15:
                self.addWarning('VariableLongName', var.lineno, 'variable '+ var.id + ' has a long name')

        if isinstance(var, Attribute):
            if len(var.attr) > 15:
                self.addWarning('VariableLongName', var.lineno, 'variable '+ var.attr + ' has a long name')

        NodeVisitor.generic_visit(self, node)


class LongVariableNameRule(Rule):
    def analyze(self, ast):
        visitor = VarVisitor()
        visitor.visit(ast)
        return visitor.warningsList()