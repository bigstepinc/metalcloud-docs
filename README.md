# Bigstep MetalCloud's documentation

[![Documentation Status](https://readthedocs.com/projects/metalsoft-metalcloud/badge/?version=latest&token=78a1dbdaa78397a8f32f7cf0043bb9b9dbbfd80d626613482bfe49eee6e950e1)](https://metalsoft-metalcloud.readthedocs-hosted.com/en/latest/?badge=latest)

This documentation uses markdown and, where tables are needed reStructuredText. Out of the markdown is used Sphinx as a build engine to generate html, table of contents, search indexes etc. 

It also includes python code that generates some portions of the documentation(prices and server_types pages)


## Installing pre-requisites

To build the sources you need `python 3.x` and `pip`. These are platform dependent.  Here are some resources but there are countless others out there.

1. [Installing python on windows](https://docs.python.org/3/using/windows.html)
2. [Installing python on ubuntu](https://linuxize.com/post/how-to-install-python-3-7-on-ubuntu-18-04/)
3. [Installing pip on ubuntu](https://linuxize.com/post/how-to-install-pip-on-ubuntu-18.04/)


To install sphinx and markdown support for it (python 3.x recommended):

```bash
$ pip install sphinx recommonmark jinja2
```

## Pulling the sources locally

While you can simply edit the files online using github's editor it is recommended that you sync the repository locally and use a better editor such as Visual Studio Code to edit the files. VS Code has a markdown extension that enables live preview. 

To pull the sources locally you need `git`. 
1. [Installing git](https://git-scm.com/download)

```bash
git clone git@github.com:bigstepinc/metalcloud-docs.git
```

## Generating the documentation manually

Note that you do not need to do this to update the live documentation, as that wil be built automatically by readthedocs upon `git push`.

However, it is very useful to generate the documentation locally in order to view it before updating it as this also performs a validation of broken links, corrupted media etc.

```bash
$ make html
```

>Note: The default theme used for local generation will be different than the one used by read-the-docs so the documentation will look different but the functionality should be the same.

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

To review the changes you made:

```bash
$ git status
```

To update the documentation simply add the file to git:

```bash
$ git pull
$ git add .
$ git commit -m "meaningful commig message"
$ git push
```

This will trigger the build and will perform a release automatically.

##  When to use ReStructuredText format (.rst)
ReStructuredText is only for the index page and pages that need to hold tables as for some reason tables are not supported by the markdown parser that sphinx uses.
