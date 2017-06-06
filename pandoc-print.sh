#!/bin/bash

pandoc -t revealjs slides.md -f markdown+pipe_tables --slide-level=3 -s -o print.html \
    -V theme=white \
#    -V parallaxBackgroundImage="XW17-empty.jpg" \
#    -V parallaxBackgroundSize="1280px 960px" \
#    -V parrallaxBackgroundHorizontal="0" \
#    -V parrallaxBackgroundVertical="0"
# removed background and renamed HTML file for priting slides
#
