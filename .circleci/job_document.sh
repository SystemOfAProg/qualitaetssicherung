#!/bin/bash
cd documentation/Latex/
rm -rf documentation_output 
mkdir documentation_output
pdflatex --output-directory documentation_output Ausarbeitung.tex
# Move output to Artifacts Folder
mkdir /tmp/artifacts 
cp -R documentation_pdf/*.pdf /tmp/artifacts/