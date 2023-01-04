
import click

from src.service.str_to_int import str_to_int


def login():
    while True:
        try:
            user = click.prompt(click.style('password_', fg='red'),
                       hide_input=True, prompt_suffix='')

            
            if len(user) < 2:
                raise ValueError

            user = str_to_int(user)

            return int(user)
        except ValueError:
            click.secho('error!', bg='red', fg='white')
            click.echo('must be at least a 2 digits password_')
