# Open-TYNDP Workshops

Series of hands-on workshops facilitated by Open Energy Transition (OET) to accompany the development of an open-source energy modeling tool for the TYNDP.
With every workshop a new notebook will be added to the repository investigating different functionalities of PyPSA
and implementations for the Open-TYNDP workflow.

## Usage

To follow and explore the series of hands-on workshops, you can visit the deployed [workshop page](https://open-energy-transition.github.io/open-tyndp-workshops/intro.html). There, you can also simply launch each notebook in a Google Colab notebook environment by clicking the rocket logo in the top right corner.
Alternatively, you can also build and explore the Open-TYNDP Workshops book locally.

All notebooks are currently compatible with PyPSA v1.0.5.

### Running notebooks locally

#### Using pixi (recommended)

[pixi](https://pixi.sh) manages the exact locked environment from `pixi.lock` and works on Linux, macOS, and Windows.

1. Clone this repository
2. [Install pixi](https://pixi.sh/latest/#installation)
3. Run `pixi install` to set up the environment
4. Launch JupyterLab with `pixi run jupyter lab`

#### Using conda (alternative)

Pre-exported, fully-pinned conda environment files are provided in the `envs/` directory.

1. Clone this repository
2. Install the environment for your platform:
   ```bash
   # Linux
   conda env create -f envs/linux-64.yaml
   # macOS (Apple Silicon)
   conda env create -f envs/osx-arm64.yaml
   # macOS (Intel)
   conda env create -f envs/osx-64.yaml
   # Windows
   conda env create -f envs/win-64.yaml
   ```
3. Activate the environment: `conda activate open-tyndp-workshops`
4. Launch JupyterLab: `jupyter lab`

### Building the book locally

With pixi:

```bash
pixi run build-book
```

To clean and rebuild from scratch:

```bash
pixi run rebuild-book
```

A fully-rendered HTML version of the book will be built in `open-tyndp-workshops/_build/html/`.

### Hosting the book

Please see the [Jupyter Book documentation](https://jupyterbook.org/publish/web.html) to discover options for deploying a book online using services such as GitHub, GitLab, or Netlify.

For GitHub and GitLab deployment specifically, the [cookiecutter-jupyter-book](https://github.com/executablebooks/cookiecutter-jupyter-book) includes templates for, and information about, optional continuous integration (CI) workflow files to help easily and automatically deploy books online with GitHub or GitLab. For example, if you chose `github` for the `include_ci` cookiecutter option, your book template was created with a GitHub actions workflow file that, once pushed to GitHub, automatically renders and pushes your book to the `gh-pages` branch of your repo and hosts it on GitHub Pages when a push or pull request is made to the main branch.

## Contributors

We welcome and recognize all contributions. You can see a list of current contributors in the [contributors tab](https://github.com/fneum/data-science-for-esm/graphs/contributors).

## Credits

This project is created by forking of [Fabian Neumann](https://github.com/fneum)'s excellent open-source course [Data Science for Energy System Modelling](https://github.com/fneum/data-science-for-esm) which uses the open source [Jupyter Book project](https://jupyterbook.org/) and the [executablebooks/cookiecutter-jupyter-book template](https://github.com/executablebooks/cookiecutter-jupyter-book).
