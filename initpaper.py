#!/usr/bin/env python
# coding: utf-8

# Standard library
import os
from os import path
import shutil

def main(dest_path, overwrite=False):
    template_path = path.join(path.dirname(path.abspath(__file__)), 'paper')

    dest_path = path.abspath(path.expanduser(dest_path))
    os.makedirs(dest_path, exist_ok=True)

    for filename in os.listdir(template_path):
        if filename.startswith('.'): continue

        dest_file = path.join(dest_path, filename)
        if path.exists(dest_file) and not overwrite:
            raise IOError("File '{0}' already exists at destination path! Use "
                          "-o to overwrite any existing files".format(filename))

        shutil.copyfile(path.join(template_path, filename), dest_file)


if __name__ == "__main__":
    from argparse import ArgumentParser

    # Define parser object
    parser = ArgumentParser(description="")

    parser.add_argument('-o', '--overwrite', action='store_true',
                        dest='overwrite', default=False,
                        help='Destroy everything.')
    parser.add_argument('--path', dest='dest_path', default=None, required=True,
                        type=str, help='Path to copy the paper template to.')

    args = parser.parse_args()

    main(dest_path=args.dest_path, overwrite=args.overwrite)
