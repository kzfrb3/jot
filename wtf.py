#!/usr/bin/env python
# -*- coding: utf-8 -
from datetime import datetime
import shutil
from argparse import ArgumentParser
from pathlib import Path

import pytz
import yaml
from feedgenerator import Atom1Feed
from jinja2 import Template
from livereload import Server
from markdown import markdown

# TODO: config file(?)
POSTS_PER_PAGE = 3
SITEURL = "https://pomes.ty-m.pw/"


def clean_build():
    """Remove build directory and recreate empty"""
    shutil.rmtree("site_build", ignore_errors=True)
    build_dir = Path("site_build")
    build_dir.mkdir(exist_ok=True)
    return build_dir


def copy_static():
    """Copy the static files into the build directory"""
    src = list(Path("static").glob("**/*"))
    for f in src:
        dest = Path("site_build", f.name)
        shutil.copy(f, dest)


def get_posts():
    """Split the posts file content into a list of individual posts"""
    with open("posts.md") as post_file:
        content = post_file.read()
    posts = content.split("{end}")[:-1]
    return posts


def parse_post(post):
    """Split an individual post into metadata and content sections, and YAML load
    the metadata while coverting the markdown content to HTML
    """
    item = [i.strip() for i in post.split("---", 2)[1:3]]
    metadata = yaml.safe_load(item[0])
    slug = item[1].split("\n")[0].strip().replace(" ", "-")
    metadata["slug"] = slug
    content = markdown(item[1])
    parsed = dict(metadata=metadata, content=content)
    return parsed


def sort_posts():
    """Convert timestamps to UTC, and sort the posts list according to these values"""
    posts = get_posts()
    sorted_posts = []
    utc = pytz.timezone("UTC")
    for post in posts:
        post = parse_post(post)
        post["metadata"]["stamp"] = (post["metadata"]["stamp"]).astimezone(utc)
        sorted_posts.append(post)
    all_sorted = sorted(
        sorted_posts, key=lambda post: post["metadata"]["stamp"], reverse=True
    )
    return all_sorted


def render(posts, page=0, total=0):
    """Given a list of parsed posts, render the HTML from the template file"""
    with open("template.j2") as template_file:
        template = Template(template_file.read())
    html = template.render(posts=posts, page=page, total=total)
    return html


def post_pages():
    posts = sort_posts()
    for i in range(0, len(posts), POSTS_PER_PAGE):
        yield posts[i : i + POSTS_PER_PAGE]  # noqa E203


def build_index(posts):
    """Generate main blog HTML from posts in `posts.md`"""
    posts = list(post_pages())
    total_pages = len(posts) - 1
    for idx, page in enumerate(posts):
        html = render(posts=page, page=idx, total=total_pages)
        file_ = f"index{idx}.html"
        if idx == 0:
            file_ = "index.html"
        with open(f"site_build/{file_}", "w") as output:
            output.write(html)


def build_individual(posts):
    """Generate permalink pages for individual posts"""
    for post in posts:
        slug = post["metadata"]["slug"]
        permalink = Path("site_build", slug)
        permalink.mkdir(parents=True, exist_ok=True)
        post_file = Path(permalink, "index.html")
        with open(post_file, "w") as post_output:
            html = render(posts=[post])
            post_output.write(html)


def build_feed(posts):
    """Generate Atom feed file"""
    feed = Atom1Feed(
        title="~tym smol pomes", description="", link=f"{SITEURL}/", language="en"
    )
    for post in posts:
        slug = post["metadata"]["slug"]
        stamp = post["metadata"]["stamp"]
        content = post["content"]
        feed.add_item(
            title=slug,
            pubdate=stamp,
            content=content,
            author="xqo",
            description=None,
            link=f"{SITEURL}/{slug}",
        )
    with open("site_build/feed.xml", "w") as feed_output:
        feed.write(feed_output, "utf-8")


def build():
    clean_build()
    copy_static()

    posts = sort_posts()
    build_index(posts)
    build_feed(posts)
    build_individual(posts)
    print("built!")


def serve():
    server = Server()
    server.watch("posts.md", build)
    server.watch("template.j2", build)
    server.serve(root="site_build")


def post():
    utc = pytz.timezone("UTC")
    stamp = utc.localize(datetime.utcnow()).isoformat()
    header = f"---\nstamp: {stamp}\n---\n\n{{end}}\n"
    with open("posts.md", "a") as post_file:
        post_file.write(header)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-s", "--serve", action="store_true", default=False)
    parser.add_argument("-p", "--post", action="store_true", default=False)
    args = parser.parse_args()

    if args.post:
        post()

    else:
        build()
        if args.serve:
            serve()
