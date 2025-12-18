import typer
app = typer.Typer()

@app.command()
def hello(name:str):
    print(f"Hello {name}")

@app.command()
def goodbye(name:str,formal :bool =False):
    print(f"goodbye {name}")


if __name__ == "__main__":
    app()