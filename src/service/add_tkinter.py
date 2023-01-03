import subprocess
import platform
import click

def add_tkinter():
    try:
        import tkinter

    except:
        click.secho('Error!', bg='red', fg='black')
        click.secho('Tkinter module required', fg='red')
        click.secho('trying to solve automatically:', fg='red')

        if platform.system() == 'Linux':
            subprocess.run(['sudo','apt', 'install', 'python3-tk'])

        elif platform.system() == 'Windows':
            click.secho('windows:', fg='red')

        else:
            click.secho(':', fg='red')

            
    