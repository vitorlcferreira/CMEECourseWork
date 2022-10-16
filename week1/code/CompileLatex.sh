#!/bin/bash

# Author: Vitor Ferreira f.ferreira@imperial.ac.uk
# Script: CompileLatex.sh
# Description: This script captures the tex argument provided and convert it to pdf file
# Arguments: none
# Date: Oct 2022

# Get the argument and strip the extension
a=`basename -s .tex $1`

# Initiate the Compilation of .tex file
pdflatex $a.tex
bibtex $a
pdflatex $a.tex
pdflatex $a.tex
mv $a.pdf ../results/
evince ../results/$a.pdf &

# After compilation, files created will be removed
rm *.aux
rm *.log
rm *.bbl
rm *.blg

#exit
