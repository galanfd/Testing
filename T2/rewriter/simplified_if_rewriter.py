from .rewriter import *

class SimplifiedIfTransformer(NodeTransformer):
    def visit_Return(self, node):
        if isinstance(node.value, IfExp):
            if isinstance(node.value.body, NameConstant) and isinstance(node.value.orelse, NameConstant):
                if node.value.body.value is True and node.value.orelse.value is False:
                    return Return(value=node.value.test)
                elif node.value.body.value is False and node.value.orelse.value is True:
                    new_node = UnaryOp(op=Not(), operand=node.value.test)
                    return Return(value=new_node)
        return node





class SimplifiedIfRewriterCommand(RewriterCommand):

    def apply(self, ast):
        new_tree = fix_missing_locations(SimplifiedIfTransformer().visit(ast))
        return new_tree