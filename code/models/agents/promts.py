from openai import OpenAI

# from langchain.prompts import PromptTemplate

# # Modo explicativo
# EXPLANATORY_PROMPT = PromptTemplate(
#     input_variables=["context", "question"],
#     template=(
#         "Basado en el siguiente contexto técnico, explica de forma detallada y educativa:\n\n"
#         "Contexto:\n{context}\n\n"
#         "Pregunta:\n{question}\n\n"
#         "Respuesta:"
#     )
# )

# #  Modo sintético (resumen ejecutivo)
# SUMMARY_PROMPT = PromptTemplate(
#     input_variables=["context", "question"],
#     template=(
#         "Resume la respuesta de manera concisa y profesional basada en el contexto:\n\n"
#         "Contexto:\n{context}\n\n"
#         "Pregunta:\n{question}\n\n"
#         "Resumen:"
#     )
# )

# #  Modo evaluativo
# CRITIQUE_PROMPT = PromptTemplate(
#     input_variables=["context", "question"],
#     template=(
#         "Evalúa críticamente el contenido relacionado con la pregunta y proporciona observaciones objetivas:\n\n"
#         "Contexto:\n{context}\n\n"
#         "Pregunta:\n{question}\n\n"
#         "Evaluación:"
#     )
# )
#  prompt = (
#         f"Eres un experto en lenguaje. Reformula esta pregunta para mejorar la recuperación semántica en un sistema RAG:\n\n{question}"
#     )

# from langchain.prompts import PromptTemplate

# EXPLANATORY_PROMPT = PromptTemplate(
#     input_variables=["context", "question"],
#     template="Usa el siguiente contexto para responder de forma clara:\n\n{context}\n\nPregunta:\n{question}\n\nRespuesta:"
# )

# SUMMARY_PROMPT = PromptTemplate(
#     input_variables=["context", "question"],
#     template="Resume la respuesta de forma concisa:\n\n{context}\n\nPregunta:\n{question}\n\nResumen:"
# )

# CRITIQUE_PROMPT = PromptTemplate(
#     input_variables=["context", "question"],
#     template="Evalúa críticamente el contenido:\n\n{context}\n\nPregunta:\n{question}\n\nEvaluación:"
# )