import getpass
import click


def login():
    while True:
        try:

            user = int(getpass.getpass(click.style('password_', fg='red')))

            if len(str(user)) < 2:
                raise ValueError

            return user
        except ValueError:
            click.secho('error!', bg='red', fg='white')
            click.echo('must be at leat a 2 digits number_')

