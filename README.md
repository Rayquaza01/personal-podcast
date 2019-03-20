# Personal Podcast

How to use:
 * `pip3 install feedgen`
 * Set the variables in the options
   * `MAX_ITEMS`: the number of items to keep in the feed (20)
   * `DELETE_OLD`: whether to delete oldest items when exceeding `MAX_ITEMS` (True)
   * `PODCAST_DIR`: A folder on your computer with podcast audio (/var/www/html/podcast)
   * `SERVER`: `PODCAST_DIR`, but accessable on the web (http://your-site.com/podcast)
   * `TITLE`: The title of the podcast (Personal Podcast)
   * `DESC`: The description of the podcast (A personal podcast)
   * `LOGO`: An icon to use as a logo (http://placekitten.com/500/500)
 * Place audio in `PODCAST_DIR`
 * Run `personal-podcast.py` (manually, or by cron)
 * A file called `podcast.rss` will be created in `PODCAST_DIR`
