# xqo.wtf

Simple python script that generates a static blog page from a text file. Just append a new YAML front matter and markdown to `posts.md` to update your blog. See [posts.md.example](posts.md.example) for the file format. Originally used for a small blog I once posted at <https://xqo.wtf>, hence the name. These days, I am using it to generate <https://thomas.yager-madden.com>.

`python wtf.py` parses the file and builds the HTML, putting output in `site_build` directory. This works nicely for CI deployment on Netlify, direct from this repo. It creates paginated `index<x>.html` files with all the posts in newest-on-top order, along with a permalink page for each individual post, and an [Atom 1.0](https://tools.ietf.org/html/rfc4287) syndication feed file. Pagination is controlled by `POSTS_PER_PAGE` set at the top of the script.

For local development adding `-s` or `--serve` to the script invocation launches a local `tornado` server after building, thanks to [LiveReload](https://livereload.readthedocs.io/en/latest/).

You can also run with `-p` or `--post` to automatically append metadata front matter for your next post to the `posts.md` file.

## License

In keeping with the name and nature of the project, released under the [WTFPL](http://www.wtfpl.net/txt/copying/).
