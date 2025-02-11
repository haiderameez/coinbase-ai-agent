# Coinbase AI Agent
This repository demonstrates how to initialize and run an on-chain interaction agent using an open-source language model (Meta-Llama 3.1 8B) combined with the Coinbase Developer Platform (CDP) AgentKit. The agent leverages various toolkits and utilities to interact with on-chain tools, process user input, and provide insightful responses related to blockchain topics.

## Usage Guide

### 1. Download the Repository using
```bash
git clone git clone https://github.com/yourusername/cdp-agentkit-chatbot-example.git
```

### 2. Install all the dependencies using the following line of code:
```python
pip install -r requirements.txt
```

### 3. Environment Variables
- Create a `.env` file in the root directory and set the following environment variables with your credentials:
- Go to https://docs.cdp.coinbase.com/cdp-apis/docs/welcome and get API keys.
- Download the `config.json` file and create `.env` file.
- Store these two in a `.env` file
```.env

CDP_API_KEY_NAME=your_cdp_api_key_name
CDP_API_KEY_PRIVATE_KEY=your_cdp_api_private_key
NETWORK_ID=your_network_id

```

### 4. Setting up Meta-Llama 3.2 1B
- Go to https://huggingface.co/meta-llama/Llama-3.2-1B.
- If permission to use the model is not allowed, fill up the consent form.
- Get `access_token` from Hugging Face.
- Run the following code,
  
  ```bash
  huggingface-cli login access_token
  ```
  
### 5. Understanding the Code Structure   

- Model & Tokenizer Setup:
  The code uses Hugging Face’s `transformers` library to load the `Meta-Llama 3.2 1B` model and its tokenizer.

- CDP AgentKit Integration:
  The `CdpAgentkitWrapper` is initialized using your API credentials to establish a connection with the CDP ecosystem.
  The `CdpToolkit` extracts a set of tools that the agent can use for on-chain interactions.

- Agent Configuration:
  The agent is created using `create_react_agent` from the `langgraph` library, with a specific `state_modifier` message that configures its on-chain behavior. The configuration includes thread          identifiers and checkpoint settings for memory persistence.

- Agent Invocation:
  The agent receives an input message (e.g., explaining how ERC-721 tokens differ from ERC-20 tokens) and processes it using its integrated tools to generate a response.


### 6. Runnning the Agent
- Run the main script using
  
  ```bash
  python main.py
  ```
- This will return an output from the agent.
