import asyncio
from tracing import trace_execution  
  
@trace_execution("Function C")  
async def c():  
    await c1()  
    await c2()  
    await c3()  
  
@trace_execution("Function C1")  
async def c1():  
    await asyncio.sleep(0.1)  
    print("C1")  
  
@trace_execution("Function C2")  
async def c2():  
    await asyncio.sleep(0.2)  
    print("C2")  
  
@trace_execution("Function C3")  
async def c3():  
    await asyncio.sleep(0.3)  
    print("C3")  
