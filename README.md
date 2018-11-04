# Movies Durations

This repo contains code to export movies from [Wikidata][] and generate a JSON
to plot the evolution of their durations per year.

[Wikidata]: https://www.wikidata.org/

## Setup

You need Python 3, and the modules in `requirements.txt`.

```
python3 movies_durations.py
```

This reads `movies.rq` and generates `movies.json`, which you can use to plot
the data with [D3][].

[Online demo](https://beta.observablehq.com/@bfontaine/movies-durations-1916-2018)

[D3]: https://d3js.org/

It generates a `cache` directory with the cached query so you don’t have to
re-run it every time.
