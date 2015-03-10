#Jot

A dumb little script for static-generated micro-blogging, sorta. It uses a couple lines of jQuery to replace a div on a web page (`index.html`) with some HTML from another file (`jotting.html`) when the page loads. This is sort of like an 'include' file in some dynamic server-side languages, except I wanted it on the client because my site is hosted at [tilde.club](http://tilde.club) so I can't do any CGI shenanigans. 

And there's a place to write new content in Markdown, and a Python script that converts the Markdown to HTML, adds it to the include file, and rsyncs to the server. So....

## Usage

- Write something in `_jot.md` and fill in the Google Maps search query at the bottom, if you wish. Note you don't need to put a time stamp at the front, as the script will take care of that.
- Edit the `jot.py` variables `local_path` and `remote_path` to where you actually have Jot installed and where you want to upload it, respectively.
- Edit the contents of the `index.html` file's `#top` and `#end` divs to taste. This will be like the static template stuff around your include file content.
- At the moment, the script just keeps adding new posts to the top of the 'jotting.html' include file. There's no facility for archiving or removing old posts. You can manage that manually by cleaning up the file, or renaming it to something else, like `jotting.old` or what have you.

## Look
I'm not saying this is super great; in fact, I acknowledge it's basically nothing. But I am enjoying using it, and maybe someone else would, too.
