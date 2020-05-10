from console import Console

console = None

def start_console(idx):
    console = Console(idx)
    console.run()

start_console(0)