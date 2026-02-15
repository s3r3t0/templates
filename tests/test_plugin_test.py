from unittest.mock import patch

import click
from click.testing import CliRunner

from plugins.test import register_commands
from plugins.test import test as cmd_test


class TestTestCommand:
    """Tests for the test plugin Click command."""

    def test_command_exists(self):
        """The `test` object is a Click command."""
        assert isinstance(cmd_test, click.Command)

    def test_command_name(self):
        """The command is named 'test'."""
        assert cmd_test.name == "test"

    def test_command_help_text(self):
        """The command has the expected help string."""
        assert cmd_test.help == "Test plugin."

    def test_register_commands_adds_test(self):
        """register_commands adds the test command to the CLI group."""
        cli = click.Group()
        register_commands(cli)
        assert "test" in cli.commands
        assert cli.commands["test"] is cmd_test

    @patch("plugins.test.logger")
    def test_invocation_succeeds(self, mock_logger):
        """Invoking the command exits with code 0."""
        runner = CliRunner()
        result = runner.invoke(cmd_test)
        assert result.exit_code == 0

    @patch("plugins.test.logger")
    def test_invocation_logs_success(self, mock_logger):
        """Invoking the command calls logger.success with the expected message."""
        runner = CliRunner()
        runner.invoke(cmd_test)
        mock_logger.success.assert_called_once_with("Test plugin executed.")

    @patch("plugins.test.logger")
    def test_invocation_via_group(self, mock_logger):
        """The command works when invoked through a parent CLI group."""
        cli = click.Group()
        register_commands(cli)
        runner = CliRunner()
        result = runner.invoke(cli, ["test"])
        assert result.exit_code == 0
        mock_logger.success.assert_called_once_with("Test plugin executed.")

    def test_help_flag(self):
        """The --help flag prints help and exits cleanly."""
        runner = CliRunner()
        result = runner.invoke(cmd_test, ["--help"])
        assert result.exit_code == 0
        assert "Test plugin." in result.output
