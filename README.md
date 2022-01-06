# Joelle Maslak\'s Resume

Continue to [a generated version of my resume](resume.pdf)

# Job Search Status

I am not currently looking for new employment. However, if you have a
particularly exciting opportunity that you believe I might be interested
in, I'm open to hearing about the opportunity.

# About the Resume Generator

To compile the resume, you must have LaTeX installed with many other
modules. I recommend the TeX-live distribution.

In addition, two fonts are used, Adobe Jenson Pro and Malcom, both of
which are commercial and thus not included in this file.  To compile the
resume, you will either need to legally obtain those fonts or modify the
[JTMresume.sty](https://github.com/jmaslak/resume/blob/main/JTMresume.sty)
file to use fonts installed on your machine.

To build the resume on Linux, simply use make from the command line.

The resume generator will utilize the
[references.bib](https://github.com/jmaslak/resume/blob/main/references.bib) file for
publication, patent, and conference information. This is a standard
biblatex references file. On my machine, the makefile will regenerate this
whenever my master reference file changes, but the generator is fully
functional without that.

The reference file regeneration uses a custom script, [extract-by-tags.py](https://github.com/jmaslak/resume/blob/main/extract-by-tags.py) to
extract references from my master file (my master file contains
references to docs I cite in other LaTeX documents beyond what is
relevant to my resume). I use three tags: mypresentations, mypatent, and
mypub in my master file to tag my own works.  These tags are also
referenced in the LaTeX sources. The dependencies for this extraction
script are listed in
[requirements.txt](https://github.com/jmaslak/resume/blob/requirements.txt)
and are installable via `pip`. Assuming you have `pip` installed, you
can install the dependencies with `pip install -r requirements.txt`.

Unit tests of the Python code (to extract references) and do basic
integration checks on the resume output can be run with `make test`.
However, before you run the tests, ensure you've installed the test
dependencies (in addition to the standard dependencies as described
above), using `pip install -r requirements-test.txt`. Then you can run
`make test` to verify the generation of the resume.

Finally, most of the text for the resume, beyond header information and
dynamic content is located in the
[sections/](https://github.com/jmaslak/resume/tree/main/sections) directory.
The [resume.tex](https://github.com/jmaslak/resume/blob/main/resume.tex) file
in the main directory is the master LaTeX file that
references these files and the style class,
[JTMresume.sty](https://github.com/jmaslak/resume/blob/main/JTMresume.sty).

# Credit

I used Timmy Chan's
[excellent resume template](https://www.overleaf.com/latex/templates/data-science-tech-resume-template/zcdmpfxrzjhv)
as a starting point for my resume. I modified this template
significantly to include patent, conference presentation, and publication
information, as well as styling and functionality changes. The LaTeX
code borrowed heavily from this template, although it was modified
extensively.

All python and Makefile code was created by Joelle Maslak.

# License

This work is licensed under the Creative Commons CC BY 4.0 License - see
the included
[LICENSE](https://github.com/jmaslak/resume/blob/main/LICENSE) file or
the summary at the [Creative Commons](https://creativecommons.org/licenses/by/4.0/)
site.

This is an attribution-required license, so you are welcome to
incorporate this into your own works, but you are required to credit
the creator of the template this is based upon, Timmy Chan, and also
Joelle Maslak for her changes to these templates.

