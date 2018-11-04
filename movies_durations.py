# -*- coding: UTF-8 -*-

import json
import argparse
from collections import defaultdict, Counter

import numpy as np


MIN_MOVIES_BY_YEAR = 100


def year_metrics(y, durations_counts):
    total = 0
    for count in durations_counts.values():
        total += count
        if total > MIN_MOVIES_BY_YEAR:
            break
    else:
        if total < MIN_MOVIES_BY_YEAR:
            return


    all_durations = np.array([d for duration, count in durations_counts.items()
                                    for d in [duration] * count])

    pmin = all_durations.min()
    pmax = all_durations.max()

    q1 = np.quantile(all_durations, 0.25)
    q2 = np.quantile(all_durations, 0.50)
    q3 = np.quantile(all_durations, 0.75)

    iqr = q3 - q1  # [i]nter[q]uartile [r]ange
    r0 = max((pmin, q1 - iqr * 1.5))
    r1 = min((pmax, q3 + iqr * 1.5))

    return {
        "x": y,
        "quartiles": [int(q1), int(q2), int(q3)],
        "range": [int(r0), int(r1)],
    }

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--file", "-f", default="movies.jsons")
    p.add_argument("--output", "-o", default="plots.json")
    opts = p.parse_args()
    with open(opts.file) as f:
        body = json.load(f)

    years = defaultdict(Counter)
    total_movies = 0

    for fields in body["results"]["bindings"]:
        pubdate = fields.get("publication_date")
        if not pubdate or pubdate["type"] != "literal":
            continue

        duration = fields.get("duration")
        if not duration or duration["type"] != "literal":
            continue

        year = pubdate["value"].split("-", 1)[0]
        if len(year) != 4:
            continue

        year = int(year)
        duration = int(float(duration["value"]))

        if not duration or not year:
            continue

        years[year][duration] += 1
        total_movies += 1

    years_metrics = []
    for y, ds in years.items():
        m = year_metrics(y, ds)
        if m:
            years_metrics.append(m)

    print("Got %d movies with duration" % total_movies)

    with open(opts.output, "w") as f:
        json.dump(sorted(years_metrics, key=lambda m: m["x"]), f)


if __name__ == "__main__":
    main()
