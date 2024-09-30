# import os
# from langchain.memory import ConversationSummaryBufferMemory
# from langchain.llms.bedrock import Bedrock
# from langchain.chains import ConversationChain

        
# def get_llm():
        
#     model_kwargs = { #AI21
#         "maxTokens": 1024, 
#         "temperature": 0.9, 
#         "topP": 0.5, 
#         "stopSequences": ["Human:"], 
#         "countPenalty": {"scale": 0 }, 
#         "presencePenalty": {"scale": 0 }, 
#         "frequencyPenalty": {"scale": 0 } 
#     }
    
#     llm = Bedrock(
#         credentials_profile_name= 'default',
#         model_id="ai21.j2-ultra-v1", #set the foundation model
#         model_kwargs=model_kwargs) #configure the properties for Claude
    
#     return llm


# def get_memory(): #create memory for this chat session
#     llm = get_llm()
#     memory = ConversationSummaryBufferMemory(llm=llm, max_token_limit=512) #Maintains a summary of previous messages
#     return memory


# def get_chat_response(input_text, memory): #chat client function
    
#     llm = get_llm()
#     conversation_with_summary = ConversationChain( #create a chat client
#         llm = llm, #using the Bedrock LLM
#         memory = memory, #with the summarization memory
#         verbose = True #print out some of the internal states of the chain while running
#     )
    
#     chat_response = conversation_with_summary.predict(input=input_text) #pass the user message and summary to the model
    
#     return chat_response


import os
from langchain.memory import ConversationSummaryBufferMemory
from langchain.llms.bedrock import Bedrock
from langchain.chains import ConversationChain
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class ChatRequest(BaseModel):
    input_text: str

def get_llm():
    model_kwargs = { #AI21
        "maxTokens": 1024, 
        "temperature": 0.9, 
        "topP": 0.5, 
        "stopSequences": ["Human:"], 
        "countPenalty": {"scale": 0 }, 
        "presencePenalty": {"scale": 0 }, 
        "frequencyPenalty": {"scale": 0 } 
    }
    
    llm = Bedrock(
        credentials_profile_name='default',
        model_id="ai21.j2-ultra-v1", # set the foundation model
        model_kwargs=model_kwargs
    )
    
    return llm

def get_memory():
    llm = get_llm()
    memory = ConversationSummaryBufferMemory(llm=llm, max_token_limit=512) # Maintains a summary of previous messages
    return memory

@app.post("/chat")
async def get_chat_response(request: ChatRequest):
    input_text = request.input_text
    memory = get_memory()
    
    llm = get_llm()
    conversation_with_summary = ConversationChain( 
        llm=llm, 
        memory=memory, 
        verbose=True
    )
    
    chat_response = conversation_with_summary.predict(input=input_text) # Pass the user message and summary to the model
    
    return {"response": chat_response}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
