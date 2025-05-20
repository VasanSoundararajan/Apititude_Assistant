from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
from rich.live import Live
import time

console = Console()

def pretty_print_chat():
    chat_history = []

    while True:
        user_input = console.input("[bold cyan]You:[/bold cyan] ").strip()
        if user_input.lower() == "exit":
            console.print("[bold red]Exiting chat.[/bold red]")
            break

        # Add user message
        chat_history.append(("user", user_input))
        console.print(Panel(user_input, title="You", style="cyan", expand=False))

        # AI response streaming simulation
        console.print(Panel.fit("[bold green]DeepSeek AI is typing...[/bold green]"), end="\r")

        full_response = ""
        # Replace this with your real client streaming code below
        # For demonstration, simulate streaming:
        simulated_response = "This is a simulated response from DeepSeek AI. Streaming chunk by chunk."
        with Live("", console=console, refresh_per_second=4) as live:
            for i in range(len(simulated_response)):
                full_response += simulated_response[i]
                live.update(Panel(full_response + "▌", title="DeepSeek AI", style="green"))
                time.sleep(0.05)

        # Print final response without cursor
        console.print(Panel(full_response, title="DeepSeek AI", style="green", expand=False))

        # Add AI response to chat history
        chat_history.append(("assistant", full_response))


if __name__ == "__main__":
    pretty_print_chat()
