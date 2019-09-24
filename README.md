# jot

Simple python script that generates a static blog page from a text file. Just append a new YAML front matter and markdown to `posts.md` to update your blog. See [posts.md.example](posts.md.example) for the file format.

`jot.py` parses the file and builds the HTML, putting output in `site_build` directory. This works nicely for CI deployment on Netlify, direct from this repo. At the moment, it creates one `index.html` with all the posts in newest-on-top order, along with a permalink page for each individual post.

## TODO

- pagination for the main index
- Atom feed output
