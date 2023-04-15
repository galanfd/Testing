from ast import *
import os
import inspect
from profiler import Profiler
import re


class ClassInstrumentor(NodeTransformer):
    #clase que implementa metodos de visita necesario para inyectar codigo usando metodos de clase ClassProfiler y recolectar informacion de las funciones que se ejecutan
    def __init__(self):
        super().__init__()
        self.current_class = None
        self.current_function = None
        self.called_functions = []
    
    def visit_ClassDef(self, node: ClassDef):
        # class_id = id(node)
        self.current_class = node.name
        # self.class_map[class_id] = node.name
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
            transformedNode.name+"'" +', '+str(transformedNode.lineno)+', '+"'"+self.current_class+"'"+')')
            injectedCode2 = parse('ClassProfiler.record_caller(\''+
            transformedNode.name+"'" +', '+str(transformedNode.lineno)+', '+"'"+self.current_class+"'"+')')
        
            if isinstance(transformedNode.body, list):
                transformedNode.body.insert(0, injectedCode.body[0])
                transformedNode.body.insert(0, injectedCode2.body[0])
            else:
                transformedNode.body = [injectedCode.body[0], node.body]
                transformedNode.body = [injectedCode2.body[0], node.body]

            fix_missing_locations(transformedNode)
            
            return transformedNode
        
        else:
            self.current_function = node.name
            transformedNode = NodeTransformer.generic_visit(self, node)
            self.current_function = None
            return transformedNode



    # def visit_Call(self, node: Call):
    #     if isinstance(node.func, Name):
    #         function_name = node.func.id
    #         self.called_functions.append((function_name, node.lineno))
    #     elif isinstance(node.func, Attribute) and node.func.value.id != "assert":
    #         function_name = node.func.attr
    #         self.called_functions.append((function_name, node.lineno))
    #     self.generic_visit(node)



class ClassProfiler(Profiler):
    #Clase que rastrea y reporta las clases que se ejecutan
    def __init__(self):
        super().__init__()
        self.class_name = None
        self.class_methods = []
        self.class_methods_executed = []
        self.caller_records = {}

    @classmethod
    def record(cls, functionName, line, class_name):
        cls.getInstance().ins_record(functionName, line, class_name)

    def ins_record(self, functionName, line, class_name):
        if (functionName, line, class_name) not in self.class_methods:
            # print((functionName, line, class_name))
            self.class_methods.append((functionName, line, class_name))

    @classmethod
    def record_caller(cls, method_name, line, class_name):
        caller_name = inspect.stack()[2][3]
        cls.getInstance().ins_record_calls(method_name, line, class_name, caller_name)

    def ins_record_calls(self, method_name, line, class_name, caller_name):
        #print((method_name, line, class_name, caller_name))
        #key = (method_name, line, class_name)
        key = caller_name
        if key not in self.caller_records:
            self.caller_records[key] = []
        if (method_name, line, class_name) not in self.caller_records[key]:
            self.caller_records[key].append((method_name, line, class_name))
        # if (method_name, calls) not in self.class_methods_executed:
        #     self.class_methods_executed.append((method_name, calls))

    def report_executed_methods(self):
        #Funcion que retorna una lista con los metodos ejecutados
        return sort_list(self.class_methods)
    
    def report_executed_by(self, method_name):
        #Funcion que retorna una lista con los metodos ejecutados por un metodo en particular
        return sort_list(self.caller_records[method_name])

def sort_list(list):
    sorted_tuples = sorted(list, key=lambda x: x[1])
    return sorted_tuples

def instrument(ast):
    visitor = ClassInstrumentor()
    return  fix_missing_locations(visitor.visit(ast))
