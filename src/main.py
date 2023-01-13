import click
from src.helper.click import ClickHelper
from src.service.modules.tkinter import AddTkinterClass
from src.service.update.update import UpdateApp
from src.service.user.user import NewUser

AddTkinterClass()
UpdateApp()
NewUser()


@ click.command(short_help='create or edit a file', context_settings=dict(help_option_names=['-h', '--help']))
@ click.option('-t', '--title', default=None, help='Select a file by title')
@ click.option('-l', '--list', default=None, help='List all files', is_flag=True)
@ click.option('-d', 'command',  help='Selete a file',  flag_value='d')
@ click.option('-i', 'command',  help='App version and install path',  flag_value='i')
@ click.option('-b', 'command',  help='Backup all files', flag_value='b')
def main(title, list, command):
    """codeswap:

    \b
    create or edit your files.
    delete your files with the '-d' command.
    you can use the '-t' option to input the file title through the terminal.


    """
    if list:
        ClickHelper.list_files()

    match command:

        case 'd': ClickHelper.delete(title)

        case 'i': ClickHelper.info()

        case 'b': ClickHelper.backup()

        case _: ClickHelper.default(title)
