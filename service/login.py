import getpass
import click

def login():
    while True:
        try:
            click.clear()
            click.echo('pls insert your password_')
            click.echo('if u are a new user just create one_')
            click.echo('must be at leat a 2 digits number_')
            user = int(getpass.getpass(click.style('password_', fg='red')))

            if len(str(user)) < 2:
                raise ValueError

            return user
        except ValueError:
            click.secho('error!', bg='red', fg='white')
