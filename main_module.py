from tracing import trace_execution  
  
@trace_execution("Main function")  
async def main():  
    from module_a import a  
    from module_b import b  
    from module_c import c  
  
    await a()  
    await b()  
    await c()  

@trace_execution("Main function")  
async def main2():  
    from module_a import a  
    from module_b import b 
  
    await a()  
    await b() 
