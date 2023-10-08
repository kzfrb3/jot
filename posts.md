---
slug: d59b357
stamp: 2023-10-06T19:08:30.464382+00:00
title: First post!
---
I have said it before, but I think it bears repeating: I am like that person you might know whose houseplants always die from neglect, but with blogs. I don't think I can even remember how many I've started and abandoned, or how many different softwares I've used or tried in the process. Not to even _mention_ that starting a with-ironic-or-scare-quotes "blog" in the year of 2023 seems particularly foolish and mad. Like what even is the point? And I'm not sure I'm doing myself any favors by dusting off an [old static site generator script](https://github.com/tym-xqo/xqo.wtf) that I wrote myself to do it with.

But then again even after deleting my Facebook and Twitter accounts back in 2016, I am increasingly dismayed by big tech's controlling grasp on the public web, and it makes me wanna do something new and indie on the internets. I've been having an OK time on Mastodon (as [@tym@tilde.zone](https://tilde.zone/@tym)), I've been trying to get a group going on [Wavelength](https://wavelength.app), and after all this time I still [reblog pics and stuff on Tumblr](https://mix.pabloedison.com), check out a limited number of subreddits from time to time, have a couple of Discord groups I visit, &c. All of that is fine I guess, — and I find I value rather than feel bothered the fragmentation of all that, as opposed to the big social media monoliths — but I'm still looking for an outlet, and want something indie, and that doesn't feel compromised or owned by someone else at its foundations. Not that there's any way out: if you're reading this, I've obviously decided to post it somewhere on the public internet. I'm not really set up to use my own hardware for that, so even this static HTML will need to run on some cloud server somewhere, and the code that builds it is already on Microsoft-owned GitHub, and the content is liable to be scraped and indexed and fed to any number of sociopathic large lanuguage models. At the bottom of all the utopian optimism of the early internet was the idea of _sharing_, and even that feels like it's all happening under corporate surveillance now. I've even considered doing some sort of [Gemini](https://geminiprotocol.net), um, thing, but obviously there's a learning curve with that, and plus it's maybe a bit _too_ small. Although I'm on the side of the small internet, I want my friends to be able to find this and read it, and not ALL of them are so extremely nerdy.

Well, anyway, to try to be more hopeful, maybe this is a start. I'm happy that the build script still works, so I can just type this in a text editor as Markdown. I'm not sure how much or often I'll be posting, or what's on my mind to write about, but for a start I think some of the things I've been sharing with my little Wavelength group could be going here instead. I'd also like to add features to make it easier to include images in posts, or maybe even handle images AS posts, because I take a lot of photos especially when I'm walking around outside and even make drawings sometimes and I'd like to share all that here instead of Tumblr, but right now all it does is parsing posts out of a text file.

I gotta admit it feels pretty okay to be typing this in my own favorite editor, I'm happy with my layout and stylesheet, and I'm hoping it will be just the first of many, for whatever any of it might turn out to be worth. Wish me luck!

{end}
---
slug: ec8f0ae
stamp: 2023-10-07T00:23:19.843374+00:00
---
A couple things I do really like about this home-grown set up: 1- It's easy to post just quick brief little things, and 2- posts don't have to have titles

{end}
---
slug: 6217e04
stamp: 2023-10-07T16:00:27.872547+00:00
---
OK, so posting images this way is pretty easy, and needed only one teensy code tweak and equally teensy change to folder structure/process: I added an `/images` subdirectory to the `static` folder, saved this jpeg in there, (relative-)linked it up using a [standard Markdown image tag](https://www.markdownguide.org/basic-syntax/#images-1), and adjusted CSS so that any image that's inside a `.post` div has a 87% max width. 

![Cornelian cherry dogwood in Bahá'í temple garden 2023-10-07](../images/cornelian-cherry-bahá'í-temple.jpg)

I think I'd like to add some logic to the build to automagically add some way to easily view the full-size image — maybe just a link, perhaps a lightbox modal if I'm feeling really fancy. And I still want a way to create like a little gallery with thumbnails. But even the current simple "skateboard" implementation is nice to have for now. If any of y'all wanna see this lovely Cornelian cherry tree I snapped this morning in the sunny Bahá'í temple garden larger, you can always right-click and open it in new tab. So there!

{end}
