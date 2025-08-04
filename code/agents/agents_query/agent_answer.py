from openai import OpenAI
# from .chroma_client import retrieve

# llm = OpenAI(api_key="tu_api_key")

# def generate_answer(query: str):
#     context_docs = retrieve(query)
#     context = "\n".join(context_docs)
#     prompt = f"Contexto:\n{context}\n\nPregunta: {query}\nRespuesta:"
    
#     response = llm.chat.completions.create(
#         model="gpt-4",
#         messages=[{"role": "user", "content": prompt}]
#     )
#     return response.choices[0].message.content
