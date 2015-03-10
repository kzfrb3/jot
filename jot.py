#!/usr/bin/env python

import os
import codecs
from sh import rsync
import markdown
from datetime import datetime

# TODO: get these variables from a config file
# For now, set these here for uploading
local_path = '~/jot/'
remote_path = 'user@somewhere.tld:~/public_html/jot/'

timenow = datetime.now()
timestamp = timenow.strftime('%Y-%m-%d %H:%M:%S')
timestamp = '**%s** \\- ' % timestamp

jotfile = codecs.open('_jot.md', encoding='utf-8')
jot = jotfile.read()
jot = timestamp + jot
jotfile.close()
# print jot

md = markdown.Markdown()
jot_html = md.convert(jot)
jotting_htmlfile = codecs.open('jotting.html', encoding='utf-8')
jotting_html = jotting_htmlfile.read()
jotting_htmlfile.close()
jotting = jot_html + jotting_html
with codecs.open('jotting.html', encoding='utf-8', mode='w') as j:
    j.write(jotting)

rsync("-ave", "ssh", local_path, remote_path)

