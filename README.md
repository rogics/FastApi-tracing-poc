
# FastAPI Execution Trace POC

This project demonstrates a method for tracing the execution of functions within a FastAPI application. The execution trace captures the execution time and order of nested function calls and returns this trace as a JSON response.

## Project Structure

```
project/
│
├── app.py
├── main_module.py
├── module_a.py
├── module_b.py
├── module_c.py
└── tracing.py
```

- `app.py`: The main FastAPI application module.
- `main_module.py`: Contains the `main` function.
- `module_a.py`: Contains functions related to module A.
- `module_b.py`: Contains functions related to module B.
- `module_c.py`: Contains functions related to module C.
- `tracing.py`: Contains the tracing logic and context management.

## Setup Instructions

1. **Clone the Repository**

   ```bash
   git clone <repository_url>
   cd project
   ```

2. **Create a Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**

   ```bash
   pip install fastapi uvicorn
   ```

4. **Run the Application**

   ```bash
   uvicorn app:app --reload
   ```

5. **Access the Endpoint**

   Open your browser and navigate to `http://127.0.0.1:8000/trace` or use a tool like `curl` or Postman to send a GET request to this endpoint.

## Code Overview

### `tracing.py`

- Contains the `ExecutionNode` class that represents each node in the execution trace.
- Uses `ContextVar` to manage execution context and ensure thread safety.
- Provides the `trace_execution` decorator to trace function execution.

### `main_module.py`

- Defines the `main` function, which calls functions from module A, B, and C.

### `module_a.py`, `module_b.py`, `module_c.py`

- Define functions `a`, `b`, `c` and their nested functions `a1`, `a2`, `a3`, `b1`, `b2`, `b3`, `c1`, `c2`, `c3` respectively.
- Functions are decorated with `trace_execution` to capture execution details.

### `app.py`

- Sets up the FastAPI application.
- Defines an endpoint `/trace` to trigger the `main` function and return the execution trace.

## Example Output

When you access the `/trace` endpoint, the response will be a JSON object representing the execution trace. Example:

```json
{
  "operation": "Root",
  "description": "Root operation",
  "orderid": 0,
  "execution_time": "N/A",
  "children": [
    {
      "operation": "main",
      "description": "Main function",
      "orderid": 1,
      "execution_time": "0.60 seconds",
      "children": [
        {
          "operation": "a",
          "description": "Function A",
          "orderid": 2,
          "execution_time": "0.60 seconds",
          "children": [
            {
              "operation": "a1",
              "description": "Function A1",
              "orderid": 3,
              "execution_time": "0.10 seconds",
              "children": []
            },
            {
              "operation": "a2",
              "description": "Function A2",
              "orderid": 4,
              "execution_time": "0.20 seconds",
              "children": []
            },
            {
              "operation": "a3",
              "description": "Function A3",
              "orderid": 5,
              "execution_time": "0.30 seconds",
              "children": []
            }
          ]
        },
        {
          "operation": "b",
          "description": "Function B",
          "orderid": 6,
          "execution_time": "0.60 seconds",
          "children": [
            {
              "operation": "b1",
              "description": "Function B1",
              "orderid": 7,
              "execution_time": "0.10 seconds",
              "children": []
            },
            {
              "operation": "b2",
              "description": "Function B2",
              "orderid": 8,
              "execution_time": "0.20 seconds",
              "children": []
            },
            {
              "operation": "b3",
              "description": "Function B3",
              "orderid": 9,
              "execution_time": "0.30 seconds",
              "children": []
            }
          ]
        },
        {
          "operation": "c",
          "description": "Function C",
          "orderid": 10,
          "execution_time": "0.60 seconds",
          "children": [
            {
              "operation": "c1",
              "description": "Function C1",
              "orderid": 11,
              "execution_time": "0.10 seconds",
              "children": []
            },
            {
              "operation": "c2",
              "description": "Function C2",
              "orderid": 12,
              "execution_time": "0.20 seconds",
              "children": []
            },
            {
              "operation": "c3",
              "description": "Function C3",
              "orderid": 13,
              "execution_time": "0.30 seconds",
              "children": []
            }
          ]
        }
      ]
    }
  ]
}
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/)

```
