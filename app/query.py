# from langchain.document_loaders import WebBaseLoader
# from langchain.text_splitter import RecursiveCharacterTextSplitter
# from langchain.embeddings import OpenAIEmbeddings
# from langchain.vectorstores import FAISS

# from langchain.chat_models import ChatOpenAI


# from langchain.chains import RetrievalQA
# from langchain.prompts import PromptTemplate
# from langchain.callbacks import LangChainTracer

# from ..config import config
import os
import dotenv

def answer_query(question: str):
    dotenv.load_dotenv()
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

    # settings = config['development']
    # OPENAI_API_KEY = settings.OPENAI_API_KEY

    # db = FAISS.load_local("vector_index", OpenAIEmbeddings(), allow_dangerous_deserialization=True)
    # retriever = db.as_retriever(search_type="similarity", search_kwargs={"k": 5})

    # llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.1, api_key=OPENAI_API_KEY)
    # qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

    # question = "Qué es thinking?"
    # result = qa_chain.run(question)

    # sources = retriever.get_relevant_documents(question)
    # return {
    #     "answer": result,
    #     "sources": [{"page": i+1, "text": doc.page_content} for i, doc in enumerate(sources)]
    # }
    return {
        "answer": "algooo.",  # Replace with actual logic 
        "sources": [{"page": 1, "text": OPENAI_API_KEY}]  # Replace with actual sources
    }