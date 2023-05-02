import os
import openai
from dotenv import load_dotenv
from colorama import Fore, Back, Style
from langchain import HuggingFaceHub

# load values from the .env file if it exists
load_dotenv()

# configure Hugging Face
os.environ["HUGGINGFACEHUB_API_TOKEN"] = "..."

llm = HuggingFaceHub(repo_id="google/flan-t5-xl", model_kwargs={"temperature":0, "max_length":64})

llm("Who is the founder of Amazon?")