import click


@click.command()
def hello():
    click.secho('Hello World!', fg='red')
    click.secho('Some more text', bg='red', fg='white')
    click.secho('ATTENTION', blink=True, bold=True)

    click.echo('Continue? [yn] ', nl=False)
    c = click.getchar()
    click.echo()
    if c == 'y':
        click.echo('We will go on')
    elif c == 'n':
        click.echo('Abort!')
    else:
        click.echo('Invalid input :(')


if __name__ == '__main__':
    hello()
