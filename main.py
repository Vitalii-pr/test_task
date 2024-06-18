from fastapi import FastAPI
from schema import SummarizedText, TextToSummarizer
from langchain_sum import summarize_text
import uvicorn


app = FastAPI()


@app.post('/summarize', response_model = SummarizedText, status_code=200)
def return_summarized_text(text_to_summarize: TextToSummarizer):
    summarized = summarize_text(text_to_summarize.text)
    return {"text": summarized}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)