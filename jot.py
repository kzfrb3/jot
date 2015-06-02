#!/usr/bin/env python
# coding: utf-8

import os
import codecs
import yaml
import markdown
import requests
# from datetime import datetime
from time import strftime
from sh import rsync

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

    jotfile = codecs.open('_jot.md', encoding='utf-8')
    jot = jotfile.read()
    jot = u'%s %s%s' % (timestamp, jot, geotag)
    jotfile.close()

    md = markdown.Markdown()
    jot_html = md.convert(jot)
    template_htmlfile = codecs.open('template.html', encoding='utf-8')
    template_html = template_htmlfile.read()
    template_htmlfile.close()
    content = template_html.replace('<!--TKTKREPLACE -->', jot_html)


    with codecs.open('index.html', encoding='utf-8', mode='w') as j:
        j.write(content)

    rsync("-ae", "ssh", local_path, remote_path)

if __name__ == '__main__':
    main()