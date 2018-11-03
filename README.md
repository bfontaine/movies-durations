# Movies Durations

This repo contains code to export movies from [Wikidata][] and generate a JSON
to plot the evolution of their durations per year.

[Wikidata]: https://www.wikidata.org/

## Setup

You need Python 3.

```
make plots.json
```

This generates a `plot.json` you can use to plot the data with [D3][].

[Online demo](https://beta.observablehq.com/@bfontaine/movies-durations-1916-2018)

[D3]: https://d3js.org/
