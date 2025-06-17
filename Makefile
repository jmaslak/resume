PROJECT=resume
SECTIONS=sections/service.tex sections/education.tex sections/experience.tex sections/_header.tex sections/objective.tex sections/skills.tex sections/publications.tex sections/patents.tex sections/presentations.tex
LATEX=lualatex
BIBLIOGRAPHIES=$${HOME}/references.bib
IMAGES=
STYLES=JTMresume.sty
BIBER=biber
LATEXFLAGS=
BIBFILE=$${HOME}/references.bib
TAGS=mypresentations mypatent mypub
TAG_EXTRACT_OPTIONS=-x notresume
PYTESTARGS="-v"

default : all

all : $(PROJECT).pdf

.PHONY: clean
clean : 
	rm -f *.p1 *.p2 *.bbl *.bcf *.log *.blg *.xml *.aux *.bak *.bak[0-9]* sections/*.bak sections/*.bak[0-9]* sections/*.log *.dvi *.out *.pdf
	rm -rf _minted-$(PROJECT)

.PHONY: test
test : $(PROJECT).pdf references.bib
	pytest $(PYTESTARGS)

indent :
	for i in *.tex sections/*.tex ; do latexindent -s -sl -w "$$i" ; done

spell :
	for f in README.md $(PROJECT).tex $(SECTIONS) ; do aspell check $$f ; done

%.pdf: %.p2
	$(LATEX) $(LATEXFLAGS) $(basename $<).tex

%.p2: %.bbl
	$(LATEX) $(LATEXFLAGS) --draftmode $(basename $<).tex && touch $(basename $<).p2

%.bbl: %.p1 $(BIBLIOGRAPHIES)
	$(BIBER) $(basename $<).bcf

%.p1: %.tex references.bib $(STYLES) $(IMAGES) $(SECTIONS)
	$(LATEX) $(LATEXFLAGS) --draftmode $< && touch $(basename $<).p1

references.bib: $(BIBFILE)
	ruff check extract_by_tags.py
	python3 extract_by_tags.py --source "$(BIBFILE)" --output references.bib $(TAG_EXTRACT_OPTIONS) $(TAGS)

$(BIBFILE):
	echo "The bib file source does not exist"

.PRECIOUS: %.p1 %.p2 %.bbl %.bcf references.bib
