### Subprocess - running a command

``` python
# Loads the InstallApplications LaunchDaemon

import subprocess
import sys
import os

def launchctld(identifier):
    try:
        path = os.path.join('/Library', 'LaunchDaemons', identifier)
        cmd = ['/bin/launchctl', 'load', path]
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)
        output, err = proc.communicate()
        return output
    except KeyError:
        pass
```

