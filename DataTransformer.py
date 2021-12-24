#!/usr/bin/env python3

import os
import re
import yaml

class DataTransformer(object):

    def transform(self, data):
        converted = []
        for line in data:
            converted.append(line.rstrip(" \n\r"))
        return converted
