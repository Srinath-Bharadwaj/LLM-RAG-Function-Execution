import automation_functions
import function_retriever

def generate_code(user_prompt):
    """Generates executable Python code for the retrieved function."""
    function_name = function_retriever.retrieve_function(user_prompt)
    
    if function_name:
        code_snippet = f"""
from automation_functions import {function_name}

def main():
    try:
        {function_name}()
        print("{function_name} executed successfully.")
    except Exception as e:
        print(f"Error executing function: {{e}}")

if __name__ == "__main__":
    main()
"""
        return function_name, code_snippet.strip()
    
    return None, "No matching function found."

# Example test
if __name__ == "__main__":
    user_input = "Open calculator"
    func_name, generated_code = generate_code(user_input)
    print(f"Function: {func_name}")
    print("Generated Code:\n")
    print(generated_code)
