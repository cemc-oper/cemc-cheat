# coding=utf-8
import click
from pathlib import Path

from cemc_cheat.render import MarkdownViewer


@click.command()
@click.argument('topic', default=None, required=False)
def cli(topic):
    """
    A command line tool for NWPC Cheat Sheet.
    """
    if topic is None:
        click.echo(click.get_current_context().get_help())
        click.get_current_context().exit()

    sheets_dir = Path(Path(__file__).parent, './sheets')
    topic_file_path = Path(sheets_dir, f"{topic}.md")

    if topic_file_path.exists():
        with open(topic_file_path, 'r', encoding='utf-8') as topic_file:
            topic_content = topic_file.read()
            app = MarkdownViewer(topic_content)
            app.run()
    else:
        click.echo('Unknown topic.')


if __name__ == "__main__":
    cli()
