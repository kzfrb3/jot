#!/usr/bin/env python

import os
import codecs
# from sh import rsync
import markdown
from datetime import datetime

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

# TODO: get these variables from a config file
local_path = '~/Dropbox/work_src/jot/*'
remote_path = 'tym@tilde.club:~/public_html/jot/'

# rsync("-ave", "ssh", local_path, remote_path)

