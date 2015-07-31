#Jot

A little script for creating a single-page, static-generated website with a "status update" content section that can be edited and replaced easily.

You just write a little content in Markdown, and a Python script converts the Markdown to HTML, adds it to the template file, and rsyncs to the server. So....

See it in action at [~tym](http://tilde.club/~tym/) on the [tilde.club](http://tilde.club).

## Usage

- Edit the `example_config.yml` and `example_template.html` to taste, and rename (or copy) to `config.yml` and `template.html`, respectively.
- Write status post content (in [Markdown](http://daringfireball.net/projects/markdown/) format) in a new file in 'drafts' directory. (Alternatively, you can put your status file wherever you like, and pass the location with `-f` or `--file` flag.) 
- If you are using my [Whereami](http://github.com/yagermadden/whereami), you can put your `gps.json` URL in the config and your status message will be geotagged automagically.
- If you don't have `gps.json`, you can add Mapquery to the post metadata, if you wish. This will be turned into a geotag link at the end of the post. Be sure to set `gps_url` to `False` in the config.
- Note that Whereami users can also put Mapquery as metadata, and Jot will prefer that to the automated GPS lookup.
- If there is neither a gps_url nor Mapquery metadata, the post will simply appear without geotagging.
- Note you don't need to put a time stamp at the front, as the script will take care of that based on the time of posting. If you want to label your post with a specific time, use Timestamp key in metadata.
- Assuming everything is all configured and you like your template, run `jot.py` to generate  your page. You can view your generated `index.html` locally in the `static` directory. Run it with `--prod` argument to proceed with upload to the server (based on config settings for local and remote paths).

## Look
Once again, this is something that scratches a personal itch in a pretty sketchy and minimal way, so no promises, eh? Also as always, forks and feedback welcome and appreciated.
