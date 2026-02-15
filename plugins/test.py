import click
from sereto.logging import logger


@click.command()
def test():
    """Test plugin."""
    logger.success("Test plugin executed.")


def register_commands(cli: click.Group):
    cli.add_command(test)
