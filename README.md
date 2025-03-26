# LLM-RAG-Function-Execution

Python API service with LLM + RAG for executing automation functions.  
Part of the assignment for Algo Root.

## 🚀 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Srinath-Bharadwaj/LLM-RAG-Function-Execution.git
   cd LLM-RAG-Function-Execution
Create a virtual environment and activate it:

bash
Copy
Edit
python -m venv env
source env/bin/activate  # On Windows use: env\Scripts\activate
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
▶️ Running the API
To start the API, run:

bash
Copy
Edit
uvicorn api:app --reload
The API will be available at: http://127.0.0.1:8000

📌 Usage Example
Request:

bash
Copy
Edit
curl -X POST "http://127.0.0.1:8000/execute_function" -H "Content-Type: application/json" -d '{"function_name": "greet", "parameters": {"name": "Alice"}}'
Response:

json
Copy
Edit
{
  "result": "Hello, Alice!"
}
📚 How It Works
The API receives a function request with parameters.

It retrieves the function using LLM + RAG.

The function is executed dynamically, and the result is returned.

📝 License
This project is for educational purposes.

2. **Commit and push the changes:**  
   ```bash
   git add README.md
   git commit -m "Updated README.md with installation and usage details"
   git push origin main
