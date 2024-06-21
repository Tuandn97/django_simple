# create llm
# create prompt
# tool

from chatbot.chat_service.simple_chat_bot import load_llm
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from chatbot.chat_service.tools import tools
from langchain.agents import create_tool_calling_agent, AgentExecutor

system_prompt = ("You are a helpful assistant. You can help me with information in Wikipedia."
                 "You can call tool function 'get_info_from_wikipedia' to get information from Wikipedia with input: 'get_info_from_wikipedia('search_term').")

prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        MessagesPlaceholder(variable_name="chat_history"),
        ("user", "{input}"), 
        MessagesPlaceholder(variable_name="agent_scratchpad")
    ])
llm = load_llm(provider="google")
agent = create_tool_calling_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
output = agent_executor.invoke({"input":"Search for me a manga named 'Hunter X hunter'", 'chat_history':[]})
print (output)