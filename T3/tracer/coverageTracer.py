import sys
import ast
import traceback
from stackInspector import StackInspector

""" Clase para rastrear funciones que fueron ejecutadas. Para su uso, considere:
with CoverageTracer() as coverage:
    function_to_be_traced()

coverage.report_executed_lines()
"""

class CoverageTracer(StackInspector):

    def __init__(self):
        # super().__init__(None, self.traceit)
        self.executed_lines = set()

    def traceit(self, frame, event, arg):
        if self.our_frame(frame) or self.problematic_frame(frame):
            # No rastrearemos nuestros propios metodos
            pass
        else:
            self.log(event, frame.f_lineno, frame.f_code.co_name, frame.f_locals)
        return self.traceit

    def log(self, *objects, sep: str = ' ', end: str = '\n', flush=True):
        if objects[0] == 'line':
            if (objects[1], objects[2]) not in self.executed_lines:
                self.executed_lines.add((objects[2], objects[1]))
                # print((objects[0], objects[1], objects[2]))
        # self.executed_lines.add((objects[1], objects[2]))
        # print((objects[0], objects[1], objects[2]))
        # print(*objects, sep=sep, end=end, flush=flush)

    def __enter__(self):
        self.original_trace_function = sys.gettrace()
        sys.settrace(self.traceit)
        return self
    
    def __exit__(self, exc, exc_value, exc_traceback):
        sys.settrace(self.original_trace_function)

        # Note que debemos retornar un valor 'False' para indicar que hubo un error interno y levantar las excepciones correspondientes.
        if self.is_internal_error(exc, exc_value, exc_traceback):
            return False
        else:
            # Significa que _todo funciona bien
            return None
        
    def report_executed_lines(self):
        return sorted(self.executed_lines)