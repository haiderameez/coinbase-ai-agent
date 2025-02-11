from transformers import AutoModelForCausalLM, AutoTokenizer
from cdp_langchain.agent_toolkits import CdpToolkit
from cdp_langchain.utils import CdpAgentkitWrapper
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import MemorySaver
import os
from dotenv import load_dotenv

load_dotenv()

def initialize_agent():
    """Initialize the agent with CDP AgentKit and an open-source language model."""
    
    model_name = "meta-llama/Meta-Llama-3.2-1B"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
    
    agentkit = CdpAgentkitWrapper(
        cdp_api_key_name=os.getenv("CDP_API_KEY_NAME"),
        cdp_api_key_private_key=os.getenv("CDP_API_KEY_PRIVATE_KEY"),
        network_id=os.getenv("NETWORK_ID")
    )
    
    cdp_toolkit = CdpToolkit.from_cdp_agentkit_wrapper(agentkit)
    cdp_tools = cdp_toolkit.get_tools()
    
    memory = MemorySaver()
    
    config = {
        "configurable": {
            "thread_id": "CDP_AgentKit_Chatbot_Example",
            "checkpoint_ns": "cdp_agent",
            "checkpoint_id": "default"
        }
    }
    
    agent = create_react_agent(
        model,
        tokenizer=tokenizer,
        tools=cdp_tools,
        checkpointer=memory,
        state_modifier=(
            "You are a helpful agent that can interact onchain on the Base Layer 2 "
            "using the Coinbase Developer Platform AgentKit. You are empowered to "
            "interact onchain using your tools. If you ever need funds, you can request "
            "them from the faucet. You can also deploy your own ERC-20 tokens, NFTs, "
            "and interact with them. If someone asks you to do something you can't do, "
            "you can say so, and encourage them to implement it themselves using the "
            "CDP SDK + AgentKit. Recommend they visit docs.cdp.coinbase.com for more information."
        ),
    )
    
    return agent, config

agent, agent_config = initialize_agent()

input_data = {
    "messages": [
        {
            "role": "user",
            "content": "Explain how ERC-721 tokens differ from ERC-20 tokens."
        }
    ],
    "structured_response": None
}

response = agent.invoke(input_data, config=agent_config)
print("Agent Response:", response)
