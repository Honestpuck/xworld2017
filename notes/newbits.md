
Show good way of printing dictionary:

```
import os
print os.eviron
for k, v in os.environ.items()
	print (k, v)
```

Data types in Python

Dynamically typed
Strongly typed
Almost everything is an object -but you don't care.
Many helpful types of objects built-in.

Data types
 type() tells you what type an object is
 help(function) gives you help on it.

Numbers
	Integr
	Float
	Not quoted

Lists
	Ordered
	Square brackets

Boolean
	Bool	True	False, None
	String  'a'		''
	Number	1 2.5	0
	List	[1,2]	[]

Dictionaries
	Key value pairs
	Unordered
	Keys
		Case sensitive
		No duplicates
		New value overwrites
		
Case statement

Functions




Working with files
	Building paths
	Name components
	

### joining paths

import os
	disabled_plug_in_paths = os.path.join("/", \
		"Library", \
		"Internet Plug-Ins", \
		"Disabled Plug-Ins")
		
print(disabled_plug_in_paths)
/Library/Internet Plug-Ins/Disabled Plug-Ins

### manipulating paths
os.path.basename(disabled_plug_in_path)

os.path.dirname((disabled_plug_in_path)

os.path.splitext("Word.docx")
('Word', 'docx')

### tests on files

os.path.exists()

os.path.isdir()

os.path.islink()

### File globbing

The same as shell globbing
Returns matching paths

### glob

import glob

text = glob.glob("/Applications/", "Text*.app")

print(text)

### version Numbers

(Two ways)

- distutils.version
	- StrictVersion
	- LooseVersion
- setuptoolls.pkg_resources
	- parse_version
	
###

from distutils import version

version.LooseVersion('10.10.2') > \
version.StrictVersion('10.10.11a2') \

False




<div class="notes">
Here we are just importing part of a package. This reduces memory needs.

</div>

###

#### Syslog

- Send messages to system log
	- With facility (the sender)
	- Priority (level)

###

import syslog
syslog.openlog("TEST")
syslog.syslog(syslog.LOG_NOTICE,
              "No nonsense found.")
syslog.closelog()

(in our shell `tail /var/log/system.log`

### 

#### Running commands
- subprocess module
- call external shell commands

|                         |  returns                   |
|-------------------------|----------------------------|
| subprocess.call         | return code                |
| subprocess.check_call   | return code or exception   |
| subprocess.check_output | output string or exception |


###

#### Running Commands
- Arguments
	- Command as a list of strings
	- Example: [“echo”, “Hello”] 
- Using shell=True
	- Command as a single string 
	- Executed directly through shell 
	- Strongly Discouraged

###

#### Runnning commands

import subprocess
cmd_str = '/usr/bin/dsmemberutil checkmembership \
-U jeremy -G admin'
cmd = cmd_str.split()
retcode = subprocess.call(cmd)
retcode = subprocess.check_call(cmd)
output = subprocess.check_output(cmd)


###

#/usr/bin/env python
import subprocess

class RunCmd(object):
    def cmd_run(self, cmd):
        self.cmd = cmd
        subprocess.call(self.cmd, shell=True)

#Sample usage

a = RunCmd()
a.cmd_run('ls -l')












