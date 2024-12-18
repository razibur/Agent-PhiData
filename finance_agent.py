from phi.agent import Agent
## from phi.model.groq import Groq
from phi.model.openai import OpenAIChat
from phi.tools.yfinance import YFinanceTools
from dotenv import load_dotenv


def get_company_symbol(company: str) -> str:
    """Use this function to get the symbol for a company

    Args:
      company (str): The name of the company.

    Returns:
      str: The symbol for the company.
    """
    symbols = {
        "SohelData": "MSFT",
        "Infosys": "INFY",
        "Tesla": "TSLA",
        "Amazon": "AMZN"
    }
    return symbols.get(company, "Unknown")


load_dotenv()

agent = Agent(
    # model=Groq(id="llama-3.3-70b-versatile"),
    model= OpenAIChat(id="gpt-4o"),
    tools=[YFinanceTools(
        stock_price=True, analyst_recommendations=True, stock_fundamentals=True), get_company_symbol],
    show_tool_calls=True,
    markdown=True,
    instructions=["Use tables to display data.",
                  "If you don't know the company symbol, please use get_company_symbol tool, even if it not a public company"],
    debug_mode=True
)

agent.print_response(
    "Summarize and compare analyst recommendations and fundamentals for TSLA and SohelData")
