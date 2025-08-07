from flask import Flask, render_template, request
from utils.observability import CrearArchivoLog
from models.agents.nodes.agent_query import query_graph
from config import config
config_env = config['default']

app = Flask(__name__)


CrearArchivoLog()

@app.route("/", methods=["GET", "POST"])
def index():
    
    response = ""
    try:
        question = request.form.get("question")
    except Exception as ex:
        question = ""

    if request.method == "POST":

        state_graph = query_graph.invoke(
            {
                "query": str(question),
                "token": config_env.SECRET_KEY_APP,

                "embedding": [],
                "documents": [""],
                "reranked_docs": [""],
                
                "response_RAG": "",

                "prompt": "",
                "answer_context": [""],

                "answer_final": {}
            }
        )

        result = state_graph["answer_final"]["answer"]

        response = state_graph.get("response", result)

    return render_template("index.html", question_asked=question, response=response)

if __name__ == "__main__":
    # app.run(debug=True)
    app.run(host="0.0.0.0",  port=7103, debug=True)
