from typing import List
import utils.prompts as prompts

def generate_answer_query_node(query: str, context: List[str], state, top_k: int = 3):

    chain = prompts.create_Chain_FromTemplate(None, "Assistant", 0.5, False)

    state["prompt"] = chain
    state["answer_context"] = context
    

    answer_context = prompts.answer_question({"question": query, "context": context}, chain)

    return {"answer_context": answer_context, "prompt": chain}
