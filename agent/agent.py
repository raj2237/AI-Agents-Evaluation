from models import model 
from tools import calculate_right_refund,get_today_date,issue_refund_ticket,get_user_purchase_history
from dotenv import load_dotenv
from langchain.agents import create_agent
from prompts import agent_system_prompt
from objects import ConversationStatus
from langgraph.checkpoint.memory import InMemorySaver
from langchain.messages import HumanMessage 
from uuid import uuid4 

load_dotenv()

agent = create_agent(
    model= model,
    system_prompt = agent_system_prompt,
    tools = [calculate_right_refund,get_today_date,issue_refund_ticket,get_user_purchase_history],
    checkpointer= InMemorySaver()

)
conversation_status_model = model.with_structured_output(
    ConversationStatus,
    method="json_mode",
)

def run_conversation():
    config = {"configurable":{'thread_id': str(uuid4())}}

    text = "I would like to request a refund"
    print(text)
    question = HumanMessage(content = text)

    conversation = True

    while conversation:
        response = agent.invoke({'messages':question},config = config)
        answer = response["messages"][-1].content
        print(answer)

        status = conversation_status_model.invoke(
            "Determine whether this assistant response asks the user for information "
            "or a reply needed to continue the same refund request. Set conversation "
            "to true if it needs another user reply, and false if the refund outcome "
            "is complete. Respond with a valid json object matching the requested "
            f"schema.\n\nAssistant response:\n{answer}"
        )
        conversation = status.conversation
        if conversation:
            user_input = input("reply: \n" )
            question = HumanMessage(content = user_input)
    print("The job is done")

# run_conversation()