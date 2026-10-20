import os

from dotenv import load_dotenv
from deepeval.models import OpenAIModel

load_dotenv()

eval_model = OpenAIModel(
	model="openai/gpt-oss-120b",
	api_key=os.getenv("GROQ_API_KEY"),
	base_url="https://api.groq.com/openai/v1",
)