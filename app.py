import argparse
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import pipeline


app = FastAPI()

summarizer = pipeline("summarization")


class SummarizationRequest(BaseModel):
    text: str
    max_length: int = 130
    min_length: int = 30
    do_sample: bool = True

class SummarizationResponse(BaseModel):
    summary: str

@app.get("/")
def root():
    return {"message": "Welcome to the Text Summarization API!"}

@app.post("/summarize", response_model=SummarizationResponse)
def summarize(request: SummarizationRequest):
    try:
        if len(request.text.strip()) == 0:
            raise HTTPException(status_code=400, detail="Input text cannot be empty.")

        summary = summarizer(
            request.text,
            max_length=request.max_length,
            min_length=request.min_length,
            do_sample=request.do_sample
        )
        return SummarizationResponse(summary=summary[0]['summary_text'])
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    parser = argparse.ArgumentParser(description="Run the FastAPI application.")
    parser.add_argument("--host", type=str, default="0.0.0.0", help="Host to bind the server to.")
    parser.add_argument("--port", type=int, default=8000, help="Port to run the server on.")
    args = parser.parse_args()

    uvicorn.run(app, host=args.host, port=args.port)
