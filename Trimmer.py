#!/usr/bin/env python3

import os
import re
import yaml
import DataTransformer
import pprint

class Trimmer(object):
    """
    Trimmer - trim lines in files, replace \r\n with \n and add final \n in file
    """

    def __init__(self):
        self._data_transformer = DataTransformer.DataTransformer()
        file_path = os.path.dirname(os.path.realpath(__file__))
        filename = os.path.join(file_path, "trimmer.yaml")
        with open(filename, "r") as stream:
            self._config = yaml.safe_load(stream)

    def debug(self):
        pprint.pprint(self._config)

    def version(self):
        print('trimmer ver. 0.3.0')

    def right(self, dir: str = '.'):
        print(f"DIRECTORY: {dir}")
        for root, subdirs, files in os.walk(dir):
            for filename in files:
                full_filename = f"{root}/{filename}"
                if (not self._is_excluded(full_filename)):
                    print(f"    {full_filename}")
                    self._process(full_filename)

    def _is_excluded(self, dir: str):
        for regexp in self._config['exclude']:
            if (re.search(regexp, dir)):
                return True
        return False

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
        self.data = self._data_transformer.transform(self.data)

    def _save_file(self, filename):
        with open(filename, "w") as text_file:
            text_file.write("\n".join(self.data) + "\n")
