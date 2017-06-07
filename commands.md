### Running Commands

#### Subprocess module
Call external shell commands

|-------------------------|----------------------------|
|                         | *Returns*                  |
| subprocess.call         | Return code                |
| subprocess.check_call   | Return code or exception   |
| subprocess.check_output | Output string or exception |

###

```
import subprocess
cmd_str = '/usr/bin/dsmemberutil checkmembership \
-U jeremy -G admin'
cmd = cmd_str.split()

retcode = subprocess.call(cmd)
checkcode = subprocess.check_call(cmd)
output = subprocess.check_output(cmd)
``
