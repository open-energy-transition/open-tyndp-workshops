# -*- coding: utf-8 -*-
from pathlib import Path
from IPython.display import Code, display
from pdf2image import convert_from_path
from pdf2image.exceptions import PDFPageCountError
import matplotlib.pyplot as plt
from pypsa_explorer import create_app

try:
    from google.colab import output

    print(f"This notebook is running on Google Colab!")
except ImportError:
    print(f"This notebook is running locally !")


def display_tree(
    directory: str | Path,
    prefix: str = "",
    is_last: bool = True,
    max_depth: int | None = None,
    current_depth: int = 0,
) -> None:
    """
    Display directory structure as a tree.

    Parameters
    ----------
    directory : str or Path
        Path to the directory.
    prefix : str, optional
        Prefix for the current line, used for recursion. Defaults to "".
    is_last : bool, optional
        Whether this is the last item in its parent directory. Defaults to True.
    max_depth : int or None, optional
        Maximum depth to traverse. None for unlimited. Defaults to None.
    current_depth : int, optional
        Current depth level, used for recursion. Defaults to 0.
    """
    directory = Path(directory)

    if not directory.exists():
        print(f"Directory '{directory}' does not exist!")
        return

    # Print current directory/file
    connector = "└── " if is_last else "├── "
    print(f"{prefix}{connector}{directory.name}/")

    # Check depth limit
    if max_depth is not None and current_depth >= max_depth:
        return

    # Get all subdirectories and files
    try:
        contents = sorted(directory.iterdir(), key=lambda x: (not x.is_dir(), x.name))
    except PermissionError:
        print(f"{prefix}    [Permission Denied]")
        return

    # Filter for directories only (optional - remove this line to show files too)
    contents = [item for item in contents if item.is_dir()]

    # Process each item
    for i, item in enumerate(contents):
        is_last_item = i == len(contents) - 1
        extension = "    " if is_last else "│   "

        if item.is_dir():
            display_tree(
                item, prefix + extension, is_last_item, max_depth, current_depth + 1
            )


def show_benchmarks(
    fn: str,
    years: list = [2030, 2040],
    bench_path: str = "data/results-1H-20251129/validation/graphics_s_all___all_years",
    layout: str = "by_row",
):
    """
    Display benchmark figures for one or more years side by side.

    Parameters
    ----------
    fn : str
        Base filename of the benchmark PDFs, without year suffix or file type suffix.
    years : list of int, optional
        Years to include in the plot. Defaults to [2030, 2040].
    bench_path : str, optional
        Path to the directory containing the benchmark PDF files.
    layout : {"by_column", "by_row"}
        Whether to arrange figures across columns (side by side) or
        down rows (stacked). Defaults to "by_row".

    Returns
    -------
    None
        Displays the plot inline and returns nothing.
    """
    try:
        images = [
            convert_from_path(Path(bench_path, f"{fn}_{y}.pdf"))[0] for y in years
        ]
    except PDFPageCountError:
        print("File not found, skipping...")
        return

    n = len(images)
    nrows, ncols = (1, n) if layout == "by_column" else (n, 1)
    fig, axes = plt.subplots(nrows, ncols)
    axes = [axes] if n == 1 else axes.flatten()

    for ax, img in zip(axes, images):
        ax.imshow(img)
        ax.axis("off")
    plt.tight_layout()
    plt.show()


def run_pypsa_explorer_in_colab(networks, port):
    print("Starting PyPSA Explorer for Google Colab...")

    # Create and start the app
    app = create_app(networks)

    import threading
    import time

    def run_server():
        app.run(jupyter_mode="external", port=port, debug=False)

    server_thread = threading.Thread(target=run_server, daemon=True)
    server_thread.start()

    # Wait for server to initialize
    time.sleep(5)
    print(f"✓ Server started on port {port}")

    # Display in iframe
    output.serve_kernel_port_as_iframe(port, height=1500)


def display_code_lines(filename, language, start, end):
    with open(filename) as f:
        lines = f.readlines()
    return Code("".join(lines[start - 1 : end]), language=language)
