import click

def decision() -> str:
    while True:
        try:
            click.clear()
            click.echo('a_ add | r_ read | e_ edit | d_ delete')
            choice = input("_").lower()

            if choice != 'a' and choice != 'r' and choice != 'q' and choice != 'e' and choice != 'd':
                raise ValueError

            return choice

        except ValueError:
            click.secho('error!', bg='red', fg='white')