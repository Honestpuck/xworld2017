### Using PyObjC

#### Read a preference

``` python

#!/usr/bin/python

from CoreFoundation import CFPreferencesCopyValue, \
  kCFPreferencesCurrentUser, kCFPreferencesAnyHost

v = CFPreferencesCopyValue('NSNavLastRootDirectory', 'com.apple.Finder', \
  kCFPreferencesCurrentUser, kCFPreferencesAnyHost)
print(v)
```
#### Write a preference value
```
CFPreferencesSetValue('FXConnectToLastURL', 'smb://example.com', 'com.apple.Finder', \
  kCFPreferencesCurrentUser, kCFPreferencesAnyHost)

# Required to force preferences to sync to .plist on disk
CFPreferencesSynchronize('com.apple.Finder', kCFPreferencesCurrentUser, 
  kCFPreferencesAnyHost)
```

<div class="notes">
PyObjC is a bridge between Python and Objective-C that allows you to do some
powerful things in Python without running any other software.
</div>
