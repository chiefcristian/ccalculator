import click

from app.model import calculator

@click.group()
@click.pass_context
def calc(ctx: click.context):
    """"A simple calculator"""
    ctx.obj={"calculator_object": calculator()}

