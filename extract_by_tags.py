#!/usr/bin/env python3

#
# Copyright (C) 2022 Joelle Maslak
# All Rights Reserved - See License
#

import argparse
import logging

import bibtexparser

LOG = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(levelname)8s [%(asctime)s] %(message)s')


def get_args():
    """Process command line arguments."""
    parser = argparse.ArgumentParser(description="Extract bibtex entries by keyword")
    parser.add_argument('--source', '-s', required=True, help='Source bibtex file to read')
    parser.add_argument('--output',
                        '-o',
                        required=True,
                        help='Destination bibtex to create/overwrite')
    parser.add_argument('keyword', nargs='+', help='Keywords to match to records for extraction')
    args = parser.parse_args()

    return args


def read_bibtex(args):
    """Read the bibtex file."""
    parser = bibtexparser.bparser.BibTexParser(common_strings=True)
    parser.ignore_nonstandard_types = False
    parser.homogenise_fields = False

    LOG.info("Reading bibtex input file")
    with open(args.source) as bibtex_file:
        db = bibtexparser.load(bibtex_file, parser)

    return db


def filter_by_keywords(args, db):
    """Creates a new bibtex database that consists only of keywords in args."""
    outdb = bibtexparser.bibdatabase.BibDatabase()

    LOG.info("Scanning bibtex data for keywords")
    for entry in db.entries:
        if 'keywords' in entry:
            kwords = entry['keywords'].split(',')  # Simplistic, but works for my input sources
            for word in args.keyword:
                if word in kwords:
                    outdb.entries.append(entry)
                    break

    return outdb


def main():
    """Extract bibtex entries by keyword."""
    LOG.info("Starting reference extraction")
    args = get_args()

    db = read_bibtex(args)
    outdb = filter_by_keywords(args, db)

    LOG.info("Writing bibtex output file")
    with open(args.output, mode='w') as bibtex_out:
        bibtexparser.dump(outdb, bibtex_out)

    LOG.info("Exiting normally")


if __name__ == '__main__':
    main()
