from langchain_nvidia_ai_endpoints import ChatNVIDIA
from dotenv import load_dotenv
import os
load_dotenv()

client = ChatNVIDIA(
    model="deepseek-ai/deepseek-r1",
    api_key=os.getenv("NVIDIA_API_KEY"),  # Replace with your NVIDIA API key or use env vars
    temperature=0.6,
    top_p=0.7,
    max_tokens=4096,
)
from rich.console import Console
from rich.panel import Panel
from rich.live import Live
import time

console = Console()

def nvidia_chat(question, answer, explanation):
    # Print user question in a panel
    console.print(Panel(question, title="You", style="cyan", expand=False))
    
    # Show typing indicator
    console.print(Panel.fit("[bold green]DeepSeek AI is thinking...[/bold green]"), end="\r")
    
    query = question + answer + explanation
    full_response = ""
    
    try:
        with Live("", console=console, refresh_per_second=15) as live:
            for chunk in client.stream([{"role": "user", "content": query}]):
                full_response += chunk.content
                live.update(Panel(full_response + "▌", title="DeepSeek AI", style="green"))
                time.sleep(0.01)  # Small delay for smoother streaming effect
            
            # Final update without cursor
            live.update(Panel(full_response, title="DeepSeek AI", style="green", expand=False))
            
    except Exception as e:
        console.print(Panel(f"[red]Error: {str(e)}[/red]", title="Error", style="red"))

