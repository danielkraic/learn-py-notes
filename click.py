import click
import os


def validate_rolls(ctx, param, value):
    try:
        rolls, dice = map(int, value.split('d', 2))
        return dice, rolls
    except ValueError:
        raise click.BadParameter('rolls need to be in format NdM')


@click.command()
@click.option('--n', default=1)
@click.option('--pos', nargs=2, type=float)
#@click.option('--item', type=(str, int))
@click.option('--item', nargs=2, type=click.Tuple([str, int]))
@click.option('-v', '--verbose', count=True)
#@click.option('--shout/--no-shout', default=False)
@click.option('--shout', is_flag=True)
@click.option('--message', '-m', multiple=True)
@click.option('--upper', 'transformation', flag_value='upper', default=True)
@click.option('--lower', 'transformation', flag_value='lower')
@click.option('--hash-type', type=click.Choice(['md5', 'sha1']))
@click.option('--count', type=click.IntRange(0, 20, clamp=True))
@click.option('--digit', type=click.IntRange(0, 10))
#@click.option('--name', prompt=True)
@click.option('--name', prompt='Your name please')
#@click.option('--password', prompt=True, hide_input=True, confirmation_prompt=True)
@click.password_option()
@click.option('--username', prompt=True, default=lambda: os.environ.get('USER', ''))
@click.confirmation_option(help='Are you sure you want to drop the db?')
@click.option('--rolls', callback=validate_rolls, default='1d6')
#@click.argument('name')
@click.argument('src', nargs=-1)
@click.argument('dst', nargs=1)
@click.argument('input', type=click.File('rb'))
@click.argument('output', type=click.File('wb'))
@click.argument('f', type=click.Path(exists=True))
@click.argument('src2', envvar='SRC', type=click.File('r'))
def initdb(n, pos, item, verbose, shout, message, transformation, hash_type, count, digit, name, username, rolls,
           src, dest, input, output, f, src2):

    click.echo('initdb')

    print(n, pos, item, verbose, shout, message, transformation, hash_type, count, digit, name, username, rolls,
          src, dest, input, output, f, src2)


if __name__ == '__main__':
    initdb()

# @click.group()
# def cli():
#     click.echo('cli')
#
#
# @cli.command()
# def initdb():
#     click.echo('initdb')
#
#
# @cli.command()
# def dropdb():
#     click.echo('dropdb')
#
#
# if __name__ == '__main__':
#     cli()
