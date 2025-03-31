# Educators Build Your Own Content

This guide helps you in building your own **Data Science for Energy System Modelling** course based on a tailor-made [Jupyter Book][JupyterBook_1]. By following these instructions, you are able to:

* Duplicate the content of this course and use it as your learning material, i.e. lectures, or similar.
* Set up and deploy a static website like this course using [Github Pages action][gh_actions_python]
* Modify this course based on the Jupyter Book [structure][JupyterBook_2].

:::{admonition} Video Tutorial
:class: tip

<div style="position: relative; width: 100%; padding-bottom: 56.25%">
<iframe src="https://www.youtube.com/embed/mvOgmEgRIhc"
        title="How to create you own energy modeling course" frameborder="0" allowfullscreen
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
        style="position: absolute; width: 95%; height: 95%;">
</iframe>
</div>
:::

<!-- If you want to see what others have created, you can visit -->

Before starting, please make sure that you are using the correct python environment that have at least all the python package dependencies from `environment.yaml` or `requirements.txt`. The instruction are [here if you are using conda (reccomended)](../intro.md#with-conda-recommended) and [here if you are using pip](../intro.md#with-pip).

To follow this tutorial, basic usage of Git is a prerequisit. Here are some resources and tutorials to help you get started with Git:

* [Atlassian: Getting Git right](https://www.atlassian.com/git)
* [PyPSA: Git](https://pypsa-earth.readthedocs.io/en/latest/software_hints.html#git)
* [Corey Schafer: Git Tutorial for Beginners: Command-Line Fundamentals](https://www.youtube.com/watch?v=HVsySz-h9r4)
* [Nick White: Git Tutorial For Dummies](https://www.youtube.com/watch?v=mJ-qvsxPHpY)
* [Colt Steele: Learn Git in 15 Minutes](https://www.youtube.com/watch?v=USjZcfj8yxE).

## 1. Create a New Fork

Create your fork of this repository by clicking on the figure below.

In the **Create a new fork** pop-up menu, shown in the figure below, *<ins>deselect</ins>* the default **Copy the `main` branch only** option.

By doing so, you will reduce further branch creation, required by the workflow.

:::{admonition} Fork this repository!
:class: tip

<center>
<figure>
    <a href='https://github.com/fneum/data-science-for-esm/fork'>
    <img src='https://github.com/open-energy-transition/data-science-for-esm/raw/stanford/data-science-for-esm/_images/03_fork_option.png' alt='' width='95%' style='vertical-align:middle;border:5px solid goldenrod;margin:20px 0px' />
    </a>
    <figcaption>Clicking on the image above will lead directly to the <strong>Create a new fork</strong></figcaption>
</figure>
</center>
:::

> **Note:** The purpose of this is to retain the initial `gh-pages` branch, which is needed for the next section.

## 2. GitHub Pages Setting

In your fork of this repository, there is a single GitHub Setting that needs modifying:

* In the GitHub repository `https://github.com/<your-username>/data-science-for-esm`, go to the GitHub **Settings** -> **Pages** heading.

* In the **GitHub Pages** heading, go to the **Branch** section, and change the selection from `None` to `gh-pages` `/root`.

Once the branch has been selected, at the top of the page a URL will be provided:
* **Your site is live at `https://<your-username>.github.io/data-science-for-esm`**.

<center>
<figure>
    <a href='https://github.com/open-energy-transition/data-science-for-esm/settings/pages'>
    <img src='https://raw.githubusercontent.com/open-energy-transition/data-science-for-esm/stanford/data-science-for-esm/_images/04_gh_pages-options.png' width='97%'style='vertical-align:middle;border:5px solid darkgreen;margin:30px 30px' />
    </a>
    <figcaption>Clicking on this figure will lead directly to the our <strong>GitHub Pages</strong> settings menu</figcaption>
</figure>
</center>


## 3. Content Modification

Modify the content in your computer by cloning your forked `data-science-for-esm` repository:
```
git clone https://github.com/<your-username>/data-science-for-esm.git
cd ./data-science-for-esm
```

You can modify the content by adding, editing and removing markdown (`.md`) and jupyter notebook (`.ipynb`) files in the `data-science-for--esm` folder. 
* Make sure that all attachments within the markdown and jupyter notebook are included as well.
* For a successful deployment of the website, please specify the files and order of those file in the [Table Of Contents](https://jupyterbook.org/en/stable/structure/toc.html) `_toc.yml`.
* To modify details of the website, such as the author, logo, other relevant GitHub and Google Collab links, modify the `_config.yml`.

you can test run the changes locally by running the `jupyter-book build data-science-for-esm` command. 
* This command is in charge generating the HTML code which you can open from your browser.
* You can then run `jupyter-book clean data-science-for-esm` to remove the generated build.
* Further readings on how `jupyter-book build` works are [here](https://jupyterbook.org/en/stable/basics/build.html)

### 3a. Add your own logo

If you want your institution to be placed in the top left corner of this website, we recommend that you follow these steps:
* name your institue logo in as `logo_int.png` and place it inside the data-science-for-esm folder.
* Run `oet-extension/merge_logo.py` to combine your institute with as smaller image of TU Berlin's and OET's logo
* Within `_config.yml`, make sure that the logo is directed to `logo: logo_merged.png`.

## 4. Deploy Settings

In the `.github/workflows/deploy.yml`file of the cloned repository, specify the branch other than the `gh-pages`, to be used by the workflow:

~~~
on:
  # Trigger the workflow on push to the main branch
  push:
    branches:
    - main
~~~

Upon the `git push` command to the specified branch, which in this example is the `main` branch, the workflow will be triggered.
~~~
git status
git add .
git commit -m 'new changes applied'
git push
~~~

## 5. GitHub Workflow Deployment

After a successful `git push`, Github will the deploy any workflow within the `.github/workflows/` folder.

The workflow deployment is tracked by your repository's status indicator, in this case a beige-brown dot &nbsp;<strong><b><font color='peru'>⏺</font></strong></b>
* This will take minutes to finished, especially for complex python commands in the Jupyter Notebooks.
* Clicking on it will show the running status, and the deployment details.

<center>
<figure>
    <!-- <a href='https://github.com/open-energy-transition/data-science-for-esm/settings/pages'> -->
    <img src='https://raw.githubusercontent.com/mdzzg/data-science-for-esm/mdzzg/data-science-for-esm/_images/05_deployment_status.png' width='85%'style='vertical-align:middle;border:5px solid paleturquoise;margin:30px 30px' />
    <!-- </a> -->
    <figcaption>Deployment status upon <code>git push</code> to the branch specified in the <code>deploy.yml</code> file</figcaption>
</figure>
</center>

Upon the deployment finalization, the status indicator turns to:
* successful: a green thick <strong><b><font color='green'>🗸</font></strong></b>
    * you should be able to see the changes taking place, after some moments, at the specified `https://<your-username>.github.io/data-science-for-esm`
* unsuccessful: a red cross mark <font color="red">🗶</font>
    * indicating an error in the `_toc.yml`, or one of the content files, which need to be revisited.

<center>
<figure>
    <!-- <a href='https://github.com/open-energy-transition/data-science-for-esm/settings/pages'> -->
    <img src='https://raw.githubusercontent.com/open-energy-transition/data-science-for-esm/stanford/data-science-for-esm/_images/06_successful_deployment.png' width='85%'style='vertical-align:middle;border:5px solid paleturquoise;margin:30px 30px' />
    <!-- </a> -->
    <figcaption>Successful deployment, after a finalized <code>jupyter-book build</code> run</figcaption>
</figure>
</center>



<!-- Congratulations on creating your own Data Science for Energy System Modeling course! Here are some examples of similar courses others have developed.

If you’d like to add your course to this list, please reach out to XXX. -->

<!-- # Internal Doc References -->
[JupyterBook_1]:        https://jupyterbook.org/en/stable/start/create.html
[JupyterBook_2]:        https://jupyterbook.org/en/stable/basics/organize.html
[gh_actions_python]:    https://github.com/peaceiris/actions-gh-pages?tab=readme-ov-file#%EF%B8%8F-static-site-generators-with-python
[fneum]:    https://github.com/fneum/data-science-for-esm
[OET]:      https://open-energy-transition.github.io/handbook/docs/Engineering/SoftForkStrategy/#contributing-oet-changes-to-upstream-via-cherry-picking
[deploy]:   https://github.com/open-energy-transition/data-science-for-esm/blob/main/.github/workflows/deploy.yml
[folder]:   https://github.com/open-energy-transition/data-science-for-esm/tree/main/data-science-for-esm

