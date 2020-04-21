# Bigstep MetalCloud's documentation

[![Documentation Status](https://readthedocs.com/projects/metalsoft-metalcloud/badge/?version=latest&token=78a1dbdaa78397a8f32f7cf0043bb9b9dbbfd80d626613482bfe49eee6e950e1)](https://metalsoft-metalcloud.readthedocs-hosted.com/en/latest/?badge=latest)

This documentation uses markdown and, where tables are needed reStructuredText. Out of the markdown is used Sphinx as a build engine to generate html, table of contents, search indexes etc. 

It also includes python code that generates some portions of the documentation(prices and server_types pages)


## Installing pre-requisites

To install sphinx and markdown support for it (python 3.x recommended):

```bash
pip install sphinx recommonmark jinja2
```

## Generating the documentation manually

Note that you do not need to do this to update the live documentation, as that wil be built automatically by readthedocs upon `git push`.

However, it is very useful to generate the documentation locally in order to view it before updating it as this also performs a validation of broken links, corrupted media etc.

>Note: The default theme used for local generation will be different than the one used by read-the-docs so the documentation will look different but the functionality should be the same.

```bash
make html
```

## Steps for creating an article

Creating an article is very simple:

1. Create a new markdown file (.md) in a directory such as "advanced".
2. Add content. A markdown cheatsheet is available [here](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet).
4. Name the assets with the name of the file you are creating suffixed by `_<number>`  for example `/assets/advanced/getting_started_2.png`. Reference a static asset like this:
    ```markdown
    [](/assets/advanced/getting_started_2.png)
    ```
3. Put static assets such as screenshots in `/assets/<name_of_section>` for example `/assets/advanced`. 

4. Use SVGs when drawing diagrams insted of pngs. Use only simple, monochrome diagrams and avoid using excesive coloring or "clipart". Use simple primitives: boxes, arrows etc. 
5. Add the new section in the index.rst by adding a
reference in a `.. toctree::` section without the (.md or .rst) suffix: `advanced/managing_assets`

## Updating the documentation

To update the documentation simply add the file to git:

```bash
git pull
git add .
git commit -m "meaningful commig message"
git push
```

This should trigger the build automatically.

##  When to use ReStructuredText format (.rst)
ReStructuredText is only for the index page and pages that need to hold tables as for some reason tables are not supported by the markdown parser that sphinx uses.
