import click


# 单个click 命令
@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name', help='The person to greet.')
def hello(count, name):
    """ single click test """  # 命令行运行的介绍内容
    for x in range(count):
        click.echo('Hello %s!' % name)


# click 命令组
@click.group(help="multiple click test")
def cli():
    pass


@cli.command(help='初始化数据库')
@click.option('--db_name', help='数据库名称', type=click.Choice(['db1', 'db2']))
def initdb(db_name):
    # type --help 显示的可选项如果选别的就会出错
    if db_name:
        click.echo(f'初始化数据库 {db_name}')
    else:
        click.echo('请输入数据库名称')


@cli.command(help='删除数据库')
@click.option('--db_name', help='数据库名称')
def dropdb(db_name):
    if db_name:
        click.echo(f'Droped the database {db_name}')
    else:
        click.echo('跑路吧')


@cli.group(help="表操作")
def table():
    """ 数据库表操作 """
    pass


@table.command(help="创建表")
@click.option('--db_name', help='数据库名称')
@click.option('--table_name', help='表名称')
def create(db_name, table_name):
    pass


@table.command(help="删除表")
@click.option('--db_name', help='数据库名称')
@click.option('--table_name', help='表名称')
def delete(db_name, table_name):
    pass


@table.command(help="修改表")
@click.option('--db_name', help='数据库名称')
@click.option('--table_name', help='表名称')
def change(db_name, table_name):
    pass


@table.command("check", help="查看表")
@click.option('--db_name', help='数据库名称')
@click.option('--table_name', help='表名称')
def get(db_name, table_name):
    pass


if __name__ == '__main__':
    # hello()
    cli()
