from ast import *
import os
from profiler import Profiler


class ClassInstrumentor(NodeTransformer):
    #clase que implementa metodos de visita necesario para inyectar codigo usando metodos de clase ClassProfiler y recolectar informacion de las funciones que se ejecutan
    def __init__(self):
        super().__init__()
        self.current_class = None
    
    def visit_ClassDef(self, node: ClassDef):
        self.current_class = node.name
        transformedNode = NodeTransformer.generic_visit(self, node)
        self.current_class = None
        # import_profile_injected = parse("from classInstrumentor import ClassProfiler")
        # transformedNode.body.insert(0, import_profile_injected.body[0])
        return transformedNode
    
    def visit_Module(self, node: Module):
        transformedNode = NodeTransformer.generic_visit(self, node)
        import_profile_injected = parse("from classInstrumentor import ClassProfiler")
        transformedNode.body.insert(0, import_profile_injected.body[0])
        fix_missing_locations(transformedNode)
        return transformedNode


    def visit_FunctionDef(self, node: FunctionDef):
        if self.current_class != None:
            transformedNode = NodeTransformer.generic_visit(self, node)
            injectedCode = parse('ClassProfiler.record(\''+
            transformedNode.name+"'" +', '+str(transformedNode.lineno)+', '+self.current_class+')')
        
            if isinstance(transformedNode.body, list):
                transformedNode.body.insert(0, injectedCode.body[0])
            else:
                transformedNode.body = [injectedCode.body[0], node.body]

            fix_missing_locations(transformedNode)
            
            return transformedNode
        else:
            return NodeTransformer.generic_visit(self, node)


class ClassProfiler(Profiler):
    #Clase que rastrea y reporta las clases que se ejecutan
    def __init__(self):
        super().__init__()
        self.class_name = None
        self.class_methods = []
        self.class_methods_executed = []

    @classmethod
    def record(cls, functionName, line, class_name):
        cls.getInstance().ins_record(functionName, line, class_name)

    def ins_record(self, functionName, line, class_name):  
        if (functionName, line, class_name) not in self.class_methods:
            print((functionName, line, class_name))
            self.class_methods.append((functionName, line, class_name))
    
    def report_executed_methods(self):
        #Funcion que retorna una lista con los metodos ejecutados
        return self.class_methods
    def report_executed_by(self, method_name):
        #Funcion que retorna una lista con los metodos ejecutados por un metodo en particular
        return self.class_methods_executed


def instrument(ast):
    visitor = ClassInstrumentor()
    return  fix_missing_locations(visitor.visit(ast))
