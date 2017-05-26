#!/bin/bash

pandoc -t revealjs notes/all.md -f markdown+pipe_tables --slide-level=3 -s -o index.html \
    -V theme=white \
    -V parallaxBackgroundImage="XW16-Empty.jpg" \
    -V parallaxBackgroundSize="1440px 900px" \
    -V parrallaxBackgroundHorizontal="0" \
    -V parrallaxBackgroundVertical="0"

