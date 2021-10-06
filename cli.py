import os
import click


# This script is use only if one wants to call the main functions in a command prompt
def cli():
    pass

@click.command()
@click.option('-s', '--shortcut', help='name', required=True)


def model(shortcut):

    ....

@click.command()
@click.option('-s', '--shortcut', help='name', required=True)


cli.add_command(model)


if __name__ == "__main__":
    cli()