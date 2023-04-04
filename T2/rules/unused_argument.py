from . rule import *

class UnusedArgVisitor(WarningNodeVisitor):
    def __init__(self):
        super().__init__()

    def visit_FunctionDef(self, node: FunctionDef):
        for child in node.args.args:
            if child.arg not in node.body[0].targets[0].elts:
                self.addWarning('UnusedArgument', node.lineno, 'argument ',child.arg, ' is not used')

        NodeVisitor.generic_visit(self, node)


class UnusedArgumentRule(Rule):

    def analyze(self, ast):
        visitor = UnusedArgVisitor()
        visitor.visit(ast)
        return visitor.warningsList()