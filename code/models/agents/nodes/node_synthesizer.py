from openai import OpenAI
# from langchain.chat_models import ChatOpenAI
# from prompts import EXPLANATORY_PROMPT, SUMMARY_PROMPT, CRITIQUE_PROMPT

# llm = ChatOpenAI(model="gpt-3.5-turbo")

# def agent_synthesizer(state):
#     context = "\n---\n".join(state["retrieved_texts"])
#     question = state["query_rewritten"]
#     mode = state.get("mode", "explanatory")

#     prompt_map = {
#         "explanatory": EXPLANATORY_PROMPT,
#         "summary": SUMMARY_PROMPT,
#         "critique": CRITIQUE_PROMPT
#     }

#     prompt = prompt_map.get(mode, EXPLANATORY_PROMPT).format(context=context, question=question)
#     response = llm.predict(prompt)
#     state["answer"] = response
#     state["trace"].span(name="synthesizer", input=prompt).set_output(response).end()
#     return state