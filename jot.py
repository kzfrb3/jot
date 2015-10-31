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

    # Parse args
    parser = ArgumentParser()
    parser.add_argument(
            '-f', '--filename', nargs='?',
            help='The input status update filename.'
        )
    parser.add_argument(
        '--prod', action='store_true',
        help=('Set flag to publish to live site via '
              'rsync to configured remote_path')
        )
    args = parser.parse_args()

# Read and convert jot file
    if args.filename:
        jotsrc = os.path.join(sys.path[0], args.filename)
    else:
        draftpath = os.path.abspath(os.path.join(sys.path[0], 'draft'))
        filen = max(os.listdir(draftpath),
                    key=lambda f: os.path.getmtime(
                    os.path.join(draftpath, f)))
        jotsrc = os.path.join(sys.path[0], 'draft', filen)
    with codecs.open(jotsrc, encoding='utf-8') as jotfile:
        jot_md = jotfile.read()
    md = markdown.Markdown(['meta'])
    jot_html = md.convert(jot_md)

# Set timestamp from meta or from current:
    if 'timestamp' in md.Meta:
        timestamp = md.Meta['timestamp'][0]
        timestamp = u'**%s** \\- ' % timestamp

    else:
        timestamp = strftime('%Y-%m-%d %H:%M:%S')
        timestamp = u'**%s** \\- ' % timestamp
    timestamp = markdown.markdown(timestamp)[3:-4]  # remove trailing p tag


# Set geotag from meta or Whereami (or blank)
    if 'mapquery' in md.Meta:
        qs = md.Meta['mapquery'][0]
        geotag = (u' <a href="http://maps.google.com/maps?q=%s">'
                  '<i class="fa fa-map-marker"></i></a></p>') % qs
    elif gps_url:
        locreq = requests.get(gps_url)
        locdata = locreq.json()['location']
        lat = locdata['latitude']
        lng = locdata['longitude']
        geotag = (u' <a href="http://maps.google.com/maps?q=%s,%s">'
                  '<i class="fa fa-map-marker"></i></a>') % (lat, lng)
    else:
        geotag = '</p>'


# Remove leading and closing p tags from post,
# we will wrap in timestamp and geotag
    jot_html = jot_html[3:-4]

# Apply the jot_html to the template w/ jinja2
    PWDIR = os.path.join(sys.path[0])
    j = Environment(loader=FileSystemLoader(PWDIR), trim_blocks=True)
    content = j.get_template('template.html').render(jotting=jot_html,
                                                     timestamp=timestamp,
                                                     geotag=geotag)

# Write rendered content to index file
    indexsrc = os.path.join(sys.path[0], 'static', 'index.html')
    with codecs.open(indexsrc, encoding='utf-8', mode='w') as j:
        j.write(content)

# only rsync to server if Prod arg is passed
    if args.prod:
        local_path = os.path.join(local_path, 'static/')
        rsync("-ae", "ssh", local_path, remote_path)
    else:
        pass

if __name__ == '__main__':
    main()
