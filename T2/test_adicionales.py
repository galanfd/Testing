import unittest
from rules import *
from rewriter import *

"""
Template para los tests de las reglas y transformaciones adicionales propuestos por usted.
IMPORTANTE: 
    - Deben existir al menos 5 tests, uno por cada regla/transformador implementado.
    - Los codigos a ser analizados usados en los tests deben ser diferentes.
    - Los tests adicionales deben ser diferentes a los del archivo tests-tarea.py
    - Si usted implemento la tarea en un nuevo archivo dentro del folder rules o rewriter
    no olvide modificar el __init__.py de rules y rewriter para importar los archivos necesarios para su tarea.
    Caso contrario importe lo necesario en este archivo.
"""

class TestWarnings(unittest.TestCase):


    # Funcion que recibe un path del archivo a ser leido y retorna un AST en base al contenido del archivo
    def get_ast_from_file(self, filename):
        file = open(filename)
        fileContent = file.read()
        file.close()
        tree = parse(fileContent)

        return tree

    """ Nombre: test_long_variable_name
        Codigo a ser analizado: extra-test-code/longVariableName.py
        Descripcion: Test para evaluar LongVariableNameRule considerando los siguientes escenarios:
        - Linea 1 : variable entregada a funcion con mas de 15 caracteres
        - Linea 2 : variable de funcion con mas de 15 caracteres definida dentro de funcion
        - Linea 17 : variable de instancia con mas de 15 caracteres declarada en un método
        - Linea 19 : variable global fuera de cualquier scope con mas de 15 caracteres 
        
        Resultado esperado (Una lista de warnings): [
        Warning('VariableLongName', 1, 'variable caso2conmasde15caracteresendefinicion has a long name'),
        Warning('VariableLongName', 2, 'variable probandomasde15caracteresenvariable has a long name'),
        Warning('VariableLongName', 17, 'variable perroladrarguaucon15caracteres has a long name'),
        Warning('VariableLongName', 19, 'variable variableglobalconmasde15caracteres has a long name')]
    """

    def test_long_variable_name(self):
        tree = self.get_ast_from_file('extra-test-code/longVariableName.py')

        longNameRule = LongVariableNameRule()
        result = longNameRule.analyze(tree)


        # Actualice el valor de expectedWarnings de acuerdo a su caso de prueba propuesto
        expectedWarnings = [
        Warning('VariableLongName', 1, 'variable caso2conmasde15caracteresendefinicion has a long name'),
        Warning('VariableLongName', 2, 'variable probandomasde15caracteresenvariable has a long name'),
        Warning('VariableLongName', 17, 'variable perroladrarguaucon15caracteres has a long name'),
        Warning('VariableLongName', 19, 'variable variableglobalconmasde15caracteres has a long name')]

        # print("-----------------------------LONGVARIABLENAME----------------------------------")
        # print((result))
        # print((expectedWarnings))
        # print("--------------------------------------------------------------------------------")

        self.assertEqual(result, expectedWarnings)

    """ Nombre: test_unused_argument
        Codigo a ser analizado: extra-test-code/unusedArgument.py
        Descripcion: Test para evaluar UnusedArgumentRule considerando los siguientes escenarios:
        - Linea <numero-linea> : <Descripcion de codigo - caso a considerar>
        
        Resultado esperado (Una lista de warnings): .....
    """

    def test_unused_argument(self):
        tree = self.get_ast_from_file('extra-test-code/unusedArgument.py')

        unusedArgRule = UnusedArgumentRule()
        result = unusedArgRule.analyze(tree)

        # Actualice el valor de expectedWarnings de acuerdo a su caso de prueba propuesto
        expectedWarnings = []

        self.assertEqual(result, expectedWarnings)


    """ Nombre: test_super_init_not_called
        Codigo a ser analizado: extra-test-code/superInitNotCalled.py
        Descripcion: Test para evaluar SuperInitNotCalledRule considerando los siguientes escenarios:
        - Linea <numero-linea> : <Descripcion de codigo - caso a considerar>
        
        Resultado esperado (Una lista de warnings): .....
    """

    def test_super_init_not_called(self):
        tree = self.get_ast_from_file('extra-test-code/superInitNotCalled.py')

        superInitRule = SuperInitNotCalledRule()
        result = superInitRule.analyze(tree)

        # Actualice el valor de expectedWarnings de acuerdo a su caso de prueba propuesto
        expectedWarnings = [
            Warning('SuperInitNotCalled', 22, 'subclass FlyingSquirrel does not call to super().__init__()')
        ]

        self.assertEqual(result, expectedWarnings)


    """ Nombre: test_minus_equal_rewriter
        Codigo a ser analizado: extra-test-code/minusEquals.py
        Descripcion: Test para evaluar transformador MinusEqualsRewriterCommand considerando los siguientes escenarios:
        - Linea 2 : a = b - 5 : no deberia ser transformado
        - Linea 6: x = x - (y + 1) : deberia ser transformado a x -= (y + 1)
        
        Resultado esperado: extra-test-code/expectedMinusEquals.py
    """

    def test_minus_equal_rewriter(self):
        tree = self.get_ast_from_file('extra-test-code/minusEquals.py')

        command = MinusEqualsRewriterCommand()
        tree = command.apply(tree)

        expectedCode = self.get_ast_from_file('extra-test-code/expectedMinusEquals.py')

        # print("TEST MINUS EQUAL REWRITER")
        # print("_------------------------------------------------------")
        # # print(dump(tree, indent=4))
        # print(unparse(tree))
        # print("_------------------------------------------------------")
        # # print(dump(expectedCode, indent=4))
        # print(unparse(expectedCode))
        # print("_------------------------------------------------------")

        self.assertEqual(dump(tree), dump(expectedCode))


    """ Nombre: test_simplified_if
        Codigo a ser analizado: extra-test-code/simplifiedIf.py
        Descripcion: Test para evaluar SimplifiedIfRewriterCommand considerando los siguientes escenarios:
        - Linea 2: Uso de If cuando tiene un else y el if.test es negado
        - Linea 5: Uso de If que retorna Falso cuando es verdadero y el if.test es negado (debiendo generar doble negacion)
        - Linea 8: Uso de If cuando expresion es booleana (La reconoce como booleana) 


        Resultado esperado: extra-test-code/expectedSimplifiedIf.py
    """

    def test_simplified_if(self):
        tree = self.get_ast_from_file('extra-test-code/simplifiedIf.py')

        command = SimplifiedIfRewriterCommand()
        tree = command.apply(tree)

        expectedCode = self.get_ast_from_file('extra-test-code/expectedSimplifiedIf.py')

        # print("TEST MINUS EQUAL REWRITER")
        # print("_------------------------------------------------------")
        # # print(dump(tree, indent=4))
        # print(unparse(tree))
        # print("_------------------------------------------------------")
        # # print(dump(expectedCode, indent=4))
        # print(unparse(expectedCode))
        # print("_------------------------------------------------------")
        
        self.assertEqual(dump(tree), dump(expectedCode))

if __name__ == '__main__':
    unittest.main()
