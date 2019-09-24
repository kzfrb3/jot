from pathlib import Path

import pytz
import yaml
from jinja2 import Template
from markdown import markdown

POSTS = open("posts.md").read()


def get_posts():
    posts = POSTS.split("{end}")
    return posts


def parse_post(post):
    item = post.split("---")[1:]
    metadata = yaml.safe_load(item[0])
    content = markdown(item[1].strip())
    item = dict(metadata=metadata, content=content)
    return item


def sort_posts():
    posts = get_posts()
    sorted_posts = []
    utc = pytz.timezone("UTC")
    for post in posts:
        post = parse_post(post)
        post["metadata"]["date"] = utc.localize(post["metadata"]["date"]).isoformat()
        sorted_posts.append(post)
    all_sorted = sorted(
        sorted_posts, key=lambda post: post["metadata"]["date"], reverse=True
    )
    return all_sorted


def render(posts=[]):
    with open("template.j2") as template_file:
        template = Template(template_file.read())
    html = template.render(posts)
    return html


def build():
    Path("site_build").mkdir(exist_ok=True)
    posts = sort_posts()
    html = render(posts=posts)
    with open("site_build/index.html", "w") as output:
        output.write(html)
    # for post in sort_posts():
    #     title = post["metadata"]["title"]
    #     filename = f"site_build/{title}.html"
    #     with open(filename, "w") as post_output:
    #         html = render(posts=[post])
    #         post_output.write(html)


if __name__ == "__main__":
    print(render(posts=sort_posts()))
