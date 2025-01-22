@echo off
pdoc3 ./shdp -o ./docs --html --force
tox --parallel
