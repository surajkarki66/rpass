#!/usr/bin/env python

import os
import click
import pyperclip


from rpass.utils.create_password import generate_password


CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])


@click.command(context_settings=CONTEXT_SETTINGS)
@click.version_option(version="0.0.2")
@click.option(
    "-l", "--length", type=int, default=12, help="Password length(default: 12)"
)
@click.option("-ns", "--no-symbols", is_flag=True, help="Do not use symbols")
@click.option("-nd", "--no-digits", is_flag=True, help="Do not use digits")
@click.option("--upper", is_flag=True, help="Only use upper case letters")
@click.option("--lower", is_flag=True, help="Only use lower case letters")
def main(**kwargs):
    """Welcome to rpass! A strong random password generator cli utility tool!"""
    password = generate_password(**kwargs)
    click.echo(click.style(f"Your password is {password}", bold=True))
    pyperclip.copy(password)
    click.echo(click.style("Saved! to clipboard", fg="green"))
    pass


if __name__ == "__main__":
    main()
