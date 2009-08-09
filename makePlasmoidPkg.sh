#!/bin/bash
zip  -x ".git/*" -x ".project" -x ".settings/*" -x ".pydevproject"  -x "*/*.pyc" -x ".gitignore" -x "makePlasmoidPkg.sh"  -r ../plasma_pyweather.plasmoid .
