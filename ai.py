import requests

def ask_llm(context, question):
    prompt = f"""
You are a helpful assistant.

Use ONLY the context below to answer the question.
If answer is not in context, say "Not found in notes".

Context:
{context}

Question:
{question}
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }
    )

    return response.json()["response"]