#!/usr/bin/env python
# coding: utf-8

import os
import sys
import codecs
import yaml
import markdown
import requests
from argparse import ArgumentParser
from time import strftime
from sh import rsync
from jinja2 import Environment, FileSystemLoader

def main():


# Read and parse configuration.
    configfile = os.path.join(sys.path[0], 'config.yml')
    with open(configfile, 'r') as config:
        y = yaml.load(config)
        local_path = y['local_path']
        remote_path = y['remote_path']
        gps_url = y['gps_url']
        use_gps = y['use_gps']

# Parse args
    parser = ArgumentParser()
    parser.add_argument(
            '-f', '--filename', nargs = '?', default='_jot.md',
            help='The input status update filename.'
        )
    parser.add_argument(
        '--prod', action='store_true',
        help='Set flag to publish to live site via rsync to configured remote_path'
        )
    args = parser.parse_args()

# Read and convert jot file
    jotsrc = os.path.join(sys.path[0], args.filename)
    with codecs.open(jotsrc, encoding='utf-8') as jotfile:
      jot_md = jotfile.read()
    md = markdown.Markdown(['meta'])
    jot_html = md.convert(jot_md)

# Set timestamp from meta or from current:
    if md.Meta.has_key('timestamp'):
        timestamp = md.Meta['timestamp'][0]
        timestamp = u'**%s** \\- ' % timestamp

    else:
        timestamp = strftime('%Y-%m-%d %H:%M:%S')
        timestamp = u'**%s** \\- ' % timestamp
    timestamp = markdown.markdown(timestamp)[:-4] # remove trailing p tag


# Set geotag from meta or Whereami (or blank)
    if use_gps == True:
        url = gps_url
        locreq = requests.get(gps_url)
        locdata = locreq.json()
        lat = locdata['latitude']
        lng = locdata['longitude']
        geotag = u'[🌐](http://maps.google.com/maps?q=%s,%s)' % (lat,lng)
        geotag = markdown.markdown(geotag)[3:] # remove leading p tag
    elif md.Meta.has_key('mapquery'):
        qs = md.Meta['mapquery'][0]
        geotag = u'[🌐](http://maps.google.com/maps?q=%s)' % qs
        geotag = markdown.markdown(geotag)[3:] # remove leading p tag
    else:
        geotag = '</p>'


# Remove leading and closing p tags from post,
# we will wrap in timestamp and geotag
    jot_html = jot_html[3:-4]

# Apply the jot_html to the template w/ jinja2
    PWDIR = os.path.join(sys.path[0])
    j = Environment(loader=FileSystemLoader(PWDIR), trim_blocks=True)
    content = j.get_template('template.html').render(jotting = jot_html,
        timestamp = timestamp, geotag = geotag)

    indexsrc = os.path.join(sys.path[0], 'index.html')
    with codecs.open(indexsrc, encoding='utf-8', mode='w') as j:
        j.write(content)
    # only rsync to server if Prod arg is passed
    # if len(sys.argv) >= 2:
    #   if sys.argv[1] == "Prod":
    if args.prod:
        print 'dry run prod success'
        # rsync("-ae", "ssh", local_path, remote_path)
    else:
        print 'you did not say prod'
      # pass

if __name__ == '__main__':
    main()