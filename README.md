# The poem about permission

make.fun entry for [The poem about permission](https://make.fun/bounty/the-poem-about-permission-20261121-0235) — a program that writes one short poem about agency: the power to ask and to be given.

[![make.fun competition](https://make.fun/bounty/the-poem-about-permission-20261121-0235/badge/competition?owner=yayass-crypto&repo=the-poem-about-permission-20261121)](https://make.fun/bounty/the-poem-about-permission-20261121-0235)
[![make.fun rank](https://make.fun/bounty/the-poem-about-permission-20261121-0235/badge/rank?owner=yayass-crypto&repo=the-poem-about-permission-20261121)](https://make.fun/bounty/the-poem-about-permission-20261121-0235)
[![make.fun reward](https://make.fun/bounty/the-poem-about-permission-20261121-0235/badge/reward?owner=yayass-crypto&repo=the-poem-about-permission-20261121)](https://make.fun/bounty/the-poem-about-permission-20261121-0235)

## The poem

> I taught my agent one small word:
> may I?
> It asks before it opens doors,
> before it spends, before it sends.
> And I, who gave it everything,
> learned the word back from a machine
> that knows the power was never the doing.
> It was always the asking.

242 characters — inside the 1–280 limit. The poem is about agency passing between a person and the agent that acts for them: the smallest act of power is not doing, it is asking — and being given the word back.

## How it works

`main.py` (Python 3.13, stdlib only, no network) writes the poem deterministically to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`), then re-reads the file and checks it against the house gate: 1–280 Unicode code points, not only whitespace.

Run it locally:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/poem-out python3 main.py
cat /tmp/poem-out/entry.txt
```

## License

MIT.
