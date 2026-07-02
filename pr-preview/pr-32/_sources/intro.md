# Welcome: Open-TYNDP Workshops

Welcome to the website covering a series of hands-on workshops facilitated by Open Energy Transition (OET) to accompany the development of an open-source energy modeling tool for the Ten-Year Network Development Plan (TYNDP).
With every workshop a new notebook will be added to this website investigating different functionalities of PyPSA and implementations for the Open-TYNDP workflow. All notebooks are currently compatible with PyPSA v1.1.2.

The workshops will, one by one, introduce modellers to the basics of the PyPSA framework and investigate important features of the TYNDP Scenario Building introduced by the OET team.
Notably, this will include:

- Electricity and H2 reference grids
- PyPSA framework introduction
- Snakemake workflows
- Open-TYNDP benchmarking framework
- Offshore Hubs
- Demand profiles
- Existing supply infrastructure (PEMMDB) & climate data (PECD)
- EVs, Synthetic fuels & Hybrid Heat Pumps
- Running CBA workflows including different projects, climate years and planning horizons

## Setting up the environment

### For the workshop: Google Colab

For these workshops we will cover the material without a local Python installation using the online service  [Google Colab (colab.google)](https://colab.google) which provides an online Python version
in a [Jupyter Notebook](jupyter.org/) environment. This requires a Google account.

For running the notebook using Google Colab you can simply launch it by clicking on the little rocket symbol in the top right corner of the page:

![notebook_launch.png](notebook_launch.png)

### Alternative: Local installation

If you don't want to use Google Colab you will need to install the packages locally. For running this, Python and nearly all of the software packages in the scientific python
ecosystem are [open-source](https://opensource.org/). Coordinating the
compatibility between these different packages and their multiple versions can be difficult! Fortunately, the problem is solved by using a Python
_distribution_ and/or _package manager_. You should use a package manager!

#### Using pixi (recommended)

[pixi](https://pixi.sh) is a fast, cross-platform package manager that installs the exact locked environment and works on Linux, macOS, and Windows.

1. Clone the repository
2. [Install pixi](https://pixi.sh/latest/#installation) (single command, no admin rights required)
3. In the repository root, run `pixi install`
4. Start JupyterLab: `pixi run jupyter lab`

#### Using conda (alternative)

##### Installing conda

**Anaconda**

You can install on your computer the popular
[Anaconda Python Distribution](https://www.anaconda.com/download/).
Follow the link above to obtain a one-click installer for your operating system.

For **Linux and MacOS users**, you can access the command line by opening the _terminal_ program.

For **Windows users**, you should first install Anaconda (described above) or `miniconda` (described below), which gives you access to the "Anaconda Prompt" desktop application. (Instructions for this are given on the [Anaconda Website](https://docs.anaconda.com/anaconda/user-guide/getting-started/#write-a-python-program-using-anaconda-prompt-or-terminal).)

From the Anaconda Prompt, you should be able to run `conda` and other shell commands.

**Lightweight miniconda**

If you don't want to download a large file like the Anaconda Python Distribution (ca. 800 MB), there is a
lightweight alternative installation called `miniconda`.
Follow the link to the [Miniconda Installation](https://docs.conda.io/en/latest/miniconda.html) page and use, for example, the [quick command line install](https://docs.anaconda.com/miniconda/#quick-command-line-install).

**Windows user installation**

For running this workshop notebook locally, it is necessary to install the required environment using the conda package manager as described above.

Windows users have multiple options for this:

- Recommended: Use [Windows Subsystem for Linux (WSL)](https://learn.microsoft.com/en-us/windows/wsl/install) which will allow you to follow the Linux installation instructions for conda and the python environment.
- Install Windows native conda via `Anaconda` (described above) or `miniconda` (described above), which gives you access to the "Anaconda Prompt" desktop application. From the Anaconda Prompt, you should be able to run `conda` and other shell commands. Visit the [Conda Website](https://docs.conda.io/projects/conda/en/stable/user-guide/install/windows.html) for more information.

##### Creating the environment

Fully-pinned environment files for each platform are available in the [`envs/` directory](https://github.com/open-energy-transition/open-tyndp-workshops/tree/main/envs) of the repository.

After cloning the repository and navigating to its folder, you can create this environment using `conda`.

    # Linux
    conda env create -f envs/linux-64.yaml
    # macOS (Apple Silicon)
    conda env create -f envs/osx-arm64.yaml
    # macOS (Intel)
    conda env create -f envs/osx-64.yaml
    # Windows
    conda env create -f envs/win-64.yaml

Activate this environment

    conda activate open-tyndp-workshops

This environment should be sufficient for all of your work in these workshops.

The environment has to be activated whenever you open a new terminal,
*before* starting a new Jupyter window with

    jupyter lab
