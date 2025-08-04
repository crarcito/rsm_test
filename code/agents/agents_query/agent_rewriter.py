import openai

# def agent_rewriter(state):
#     question = state["query"]
#     prompt = f"Reformula esta pregunta para mejorar recuperación semántica:\n{question}"
#     response = openai.chat.completions.create(
#         model="gpt-3.5-turbo",
#         messages=[{"role": "user", "content": prompt}]
#     )
#     state["query_rewritten"] = response.choices[0].message.content.strip()
#     state["trace"].span(name="rewriter", input=question).set_output(state["query_rewritten"]).end()
#     return state
