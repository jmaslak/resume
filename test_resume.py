#!/usr/bin/env python3

#
# Copyright (C) 2022 Joelle Maslak
# All Rights Reserved - See License
#

import pypdf

#
# Some unit tests for the resume
#

f = open("resume.pdf", "rb")
pdf = pypdf.PdfReader(f)


def outline_titles():
    """Pull the titles out of the outline."""
    ret = []
    othercount = 0
    for section in pdf.outline:
        if type(section) is list:
            for eles in section:
                ret.append(f"OtherSection_{othercount}")
                othercount += 1
        else:
            ret.append(section["/Title"])

    return set(ret)


def test_isMultipage():
    """Test that the resume is >= 2 pages long."""
    assert len(pdf.pages) >= 2


def test_hasSections():
    """Test that key sections are present."""
    titles = outline_titles()

    assert "Skills" in titles
    assert "Technical Experience" in titles
    assert "Education" in titles
    assert "Service" in titles
    assert "Publications" in titles
    assert "Conference Presentations" in titles
    assert "OtherSection_1" in titles  # For experience elements, second one.
