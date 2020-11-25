#!/usr/bin/env bash
# Running:
#    . ./genpython.sh
# Note: need antlr4.8  to run this!
# see: http://www.antlr.org/download.html for details
cp ../../grammar/ShExDoc.g4 .
antlr4 -Dlanguage=Python3 -package parser -o ../pyshexc/parser -no-listener -visitor ShExDoc.g4
rm ShExDoc.g4

