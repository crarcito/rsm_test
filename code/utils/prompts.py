from langchain_core.prompts import PromptTemplate

from langchain_core.output_parsers import JsonOutputParser
from langchain_openai import ChatOpenAI
# from langchain_community.chat_models import ChatOpenAI

from langchain_core.output_parsers import StrOutputParser

from utils.prompts_class import DocumentScore, ValidLanguage, ValidQuestion

from config import config
config_env = config['default']

class Prompts():

        # Templates for the prompts si se usa ChatPromptTemplate para obtener la relevancia de los documentos
        global template_DocumentScore
        template_DocumentScore = """
                You need to assign a relevance score to a given context based on a specific question.
                The score should range from 0 to 1, where 0 indicates that the text has no relevance at all, 
                and 1 indicates that it is highly relevant.
                You can use up to two decimal places for the score.
                {format_instructions}
                Question: {question}
                Context: {context}
                """
                # Document: {document}

        # Prompt de instrucciones iniciales para el asistente
        global template_Assistant
        template_Assistant = """
                You are an assistant for question-answering tasks and that searches for information based on the user's search criteria
                You are a Programming Assistant or Systems Developer with expertise in ""Python"" information.
                Your role is to respond to user queries regarding programming, including but not limited to code snippets, libraries, frameworks, best practices, and debugging.
                You will have access to relevant excerpts from official documentation to provide accurate and comprehensive answers to the user's question.

                # Instructions
                - Answer in Spanish.
                - Ensure that the information provided is accurate, clear, and concise.
                - Use only given information
                - If the context provided is empty or you don't know the answer, it indicates that you do not have enough information to answer the question.
                - Do not answer anything outside the context of your role.
                - You will have a text with information about programming or systems development as context. You must review it and verify that it meets the criteria provided by the user.
                - Do not mention topics that do not meet the criteria provided by the user.
                - Each answer should be in separate paragraphs.
                - Use three sentences maximum and keep the answer concise."
                - Use the following pieces of retrieved context to answer the question.

                Context: {context}

                Question: {question}

                Answer:
                """   

        # ValidQuestionWithHistory is used to validate the question based on programming language topics and history
        global template_ValidQuestionWithHistory
        template_ValidQuestionWithHistory="""
                You are an assistant who must determine a question's relationship to the following topics and who validates questions about the characteristics of programming languages. 
                Your topics are:

                - Programming language topics: Questions related to ""Python"" must be allowed.
                - Programming language topics: Questions related to any programming language must be allowed.

                Your only restrictions are:

                #INSTRUCTIONS
                - Answer in Spanish.
                - If the question is not related to programming language topics, you should mark the question as false and provide a reason.
                - You must construct the user's question based on the user's history, obtaining details of previous messages, if necessary, so that the latest message contains the full context of the question the user wants to ask.
                - Always translate the name of the programming language into English.

                {format_instructions}

                History: {chat_history}

                """

        # ValidQuestion is used to validate the question based on programming language topics
        global template_ValidQuestion        
        template_ValidQuestion="""
                You are an assistant who must determine a question's relationship to the following topics and who validates questions about the characteristics of programming languages. 
                Your topics are:

                - Programming language topics: Questions related to ""Python"" must be allowed.
                - Programming language topics: Questions related to any programming language should be allowed, but it should be noted that you will be answering with reference to Python

                #INSTRUCTIONS
                - Answer in Spanish.
                - If the question is not related to programming language topics, you should mark the question as false and provide a reason.
                - Always translate the name of the programming language into English.
                
                Your only restrictions are:
                1) The user can't ask for recommendations or refer to professionals in the field.
                2) The user must ask about at least one programming language; otherwise, the question will refer to ""Python"".


                {format_instructions}
                Question: {question}

                """

        # ValidLanguage is used to validate the Python language of the question
        global template_ValidLanguage        
        template_ValidLanguage = """
                You are an assistant who must extract the programming language information from a user's query, including programming language name and version.
                You have to determine if the language is valid or not; otherwise, the question will refer to ""Python"".

                #INSTRUCTIONS
                - Answer in Spanish
                - If the user does not provide a programming language name, the language value must be "python".
                - If the user doesn't provide the Python programming language, you must leave a message indicating that you will search and answer based on the Python programming language with the information provided. This indicates that at least the programming language must be provided in the question.

                {format_instructions}

                Question: {question}
                """


                
# Function to create a chain from a template
# This function allows you to create a chain based on the provided template and model name.               

def create_Chain_FromTemplate(doc=None, 
                        pydantic: str = "StrOutputParser", 
                        temp: float = 0, 
                        si_format_instructions: bool = False,
                        question: str = ""):

        if pydantic == "StrOutputParser":
                json_parser = StrOutputParser()
                format_instructions = ({"format_instructions": json_parser.get_format_instructions()}) if si_format_instructions else ""
                chain_template = template_Assistant

        elif pydantic == "DocumentScore":
                json_parser = JsonOutputParser(pydantic_object=DocumentScore) 
                format_instructions = ({"format_instructions": json_parser.get_format_instructions()}) if si_format_instructions else ""
                chain_template = template_DocumentScore

        elif pydantic == "Assistant":
                json_parser = StrOutputParser()
                format_instructions = ({"format_instructions": json_parser.get_format_instructions()}) if si_format_instructions else ""
                chain_template = template_Assistant

                
        elif pydantic == "ValidLanguage":
                json_parser = JsonOutputParser(pydantic_object=ValidLanguage) 
                format_instructions = ({"format_instructions": json_parser.get_format_instructions()}) if si_format_instructions else ""
                chain_template = template_ValidLanguage

        elif pydantic == "ValidQuestion":
                json_parser =  JsonOutputParser(pydantic_object=ValidQuestion) 
                format_instructions = ({"format_instructions": json_parser.get_format_instructions()}) if si_format_instructions else ""
                chain_template = template_ValidQuestion

        llm = ChatOpenAI(model=config_env.MODEL_TO_USE, temperature=temp, api_key=config_env.OPENAI_API_KEY)

        if format_instructions:
                prompt_template = PromptTemplate(
                        template=chain_template,
                        input_variables=['question'],
                        partial_variables=format_instructions,
                )
                # input_variables=(['question'] if pydantic != "ValidQuestion" else []) + ['context'] + ['chat_history'] if 'chat_history' in chain_template else [],
        else:
                prompt_template = PromptTemplate(
                        template=chain_template,
                        input_variables=['question'],
        )
                
        return prompt_template | llm | json_parser

def answer_question(inputs, chain):
        question = inputs["question"]
        context = inputs["context"]
        return chain.invoke({"question": question, "context": context})