### PyObjC

``` python
from AppKit import NSScreen

width = NSScreen.mainScreen().frame().size.width
height = NSScreen.mainScreen().frame().size.height

print height, width
900.0 1440.0
```

<div class="notes">
PyObjC is a bridge between Python and Objective-C that allows you to do some
powerful things in Python without running any other software.
</div>