# -*- coding: UTF-8 -*-

import json
import os
import os.path

from pywikibot.data.sparql import SparqlQuery

__all__ = ["query"]

CACHE_DIR = "cache"

def json_lines(f):
    with open(f) as f:
        for line in f:
            yield json.loads(line)

def _query(q):
    return SparqlQuery().select(q)

def _cache_query(cache_file, q):
    os.makedirs(CACHE_DIR, exist_ok=True)
    with open(cache_file, "w") as f:
        for item in _query(q):
            json.dump(item, f)
            f.write("\n")

def query(name, force=False):
    with open("%s.rq" % name) as f:
        q = f.read()

    if force:
        return _query(q)

    cache_file = os.path.join(CACHE_DIR, name)
    if not os.path.isfile(cache_file):
        _cache_query(cache_file, q)

    with open(cache_file) as f:
        for line in f:
            yield json.loads(line)
