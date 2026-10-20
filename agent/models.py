from dotenv import load_dotenv
from langchain.chat_models import init_chat_model 

load_dotenv()  # Load environment variables from .env file
model = init_chat_model('openai/gpt-oss-120b', model_provider='groq')

# response =  model.invoke("Tell me something about Madhya Pradesh")
# print(response)