from fastapi import FastAPI
from pydantic import BaseModel
import code_generator

app = FastAPI()

# Request model
class PromptRequest(BaseModel):
    prompt: str

@app.post("/execute")
async def execute_function(request: PromptRequest):
    function_name, generated_code = code_generator.generate_code(request.prompt)
    
    if function_name:
        return {"function": function_name, "code": generated_code}
    return {"error": "No matching function found."}

# Run the API (only when executing api.py directly)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
