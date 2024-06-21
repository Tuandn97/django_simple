from langchain_community.tools import WikipediaQueryRun, tool
from langchain_community.utilities import WikipediaAPIWrapper

# wikipedia = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())

# tools = [wikipedia]

from langchain.pydantic_v1 import BaseModel, Field
from langchain.tools import BaseTool, StructuredTool, tool

class WikipediaInput(BaseModel):
    query: str = Field(description="should be a search query")

@tool("get_info_from_wikipedia", args_schema=WikipediaInput)
def get_info_from_wikipedia(query: str) -> str:
    """Get information from Wikipedia."""
    output = WikipediaAPIWrapper().run(query)
    return output

tools = [get_info_from_wikipedia]