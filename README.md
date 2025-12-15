
## Barebone Vector DB

Simple vector database API using FastAPI and MiniLM embeddings.

### How It Works

This project provides a simple vector database that operates "in-memory" with disk persistence. Here's a breakdown of its core components:

*   **FastAPI Server**: The backbone of the project is a web server built with `FastAPI`. It exposes RESTful API endpoints to add data, search for similar items, and retrieve all data.

*   **Vector Database (`VectorDB` class)**:
    *   **Persistence**: The vector database stores its data in the `data/` directory.
        *   **Vectors**: The numerical vector embeddings are stored in a NumPy binary file (`vectors.npy`).
        *   **Metadata**: The corresponding metadata for each vector is kept in a structured JSON file (`metadata.json`).
    *   **In-Memory Operation**: On startup, the server loads the vectors and metadata into memory, allowing for fast access and computations.

*   **Text Embedding**:
    *   **SentenceTransformer**: The project uses the popular `sentence-transformers/all-MiniLM-L6-v2` model to convert text into meaningful 384-dimensional vector embeddings.
    *   **Embedding Process**: When you add new text, it's passed through this model to generate a vector, which is then stored.

*   **Similarity Search**:
    *   **Cosine Similarity**: To find text similar to a query, the query is first embedded into a vector. Then, the **cosine similarity** is calculated between this query vector and every other vector in the database.
    *   **Top-K Results**: The API returns the `top_k` most similar entries based on their cosine similarity scores.

### API Endpoints

The following are the primary endpoints available:

*   `POST /add`: Adds a new text entry to the database.
    *   **Body**: `{ "text": "...", "label": "...", "source": "..." }`
*   `POST /invoke`: Searches the database for text similar to the query.
    *   **Body**: `{ "query": "...", "top_k": 5 }`
*   `GET /all`: Retrieves all vectors and metadata stored in the database.

For detailed request and response models, see the auto-generated OpenAPI documentation at `/docs`.

### Setup and Run

#### 1. Create a virtual environment
```bash
python -m venv venv
```
#### 2. Activate the virtual environment

* **Windows:**

```bash
venv\Scripts\activate
```

* **Linux / macOS:**

```bash
source venv/bin/activate
```

#### 3. Install dependencies

```bash
pip install -r requirements.txt
```

#### 4. Run the FastAPI app

```bash
uvicorn app:app --reload --port 8000
```

#### 5. Access

* API: `http://127.0.0.1:8000`
* Docs: `http://127.0.0.1:8000/docs`
