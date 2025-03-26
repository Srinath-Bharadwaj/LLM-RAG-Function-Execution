import chromadb
from sentence_transformers import SentenceTransformer

# Initialize ChromaDB
client = chromadb.PersistentClient(path="chroma_db")
collection = client.get_or_create_collection(name="functions")

# Load a sentence transformer model for embeddings
model = SentenceTransformer("all-MiniLM-L6-v2")

# Predefined function metadata (function name and description)
functions = {
    "open_chrome": "Launches Google Chrome browser.",
    "open_calculator": "Opens the calculator application.",
    "open_notepad": "Opens the Notepad application.",
    "get_cpu_usage": "Retrieves current CPU usage percentage.",
    "get_ram_usage": "Retrieves current RAM usage percentage.",
    "run_command": "Executes a given shell command."
}

# Store function metadata in the vector database
for func_name, description in functions.items():
    embedding = model.encode(description).tolist()
    collection.add(ids=[func_name], embeddings=[embedding], metadatas=[{"description": description}])

def retrieve_function(user_query):
    """Retrieve the most relevant function based on user input."""
    query_embedding = model.encode(user_query).tolist()
    results = collection.query(query_embeddings=[query_embedding], n_results=1)
    
    if results["ids"][0]:  # If a function is found
        return results["ids"][0][0]  # Return the function name
    return None

# Example test
if __name__ == "__main__":
    query = "Launch Google Chrome"
    function_name = retrieve_function(query)
    print(f"Best match: {function_name}")
