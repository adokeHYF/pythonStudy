import click
# @click.command()
# @click.option('--count', default=1, help='Number of greetings.')
# @click.option('--name', prompt='Your name', help='The person to greet.')
# def hello(count, name):
#     """Simple program that greets NAME for a total of COUNT times."""
#     for x in range(count):
#         click.echo('Hello %s!' % name)
#
#
# if __name__ == '__main__':
#     hello()


@click.group()
def cli():
    pass


@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name', help='The person to greet.')
def initdb(count, name):
    click.echo('Initialized the database')
    for x in range(count, name):
        click.echo('Hello %s!' % name)


@click.command()
def dropdb():
    click.echo('Dropped the database')


cli.add_command(initdb)
cli.add_command(dropdb)

if __name__ == '__main__':
    cli()
