from .rewriter import *

class MinusEqualsTransformer(NodeTransformer):
    def visit_Assign(self, node: Assign):
        new_node = AugAssign(op=Sub(), target=node.targets[0], value=BinOp(left=node.targets[0], op=Sub(), right=node.value))
        # new_node = AugAssign(op=Sub(), target=node.targets)
        var = node.targets[0]

        if isinstance(var, Name) and isinstance(node.value, BinOp):

            if isinstance(node.value.left, Name) and node.value.left.id == var.id:
                new_node.value = node.value.right
                return new_node

            elif isinstance(node.value.right, Name) and node.value.right.id == var.id:
                new_node.value = node.value.left
                return new_node

        if isinstance(var, Attribute) and isinstance(node.value, BinOp):
            if isinstance(node.value.left, Attribute) and node.value.left.attr == var.attr:
                new_node.value = node.value.right
                return new_node
            
            elif isinstance(node.value.right, Attribute) and node.value.right.attr == var.attr:
                new_node.value = node.value.left
                return new_node

        return node


class MinusEqualsRewriterCommand(RewriterCommand):

    def apply(self, ast):
        new_tree = fix_missing_locations(MinusEqualsTransformer().visit(ast))
        return new_tree