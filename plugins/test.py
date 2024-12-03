import click


@click.command()
def test():
    """Test plugin."""
    click.echo("Test plugin executed")


def register_commands(cli: click.Group):
    cli.add_command(test)
