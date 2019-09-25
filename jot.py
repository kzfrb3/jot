import shutil
from pathlib import Path

import pytz
import yaml
from jinja2 import Template
from markdown import markdown

POSTS = open("posts.md").read()
POSTS_PER_PAGE = 3


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


def render(posts=[], page=0, total=0):
    """ Given a list of parsed posts, render the HTML from the template file
    """
    if not posts:
        posts = sort_posts()
    with open("template.j2") as template_file:
        template = Template(template_file.read())
    html = template.render(posts=posts, page=page, total=total)
    return html


def clean_build():
    """ Remove build directory and recreate empty
    """
    shutil.rmtree("site_build", ignore_errors=True)
    build_dir = Path("site_build")
    build_dir.mkdir(exist_ok=True)
    return build_dir


def copy_static():
    """ Copy the static files into the build directory
    """
    src = list(Path("static").glob("**/*"))
    for f in src:
        dest = Path("site_build", f.name)
        shutil.copy(f, dest)


def post_pages():
    posts = sort_posts()
    for i in range(0, len(posts), POSTS_PER_PAGE):
        yield posts[i : i + POSTS_PER_PAGE]  # noqa E203


def build_index():
    """ Generate main blog HTML from posts in `posts.md`
    """
    posts = list(post_pages())
    total_pages = len(posts) - 1
    for idx, page in enumerate(posts):
        html = render(posts=page, page=idx, total=total_pages)
        file_ = f"index{idx}.html"
        if idx == 0:
            file_ = "index.html"
        with open(f"site_build/{file_}", "w") as output:
            output.write(html)


def build_individual():
    """ Generate permalink pages for individual posts
    """
    for post in sort_posts():
        slug = post["metadata"]["slug"]
        permalink = Path("site_build", slug)
        permalink.mkdir(parents=True, exist_ok=True)
        post_file = Path(permalink, "index.html")
        with open(post_file, "w") as post_output:
            html = render(posts=[post])
            post_output.write(html)


def build():
    clean_build()
    copy_static()
    build_index()
    build_individual()


if __name__ == "__main__":
    build()
