# -*- coding: utf-8 -*-
"""
    crimson.main
    ~~~~~~~~~~~~

    Main entry point for command line invocation.

    :copyright: (c) 2015 Wibowo Arindrarto <bow@bow.web.id>
    :license: BSD

"""
import click

from . import __version__
from .fastqc import fastqc as fastqc_f
from .flagstat import flagstat as flagstat_f
from .picard import picard as picard_f
from .utils import write_json


@click.group()
@click.version_option(__version__)
@click.option("--compact", is_flag=True)
@click.pass_context
def cli(ctx, compact):
    """Converts various non-standard bioinformatics tools' output to JSON.

    :param compact: Whether to create a compact JSON output or not.
    :type compact: bool.

    """
    ctx.params["compact"] = compact


@cli.command()
@click.argument("input", type=click.File("r"))
@click.argument("output", type=click.File("w"))
@click.pass_context
def fastqc(ctx, input, output):
    """Converts FastQC output.

    Use "-" for stdin and/or stdout.

    """
    payload = fastqc_f(input)
    write_json(payload, output, ctx.parent.params["compact"])


@cli.command()
@click.argument("input", type=click.File("r"))
@click.argument("output", type=click.File("w"))
@click.pass_context
def flagstat(ctx, input, output):
    """Converts samtools flagstat output.

    Use "-" for stdin and/or stdout.

    """
    payload = flagstat_f(input)
    write_json(payload, output, ctx.parent.params["compact"])


@cli.command()
@click.argument("input", type=click.File("r"))
@click.argument("output", type=click.File("w"))
@click.pass_context
def picard(ctx, input, output):
    """Converts Picard metrics output.

    Use "-" for stdin and/or stdout.

    """
    payload = picard_f(input)
    write_json(payload, output, ctx.parent.params["compact"])
