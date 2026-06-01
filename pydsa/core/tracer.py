import sys
import inspect

class AlgorithmTracer:
    """
    Hooks into the Python interpreter to capture local variables
    line-by-line as an algorithm executes.
    """
    def __init__(self, target_func_name="solve", max_steps=100):
        self.target_func_name = target_func_name
        self.max_steps = max_steps
        self.history = []
        self._last_locals = {}

    def trace_calls(self, frame, event, arg):
        if event == 'call':
            func_name = frame.f_code.co_name
            if func_name == self.target_func_name:
                return self.trace_lines
        return None

    def trace_lines(self, frame, event, arg):
        if event in ['line', 'return']:
            if len(self.history) >= self.max_steps:
                return None # Stop tracing if it's an infinite loop or massive array
            
            # Capture local variables, ignoring python internals (starting with _)
            current_locals = {
                k: str(v)[:50] + ("..." if len(str(v)) > 50 else "") # truncate massive strings/arrays
                for k, v in frame.f_locals.items() 
                if not k.startswith('_')
            }

            # Only save a step if variables actually changed (filters out empty lines)
            if current_locals != self._last_locals:
                self.history.append((frame.f_lineno, current_locals.copy()))
                self._last_locals = current_locals

        return self.trace_lines