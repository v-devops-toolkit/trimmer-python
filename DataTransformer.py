#!/usr/bin/env python3


class DataTransformer(object):
    def transform(self, data):
        converted = []
        for line in data:
            converted.append(line.rstrip(" \n\r\t"))
        return converted
