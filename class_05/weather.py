from agents import Agent, Runner, function_tool
from main import config
import os
import requests
from rich.console import Console

console = Console()
api_key = os.getenv("WEATHER_API_KEY")

@function_tool
def get_weather(city: str) -> str:
    """Get detailed weather of a city with error handling."""
    try:
        url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        current = data["current"]
        location = data["location"]

        temp = current["temp_c"]
        condition = current["condition"]["text"]
        humidity = current["humidity"]
        wind = current["wind_kph"]
        feels_like = current["feelslike_c"]
        last_updated = current["last_updated"]

        return (
            f"[bold cyan]Weather for {location['name']}, {location['country']}[/bold cyan]\n"
            f"[bold yellow]Condition:[/bold yellow] {condition}\n"
            f"[bold yellow]Temperature:[/bold yellow] {temp}°C (Feels like {feels_like}°C)\n"
            f"[bold yellow]Humidity:[/bold yellow] {humidity}%\n"
            f"[bold yellow]Wind Speed:[/bold yellow] {wind} kph\n"
            f"[bold yellow]Last Updated:[/bold yellow] {last_updated}"
        )

    except requests.exceptions.RequestException as e:
        return f"[red]Failed to fetch weather data:[/red] {e}"
    except KeyError:
        return "[red]Invalid data format received. Check the city name or API key.[/red]"

# Define the agent
simple_agent = Agent(
    name="Simple Assistant",
    instructions="You are a helpful assistant that gives current weather updates.",
    tools=[get_weather]
)

# Take input from user
user_city = input(">> Enter the city name to check the weather: ")

# Run the agent
res = Runner.run_sync(
    starting_agent=simple_agent,
    input=f"What is the current weather in {user_city}",
    run_config=config
)

# Print the result directly (no panel)
console.print("[bold magenta]🌤️ Weather Report[/bold magenta]\n")
console.print(res.final_output)
