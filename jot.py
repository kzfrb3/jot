import shutil
from pathlib import Path

import pytz
import yaml
from jinja2 import Template
from markdown import markdown

POSTS = open("posts.md").read()


def get_posts():
    """ Split the posts file content into a list of individual posts
    """
    posts = POSTS.split("{end}")
    return posts


def parse_post(post):
    """ Split an individual post into metadata and content sections, and YAML load
    the metadata while coverting the markdown content to HTML
    """
    item = post.split("---")[1:]
    metadata = yaml.safe_load(item[0])
    content = markdown(item[1].strip())
    item = dict(metadata=metadata, content=content)
    return item


def sort_posts():
    """ Convert post timestamps to UTC, and sort the posts list according to these values
    """
    posts = get_posts()
    sorted_posts = []
    utc = pytz.timezone("UTC")
    for post in posts:
        post = parse_post(post)
        post["metadata"]["stamp"] = utc.localize(post["metadata"]["stamp"]).isoformat()
        sorted_posts.append(post)
    all_sorted = sorted(
        sorted_posts, key=lambda post: post["metadata"]["stamp"], reverse=True
    )
    return all_sorted


def render(posts=[]):
    """ Given a list of parsed posts, render the HTML from the template file
    """
    if not posts:
        posts = sort_posts()
    with open("template.j2") as template_file:
        template = Template(template_file.read())
    html = template.render(posts=posts)
    return html


def copy_static():
    """ Copy the static files into the build directory
    """
    src = list(Path("static").glob("**/*"))
    for file_ in src:
        dest = Path("site_build", file_.name)
        shutil.copy(file_, dest)


def build():
    """ Generate HTML from posts in `posts.md`
    """
    # TODO: pagination on main posts page
    Path("site_build").mkdir(exist_ok=True)  # create build directory
    copy_static()
    posts = sort_posts()
    html = render(posts=posts)
    with open("site_build/index.html", "w") as output:
        output.write(html)
    for post in sort_posts():
        slug = post["metadata"]["slug"]
        filename = f"site_build/{slug}.html"
        with open(filename, "w") as post_output:
            html = render(posts=[post])
            post_output.write(html)


if __name__ == "__main__":
    build()
