# wtf

Simple python script that generates a static blog page from a text file. Just append a new YAML front matter and markdown to `posts.md` to update your blog. See [posts.md.example](posts.md.example) for the file format.

`wtf.py` parses the file and builds the HTML, putting output in `site_build` directory. This works nicely for CI deployment on Netlify, direct from this repo. At the moment, it creates one `index.html` with all the posts in newest-on-top order, along with a permalink page for each individual post, and an [Atom 1.0]() syndication feed file.

This repo currently includes content and template for <https://xqo.wtf> but in theory could be forked and reused by anyone.

## License

In keeping with the name and nature of the project, released under the [WTFPL](http://www.wtfpl.net/txt/copying/).

## TODO

- move pagination link calculation from template to script
- stand-alone pages from template
- multiple post files
- ~~pagination for the main index~~
- ~~Atom feed output~~
