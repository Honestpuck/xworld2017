# xworld2017

A repo for my workshop at X World 2017 "Charming The Snake"

It contains a bunch of example scripts and the Markdown source and
reveal.js slideshow for the presentation.

The reveal.js slideshow is created using [pandoc](http://pandoc.org).
The exact pandoc command can be found in `pandoc.sh`. I have modified
the `white.css` reveal.js template to hopefully increase readability 
and use my favourite code font.

While running the slideshow pressing `S` will open a speaker view where 
you can read the notes. For other hints visit the 
[reveal.js](http://lab.hakim.se/reveal-js/#/) home page.

The `slides.pdf` file is generated by running the slideshow in  a
browser with the query `?print-pdf` and then saving to PDF from the
print dialog. As the background doesn't print properly in the normal
slideshow the special version `print.html` has been created with the
command line `pandoc-print.sh` that doesn't include the background. So
to create the PDF the URL is
`http://localhost:8000/print.html?print-pdf` if you run 
`python -mbSimpleHTTPServer` in this directory. (It looks strange in Safari 
but saves out the PDF fine.)

The `slides_notes.pdf` file is generated using `Marked 2` and 
`Export as, Save PDF`.

| File                 | Description                                     |
| -------------------- | ----------------------------------------------- |
| Input-Font.zip       | The Input font - used in presentation           |
| PYTHONPATH.txt       | Line to add to bash profile for PYTHON          |
| README.md            | This file                                       |
| XW17-Empty.png       | Background for slides                           |
| index.html           | The presentation slides                         |
| pandoc.sh            | command line to run Pandoc and create slideshow |
| pandoc-print.sh      | command line to create `print.html`             |
| print.html           | special edition of slides for creating PDF      |
| reveal.js/*          | Slideshow software                              |
| slides.md            | The Markdown source for the slides              |
| slides.pdf           | a PDF of the presentation slides                |
| slides_notes.pdf     | a PDF of the slides and my notes                |
| solarized.zip        | My favourite theme for Terminal                 |
