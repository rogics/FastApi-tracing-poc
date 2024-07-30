import asyncio
from tracing import trace_execution  
  
@trace_execution("Function B")  
async def b():  
    await b1()  
    await b2()  
    await b3()  
  
@trace_execution("Function B1")  
async def b1():  
    await asyncio.sleep(0.1)  
    print("B1")  
  
@trace_execution("Function B2")  
async def b2():  
    await asyncio.sleep(0.2)  
    print("B2")  
  
@trace_execution("Function B3")  
async def b3():  
    await asyncio.sleep(0.3)  
    print("B3")  
