from openai import OpenAI
# def agent_critic(state):
#     answer = state["answer"]
#     if len(answer) < 100:
#         state["answer"] += "\n(Respuesta breve: el contenido puede ser limitado)"
#     state["trace"].span(name="critic", input=answer).set_output(state["answer"]).end()
#     return state