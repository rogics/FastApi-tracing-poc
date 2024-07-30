from fastapi import FastAPI  
from tracing import execution_trace_var  
from main_module import main, main2  
  
app = FastAPI()  
  
@app.get("/trace")  
async def trace():  
    await main()  
    trace = execution_trace_var.get()  
    if trace:  
        return trace.to_dict()  
    return {"message": "No trace found."} 

@app.get("/trace2")  
async def trace():  
    await main2()  
    trace = execution_trace_var.get()  
    if trace:  
        return trace.to_dict()  
    return {"message": "No trace found."}  
  
if __name__ == "__main__":  
    import uvicorn  
    uvicorn.run(app, host="127.0.0.1", port=8000)  
