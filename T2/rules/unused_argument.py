from . rule import *

class UnusedArgVisitor(WarningNodeVisitor):
    def __init__(self):
        super().__init__()
        self.currentClass = None
        self.used_args = set()
        self.current_param = None

    def visit_ClassDef(self, node: ClassDef):
        self.currentClass = node.name # Guardar el nombre de la clase actual
        NodeVisitor.generic_visit(self, node) # Visitar los nodos hijos
        self.currentClass = None # Restaurar el valor de currentClass

    def visit_FunctionDef(self, node: FunctionDef):

        args = [arg.arg for arg in node.args.args] # Obtener los nombres de los argumentos de la funcion

        if self.currentClass != None:
            #eliminate self from the list of arguments
            args = args[1:]
            #hay que ignorar el self de args
        for arg_name in args:
            self.current_param = arg_name
            NodeVisitor.generic_visit(self, node)
            if arg_name not in self.used_args:
                print(f"Unused Argument {node.lineno} argument {arg_name} not used")
                self.addWarning('UnusedArgument', node.lineno, f"argument {arg_name} is not used")
        self.current_param = None
        self.used_args = set()
        NodeVisitor.generic_visit(self, node)

    def visit_Name(self, node: Name):
        if isinstance(node.ctx, Load) and node.id == self.current_param:
            self.used_args.add(node.id)



class UnusedArgumentRule(Rule):

    def analyze(self, ast):
        visitor = UnusedArgVisitor()
        visitor.visit(ast)
        return visitor.warningsList()