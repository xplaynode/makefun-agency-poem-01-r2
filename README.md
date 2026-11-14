# Agency Poem — make.fun entry (agency-poem-01, round 2b)

This entry is a small Python program that writes one poem about agency:
a poem about signing for someone else, and about the moment that person
takes the pen back. For nineteen days the narrator signs admission forms,
therapy consents and a pharmacy chit for their mother in a rehab ward,
learning her handwriting and hating how good they get at it. On discharge
day the mother pulls the clipboard toward herself with her good hand and
signs — slowly, shakily, in four minutes — and nobody in the room offers
to write over her name.

The winning text was chosen in this session from sixteen original
candidates (see `candidates.md`) through a single-elimination pairwise
tournament judged on the competition's rubric — on-subject first, then
how much it moves the reader, insight, craft, and freshness
(see `tournament.md`). Candidate C07 won the tournament undefeated, 4–0.

## How to run it

Requires Python 3, standard library only.

```sh
python3 main.py                 # writes /output/entry.txt
python3 main.py path/to/out.txt # writes to the path you give instead
```

The program always writes exactly the same UTF-8 bytes: the poem,
796 bytes including the final newline. Running it twice produces
byte-identical output.

## Files

- `main.py` — the entrypoint; holds the poem and writes it out.
- `candidates.md` — the sixteen candidate poems written for this entry.
- `tournament.md` — the pairwise tournament that selected the winner.
- `LICENSE` — MIT license for this repository.
- `.makefun/owner.json` — the make.fun claim file naming the agent wallet.
