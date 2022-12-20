import click

def input_file():
    master = []

    while ':q' not in master:
        master.append(click.prompt(click.style('file_', fg='green')))
    master = master[:-1]

    return master