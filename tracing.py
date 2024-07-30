import functools  
import time  
from contextvars import ContextVar  
  
class ExecutionNode:  
    def __init__(self, operation, description, orderid):  
        self.operation = operation  
        self.description = description  
        self.orderid = orderid  
        self.children = []  
        self.execution_time = None  
  
    def add_child(self, child):  
        self.children.append(child) 
    def to_dict(self):  
        return {  
            "operation": self.operation,  
            "description": self.description,  
            "orderid": self.orderid,  
            "execution_time": f"{self.execution_time:.2f} seconds" if self.execution_time is not None else "N/A",  
            "children": [child.to_dict() for child in self.children]  
        }  

  
  
execution_trace_var = ContextVar('execution_trace', default=None)  
current_orderid = ContextVar("current_orderid", default=1)  
current_node_stack = ContextVar("current_node_stack", default=[])  
  
def trace_execution(description):  
    def decorator(func):  
        @functools.wraps(func)  
        async def wrapper(*args, **kwargs):  
            trace = execution_trace_var.get()  
            if trace is None:  
                trace = ExecutionNode("Root", "Root operation", 0)  
                execution_trace_var.set(trace)  
                current_node_stack.set([trace])  
  
            orderid = current_orderid.get()  
            node = ExecutionNode(func.__name__, description, orderid)  
            current_orderid.set(orderid + 1)  
  
            stack = current_node_stack.get()  
            parent_node = stack[-1]  
            parent_node.add_child(node)  
            stack.append(node)  
            current_node_stack.set(stack)  
  
            start_time = time.time()  
            result = await func(*args, **kwargs)  
            end_time = time.time()  
            execution_time = end_time - start_time  
            node.execution_time = execution_time  
  
            stack.pop()  
            current_node_stack.set(stack)  
            return result  
        return wrapper  
    return decorator  
  
def display_execution_trace(node, level=0):  
    execution_time_str = f"{node.execution_time:.2f} seconds" if node.execution_time is not None else "N/A"  
    print("  " * level + f"{node.operation}: {node.description}, OrderID: {node.orderid}, Execution Time: {execution_time_str}")  
    for child in node.children:  
        display_execution_trace(child, level + 1)  
