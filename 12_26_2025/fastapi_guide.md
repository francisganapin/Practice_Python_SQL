# FastAPI vs Flask vs Django

## Quick Comparison

| Feature | **Django** | **Flask** | **FastAPI** |
| :--- | :--- | :--- | :--- |
| **Type** | Full-Stack Framework | Micro-framework | Modern API Framework |
| **Speed** | Slower (Heavy) | Medium | **Very Fast** (comparable to NodeJS/Go) |
| **Async** | Added later (partial) | Added later (partial) | **Native** (Built-in from start) |
| **Best For** | Large, standard websites (e.g., E-commerce, CMS) | Small-Medium apps, simple tools | **High-performance APIs**, ML models, Backends for React/Vue |
| **Learning Curve** | Steep (Lots to learn) | Easy (Minimal) | Medium (Easy to start, deep features) |
| **Key Feature** | "Batteries Included" (Admin, ORM, Auth) | Flexibility (Choose your own tools) | **Automatic Documentation** (Swagger UI) & Validation |

---

## Why FastAPI?

1.  **Performance**: It uses `Starlette` (for web) and `Pydantic` (for data) to achieve very high performance.
2.  **Automatic Docs**: Just by writing code, you get an interactive documentation page at `/docs`. You can test your API directly from the browser without writing extra HTML/JS.
3.  **Type Safety**: It relies heavily on Python "Type Hints" (e.g., `name: str`). This helps your editor give you better autocompletion and catches bugs early.
4.  **Async/Await**: It was designed for modern asynchronous programming, making it great for handling many requests at once.

---

## How to Run the Sample (`main.py`)

### 1. Install Requirements
You need `fastapi` and `uvicorn` (the server that runs FastAPI).

```bash
pip install fastapi uvicorn
```

### 2. Run the Server
Unlike Flask's `python app.py`, we usually run FastAPI using `uvicorn` from the terminal:

```bash
uvicorn main:app --reload
```

*   `main`: The name of your file (`main.py`).
*   `app`: The name of the FastAPI instance inside the file (`app = FastAPI()`).
*   `--reload`: Restarts the server automatically when you save code changes.

### 3. See the Magic
Open your browser to:
**[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)**

You will see the interactive API documentation where you can try out your endpoints!
