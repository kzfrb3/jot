#!/usr/bin/env python
# coding: utf-8

import os
import sys
import codecs
import yaml
import markdown
import requests
from time import strftime
from sh import rsync
from jinja2 import Environment, FileSystemLoader

def main():
    timestamp = strftime('%Y-%m-%d %H:%M:%S')
    timestamp = '**%s** \\- ' % timestamp

# Read and parse configuration.
    with open('config.yml', 'r') as config:
        y = yaml.load(config)
        local_path = y['local_path']
        remote_path = y['remote_path']
        gps_url = y['gps_url']
        use_gps = y['use_gps']

    geotag = ''

    if use_gps == True:
        url = gps_url
        locreq = requests.get(gps_url)
        locdata = locreq.json()
        lat = locdata['latitude']
        lng = locdata['longitude']
        geotag = u'[🌐](http://maps.google.com/maps?q=%s,%s)' % (lat,lng)

    with codecs.open('_jot.md', encoding='utf-8') as jotfile:
      jot = jotfile.read()
    jot = u'%s %s%s' % (timestamp, jot, geotag)

    md = markdown.Markdown()
    jot_html = md.convert(jot)

    PWDIR = os.path.dirname(os.path.abspath(__file__))
    j = Environment(loader=FileSystemLoader(PWDIR), trim_blocks=True)
    content = j.get_template('template.html').render(jotting = jot_html)

    with codecs.open('index.html', encoding='utf-8', mode='w') as j:
        j.write(content)
    # only rsync to server if Prod arg is passed
    if len(sys.argv) >= 2:
      if sys.argv[1] == "Prod":
        rsync("-ae", "ssh", local_path, remote_path)
    else:
      pass

if __name__ == '__main__':
    main()