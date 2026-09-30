#!/usr/bin/env python3
import csv

TIE = ["V2C1", "V2C3", "V2C2", "V2C4", "V2C5", "V2C6", "V2C7"]

with open("SCORING_MODEL.csv", encoding="utf-8-sig", newline="") as f:
    model = list(csv.DictReader(f))
weights = {row["criterion_id"]: float(row["weight"]) for row in model}
criteria = list(weights)

with open("SCORE_MATRIX.csv", encoding="utf-8-sig", newline="") as f:
    rows = list(csv.DictReader(f))

def score(row):
    return sum(float(row[c]) / 5.0 * weights[c] for c in criteria)

def sort_key(row):
    return (score(row),) + tuple(float(row[c]) for c in TIE)

ordered = sorted(rows, key=sort_key, reverse=True)
for rank, row in enumerate(ordered, 1):
    calculated = score(row)
    published = float(row["total_score_exact"])
    if abs(calculated - published) > 1e-9:
        raise SystemExit(
            f"Score mismatch for {row['participant']}: calculated={calculated}, published={published}"
        )
    if int(row["rank"]) != rank:
        raise SystemExit(
            f"Rank mismatch for {row['participant']}: calculated={rank}, published={row['rank']}"
        )
    print(f"{rank}\t{row['participant']}\t{calculated:.10g}")