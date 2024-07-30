import asyncio
from tracing import trace_execution  
  
@trace_execution("Function A")  
async def a():  
    await a1()  
    await a2()  
    await a3()  
  
@trace_execution("Function A1")  
async def a1():  
    await asyncio.sleep(0.1)  
    print("A1")  
  
@trace_execution("Function A2")  
async def a2():  
    await asyncio.sleep(0.2)  
    print("A2")  
  
@trace_execution("Function A3")  
async def a3():  
    await asyncio.sleep(0.3)  
    print("A3")  
