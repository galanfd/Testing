from .rewriter import *

class SimplifiedIfTransformer(NodeTransformer):
    def visit_If(self, node: If):
        new_node = If(test=node.test, body=node.body, orelse=node.orelse)
        if isinstance(node.test, Compare):
            if isinstance(node.test.left, Name) and isinstance(node.test.comparators[0], Name):
                if node.test.ops[0] == Eq():
                    if isinstance(node.body[0], Assign):
                        if isinstance(node.body[0].value, Name):
                            if node.body[0].value.id == node.test.left.id:
                                new_node.test = node.test.left
                                return new_node
                            elif node.body[0].value.id == node.test.comparators[0].id:
                                new_node.test = UnaryOp(op=Not(), operand=node.test.left)
                                return new_node
        return node


class SimplifiedIfRewriterCommand(RewriterCommand):

    def apply(self, ast):
        new_tree = fix_missing_locations(SimplifiedIfTransformer().visit(ast))
        return new_tree