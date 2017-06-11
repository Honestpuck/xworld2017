#!/bin/bash

pandoc -t revealjs slides.md -f markdown+pipe_tables --slide-level=3 -s -o index.html \
    -V theme=white \
    -V parallaxBackgroundImage="XW17-Empty.png" \
    -V parallaxBackgroundSize="1280px 960px" \
    -V parrallaxBackgroundHorizontal="0" \
    -V parrallaxBackgroundVertical="0"

