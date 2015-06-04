#Jot

A little script for creating a single-page, static-generated website with a "status update" content section that can be edited and replaced easily.

You just write a little content in Markdown, and a Python script converts the Markdown to HTML, adds it to the template file, and rsyncs to the server. So....

See it in action at [~tym](http://tilde.club/~tym/) on the [tilde.club](http://tilde.club).

## Usage

- Edit the `example_config.yml` and `example_template.html` to taste, and rename (or copy) to `config.yml` and `template.html`, respectively.
- Write status post in `_jot.md`. 
- If you are using my [Whereami](http://github.com/yagermadden/whereami), you can put your `gps.json` URL in the config and your status message will be geotagged automagically. Set `use_gps` to True(1) in the config.
- If you don't have `gps.json`, you can add Mapquery to the post metadata, if you wish. This will be turned into a geotag link at the end of the post.
- Note you don't need to put a time stamp at the front, as the script will take care of that. If you want to label your post with a specific time, use Timestamp key in metadata.
- Assuming everything is all configured and you like your template, run `jot.py` to generate and publish your page.

## Look
Once again, this is something that scratches a personal itch in a pretty sketchy and minimal way, so no promises, eh? Also as always, forks and feedback welcome and appreciated.
