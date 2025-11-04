# Open-TYNDP Workshops

Series of hands-on workshops facilitated by Open Energy Transition (OET) to accompany the development of an open-source energy modeling tool for the TYNDP.
With every workshop a new notebook will be added to the repository investigating different functionalities of PyPSA
and implementations for the Open-TYNDP workflow.

## Usage

To follow and explore the series of hands-on workshops, you can visit the deployed [workshop page](https://open-energy-transition.github.io/open-tyndp-workshops/intro.html). There, you can also simply launch each notebook in a Google Colab notebook environment by clicking the rocket logo in the top right corner.
Alternatively, you can also build and explore the Open-TYNDP Workshops book locally.

### Building the book

If you'd like to develop and/or build the Open-TYNDP Workshops book locally, you should:

1. Clone this repository
2. Install the environment by running `conda env create -f environment.yaml`
3. Activate the environment by running `conda activate open-tyndp-workshops`
3. (Optional) Edit the books source files located in the `open-tyndp-workshops/` directory
4. Run `jupyter-book clean open-tyndp-workshops/` to remove any existing builds
5. Run `jupyter-book build open-tyndp-workshops/`

A fully-rendered HTML version of the book will be built in `open-tyndp-workshops/_build/html/`.

### Hosting the book

Please see the [Jupyter Book documentation](https://jupyterbook.org/publish/web.html) to discover options for deploying a book online using services such as GitHub, GitLab, or Netlify.

For GitHub and GitLab deployment specifically, the [cookiecutter-jupyter-book](https://github.com/executablebooks/cookiecutter-jupyter-book) includes templates for, and information about, optional continuous integration (CI) workflow files to help easily and automatically deploy books online with GitHub or GitLab. For example, if you chose `github` for the `include_ci` cookiecutter option, your book template was created with a GitHub actions workflow file that, once pushed to GitHub, automatically renders and pushes your book to the `gh-pages` branch of your repo and hosts it on GitHub Pages when a push or pull request is made to the main branch.

## Contributors

We welcome and recognize all contributions. You can see a list of current contributors in the [contributors tab](https://github.com/fneum/data-science-for-esm/graphs/contributors).

## Credits

This project is created by forking of [Fabian Neumann](https://github.com/fneum)'s excellent open-source course [Data Science for Energy System Modelling](https://github.com/fneum/data-science-for-esm) which uses the open source [Jupyter Book project](https://jupyterbook.org/) and the [executablebooks/cookiecutter-jupyter-book template](https://github.com/executablebooks/cookiecutter-jupyter-book).
