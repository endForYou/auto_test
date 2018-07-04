import ast
import csv
import io
import itertools
import json
import os
import random
import re


def load_csv_file(csv_file):
    """ load csv file and check file content format
    @param
        csv_file: csv file path
        e.g. csv file content:
            username,password
            test1,111111
            test2,222222
            test3,333333
    @return
        list of parameter, each parameter is in dict format
        e.g.
        [
            {'username': 'test1', 'password': '111111'},
            {'username': 'test2', 'password': '222222'},
            {'username': 'test3', 'password': '333333'}
        ]
    """
    csv_content_list = []
    csv_file_actual = "E:\\project\\python_project\\xgjInterfaceTest\\conf\\"+csv_file
    with io.open(csv_file_actual, encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            csv_content_list.append(row)

    return csv_content_list
