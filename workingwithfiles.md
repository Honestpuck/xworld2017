#### Joining Paths

```
import os
silverlight_plugin_path = os.path.join("/", \
    "Library", \
    "Internet Plug-Ins", \
    "Silverlight.plugin")
print(silverlight_plugin_path)
/Library/Internet Plug-Ins/Silverlight.plugin
```

#### Manipulating Paths

```
os.path.basename(silverlight_plugin_path)
'Silverlight.plugin'
os.path.dirname(silverlight_plugin_path)
'/Library/Internet Plug-Ins'
os.path.splitext("com.apple.Safari.plist")
('com.apple.Safari', '.plist')
```

#### Tests on Files

```
os.path.exists(silverlight_plugin_path)
True
os.path.isdir(silverlight_plugin_path)
True
os.path.islink("/etc")
True
```

#### glob

```
import glob
osx_install = glob.glob("/Applications/" \
    "Install*OS X*.app")
print(osx_install)
['/Applications/Install Mac OS X Lion.app',
 '/Applications/Install OS X Mountain
Lion.app']
```

<div class="notes">
- Equivalent to shell globbing 
- Returns matching path(s) as a list
- glob uses the fnmatch module
</div>





