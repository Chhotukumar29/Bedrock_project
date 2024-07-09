from langchain.llms.bedrock import Bedrock 
from langchain.chians import LLMChain
from langchain.prompts import PromptTemplate
import boto3 
import sys
from langchain.llms.bedrock import Bedrock
#bedrock  client 
bedrock_client = boto3.client(
    service_name = 'bedrock-runtime',
    region_name = 'us-east-1'   
)

model_id =  "ai21.j2-mid-v1" 

llm = Bedrock(
    model_id=model_id,
    client = bedrock_client
)

def my_model(use_prompt):
    prompt = PromptTemplate(
        input_variables=['user_prompt'],
        template= 'You are a chatbot.Provide answers for {user_prompt}'
    )


    bedrock_chain = LLMChain(llm = llm, prompt= prompt)
    bedrock_chain({"user_prompt": user_prompt})

    return response

my_model = 'What is Python?'
res = my_model(user_prompt)
print(res['text']) 
