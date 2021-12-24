#!/usr/bin/env python3

import os
import re
import yaml

class Trimmer(object):
    """
    Trimmer - trim lines in files, replace \r\n with \n and add final \n in file
    """

    def __init__(self):
        file_path = os.path.dirname(os.path.realpath(__file__))
        filename = os.path.join(file_path, "trimmer.yaml")
        with open(filename, "r") as stream:
            self._config = yaml.safe_load(stream)

    def right(self, dir: str = '.'):
        print(f"DIRECTORY: {dir}")
        for root, subdirs, files in os.walk(dir):
            if (self._not_masked(root)):
                for filename in files:
                    if (self._not_masked(filename)):
                        full_filename = f"{root}/{filename}"
                        print(f"    {full_filename}")
                        self._process(full_filename)

    def _not_masked(self, dir: str):
        for regexp in self._config['regexps']:
            if (re.match(regexp, dir)):
                return False

        return True

    def _process(self, filename):
        try:
            self._load_file(filename)
            self._transform_data()
            self._save_file(filename)
        except UnicodeDecodeError:
            print(f"        ===> UnicodeDecodeError: {filename}")
            pass

    def _load_file(self, filename: str):
        with open (filename, "r") as myfile:
            self.data = myfile.readlines()

    def _transform_data(self):
        converted = []
        for line in self.data:
            converted.append(line.rstrip(" \n\r"))
        self.data = converted

    def _save_file(self, filename):
        with open(filename, "w") as text_file:
            text_file.write("\n".join(self.data) + "\n")