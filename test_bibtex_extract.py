#!/usr/bin/env python3

#
# Copyright (C) 2022 Joelle Maslak
# All Rights Reserved - See License
#

import extract_by_tags

#
# Some unit tests for the bibtex extractor
#


def args():
    """Do nothing but function as holder for attributes."""
    pass


args.source = "references.bib"
db = extract_by_tags.read_bibtex(args)


def test_read_has_entries():
    assert len(db.entries) > 5


def test_filter_one_keyword():
    args.keyword = ['mypatent']
    newdb = extract_by_tags.filter_by_keywords(args, db)

    assert len(newdb.entries) > 2
    assert len(newdb.entries) < len(db.entries)


def test_filter_two_keywords():
    args.keyword = ['mypatent']
    newdb1 = extract_by_tags.filter_by_keywords(args, db)

    args.keyword = ['mypatent', 'mypub']
    newdb2 = extract_by_tags.filter_by_keywords(args, db)

    assert len(newdb2.entries) > len(newdb1.entries)
    assert len(newdb2.entries) < len(db.entries)


def test_filter_all_keywords():
    args.keyword = ['mypatent', 'mypub', 'mypresentations']
    newdb = extract_by_tags.filter_by_keywords(args, db)

    assert len(db.entries) == len(newdb.entries)


def test_filter_all_keywords():
    args.keyword = ['mypatent', 'mypub', 'mypresentations']
    args.exclude = 'notresume'
    newdb_no_excludes = extract_by_tags.filter_by_keywords(args, db)
    newdb_with_excludes = extract_by_tags.filter_by_excludes(args, newdb_no_excludes)
    double_execution = extract_by_tags.filter_by_excludes(args, newdb_with_excludes)

    assert len(newdb_no_excludes.entries) > len(newdb_with_excludes.entries)
    assert len(newdb_with_excludes.entries) == len(double_execution.entries)
