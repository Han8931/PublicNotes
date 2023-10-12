# Introduction

## Setup 

```sh
pip install langchain
pip install openai
```

Put your OpenAI API Key... 
```python
import os
os.environ["OPENAI_API_KEY"] = "your_key"
```

# Building A Language Model Application

#### LLMs: Get Predictions from a Language model

```python
from langchain.llms import OpenAI

llm = OpenAI(temperature=0.9) # Randomness ~1 / deteministic ~0
text = "What are 5 vacation destinations for someone who likes to eat pasta?"
print(llm(text))
```

#### Prompt Templates: Manage Prompts for LLMs

```python
from langchain.prompts import PromptTemplate

prompt = PromptTemplate(
	input_variables=["food"],
	template="What are 5 vacation destinations for someone who likes to eat {food}?"
						
)

print(prompt.format(food="dessert"))
print(llm(prompt.format(food="dessert")))
```

#### Chains: Combine LLMs and Prompts in Multi-Step Workflows
```python
from langchain.prompts import PromptTemplate 
from langchain.llms import OpenAI
from langchain.chains import LLMChain

llm = OpenAI(temperature=0.9)
prompt = PromptTemplate(
	input_variables=["food"],
	template="What are 5 vacation destinations for someone who likes to eat {food}?"
)

chain = LLMChain(llm=llm, prompt=prompt)
print(chain.run("fruit"))
```

#### Agents: Dynamically Call Chains based on User Input

```sh
pip install  google-search-results
```

```python
from langchain.agents import load_tools, initialize_agent
from langchain.llms import OpenAI

llm = OpenAI(temperature=0.9)

tools = load_tools(["serpapi", "llm-math"], llm=llm)

agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)

agent.run("Who is the current leader of Japan? What is the largest prime number that is smaller than their age?")
```

#### Memory: Add State to Chains and Agents

```python
from langchain import OpenAI, ConversationChain

llm = OpenAI(template=0.9)
conversation = ConversationChain(llm=llm, verbose=True)
conversation.predict(input="Hi there!")
conversation.predict(input="I'm doing well Just having a conversation with an AI.")
```


