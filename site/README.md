# proselint.com

## Installing Jekyll

If you don't have Jekyll already installed, you will need to go ahead and do that.

```
$ gem install jekyll
```

#### Verify your Jekyll version

It's important to also check your version of Jekyll since this project uses Native Sass which
is [only supported by 2.0+](http://jekyllrb.com/news/2014/05/06/jekyll-turns-2-0-0/).

```
$ jekyll -v
# This should be jekyll 2.0.0 or later
```

### Modify the _config.yml

The `_config.yml` located in the root site directory contains all the configuration details for the Jekyll site. The defaults are:

### Jekyll Serve

Then, start the Jekyll Server. Using the `--watch` option updates the generated HTML when you make changes.

```
$ jekyll serve --watch
```

Now you can navigate to `localhost:4000` in your browser to see the site.
