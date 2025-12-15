
from pydantic import BaseModel
from typing import Optional, List

# --- Request and Response Models for /add endpoint ---
class AddRequest(BaseModel):
    """Request model for adding a new text entry to the database."""
    text: str                 # The text content to be embedded and stored.
    label: str                # A required label for the text, used for categorization.
    source: Optional[str] = None # An optional source or reference for the text.

class AddResponse(BaseModel):
    """Response model after successfully adding a new entry."""
    status: str               # The status of the operation (e.g., "success").
    vector_index: int         # The index of the newly added vector in the database.

# --- Request and Response Models for /invoke endpoint ---
class InvokeRequest(BaseModel):
    """Request model for searching the vector database."""
    query: str                # The query text to search for similar entries.
    top_k: int = 5            # The number of top similar results to return.

class ResultItem(BaseModel):
    """A single result item in the search response."""
    index: int                # The index of the found vector in the database.
    score: float              # The cosine similarity score of the result.
    metadata: dict            # The metadata associated with the found vector.

class InvokeResponse(BaseModel):
    """Response model for a search query, containing a list of results."""
    results: List[ResultItem]