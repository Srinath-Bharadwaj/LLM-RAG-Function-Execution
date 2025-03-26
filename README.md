# LLM-RAG-Function-Execution

Python API service with LLM + RAG for executing automation functions.  
Part of the assignment for Algo Root.

## 🚀 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Srinath-Bharadwaj/LLM-RAG-Function-Execution.git
   cd LLM-RAG-Function-Execution
   
Create a virtual environment and activate it:
```python 
-m venv env
source env/bin/activate  # On Windows use: env\Scripts\activate```
```

Install dependencies:
```bash
pip install -r requirements.txt
```

▶️ Running the API
To start the API, run:
```bash
uvicorn api:app --reload
```

The API will be available at: http://127.0.0.1:8000

📌 Usage Example
Request:
```bash
curl -X POST "http://127.0.0.1:8000/execute_function" -H "Content-Type: application/json" -d '{"function_name": "greet", "parameters": {"name": "Srinath"}}'
```

Response:
```json
{
  "result": "Hello, Srinath!"
}
```
📚 How It Works
The API receives a function request with parameters.

It retrieves the function using LLM + RAG.

The function is executed dynamically, and the result is returned.

📝 License:
This project is for internship purposes.
