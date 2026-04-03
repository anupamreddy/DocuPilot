import json

from langgraph.prebuilt import create_react_agent
from langchain_openai import ChatOpenAI

from ansible_tool import run_ansible_playbook_with_password
from human_help_tool import need_help
from chroma_tools import search_in_chroma

with open("prompts.json", "r") as prompts_json:
    prompts = json.load(prompts_json)

def agent_factory(agent_name, model_name = "gpt-4o-mini"):
    
    if(agent_name == "doc_agent"):
        model = ChatOpenAI(model = model_name)
        info_agent = agent_factory("info_agent" ,model_name)
        agent = create_react_agent(
            model,
            tools = [run_ansible_playbook_with_password, info_agent.as_tool(name= "info_agent", description="This agent has a knowledge base, this can provide information that you need")],
            prompt = prompts.get("doc_agent_prompt")
        )

        return agent

    elif(agent_name == "info_agent"):
        model = ChatOpenAI(model = model_name)
        agent = create_react_agent(
            model,
            tools=[search_in_chroma, need_help],
            prompt = prompts.get("info_agent_prompt")
        )

        return agent
