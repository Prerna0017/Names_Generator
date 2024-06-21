from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
import langchain_community
import streamlit as st

OPENAI_API_KEY = st.secrets["OpenAI_api"]

llm = OpenAI(model_name="gpt-3.5-turbo-instruct", temperature = 0.6)

def generate_baby_names(gender: str,nationality:str) -> list[str]:
    prompt_template_name = PromptTemplate(
        input_variables=['gender', 'nationality'],
        template="""I want to find a name for a {nationality} {gender} baby. 
                    Suggest top 5 popular names for the baby.
                    Return it as a comma separated list """
                )

    name_chain = LLMChain(llm=llm,
                          prompt=prompt_template_name,
                          output_key='baby_names')

    chain = SequentialChain(
        chains=[name_chain],
        input_variables=['gender', 'nationality'],
        output_variables=['baby_names']
    )

    response = chain({'gender': gender,
                      'nationality': nationality})
    return response
