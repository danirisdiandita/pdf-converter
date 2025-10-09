#!/bin/bash

pandoc --pdf-engine=xelatex --include-in-header=/data/header.tex $1 -o $2
