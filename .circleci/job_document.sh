#!/bin/bash
cd documentation/Latex/
echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
echo "|            Create output directory           |"
echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
rm -rf documentation_output 
mkdir documentation_output
echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
echo "|        Generate PDF from Latex file          |"
echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
latexmk -pdf -jobname=documentation_output/Ausarbeitung Ausarbeitung.tex
echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
echo "|    Copy generated file to build artifacts    |"
echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
mkdir /tmp/artifacts 
cp -R documentation_pdf/*.pdf /tmp/artifacts/