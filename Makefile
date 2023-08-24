#
# Makefile for rpapol manuscript
#


texfiles:= presentation.tex
bibfiles:= presentation.bib

all: presentation.pdf

presentation.pdf: presentation.bbl
	pdflatex presentation

rpapol.bbl: $(texfiles) $(bibfiles)
	@export BSTINPUTS=$(BSTINPUTS) BIBINPUTS=$(BIBINPUTS)
	pdflatex presentation
	biber presentation
	pdflatex presentation

.PHONY: clean
clean:
	-$(RM) -f *.aux *.log *.idx *.ilg *.out *.blg
	-$(RM) presentationNotes.bib tmp.bib

.PHONY: realclean
realclean: clean
	-$(RM) -f *.dvi *.ps *.pdf *.html *.png *.4ct *.4tc *.css *.idv *.lg *.tmp *.xref *.bbl *.ind *.toc
