#!/bin/bash
cd documentation/Latex/
rm -rf documentation_output 
mkdir documentation_output
latexmk -pdf -jobname=documentation_output/Ausarbeitung Ausarbeitung.tex
# Move output to Artifacts Folder
mkdir /tmp/artifacts 
cp -R documentation_pdf/*.pdf /tmp/artifacts/