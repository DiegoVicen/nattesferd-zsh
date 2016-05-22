import os

# This will get the value of $HOST
host = os.uname()[1]

# This is the dictionary used to look up. Here you should add all aliases:
#   "<real>": "<alias>"
# You can use punctuation and spaces in the alias field.
alias = { "mbp.local": "Millenium Falcon"
        }

if (alias.has_key(host)):
    print alias[host]
else:
    print host
