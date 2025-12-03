# -*- coding: utf-8 -*-
from pathlib import Path
from IPython.display import Code, display


def display_tree(directory, prefix="", is_last=True, max_depth=None, current_depth=0):
    """
    Display directory structure as a tree.

    Args:
        directory: Path to the directory
        prefix: Prefix for the current line (used for recursion)
        is_last: Whether this is the last item in its parent directory
        max_depth: Maximum depth to traverse (None for unlimited)
        current_depth: Current depth level (used for recursion)
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
