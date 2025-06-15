import requests
from rich.console import Console

res = requests.get("https://zenquotes.io/api/random")
console = Console()

if res.status_code == 200:
    data = res.json()
else:
    print("There was an error, code:", res.status_code)

console.print(f":sparkles:[purple]{data[0]['q']}[/purple]:sparkles:", " - ", end = " ")
console.print(f"[green]{data[0]['a']}[/green]")
