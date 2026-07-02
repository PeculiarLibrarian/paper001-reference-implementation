import json
import hashlib
import os

def canon(x):
    return x.strip().lower().replace(" ", "-")

PREFIXES = """
@prefix fin: <https://peculiarlibrary.org/ontology/finance#> .
@prefix core: <https://peculiarlibrary.org/ontology/core#> .
@prefix org: <https://peculiarlibrary.org/ontology/organization#> .
"""

def compile_row(row):
    obs = f"saf-fin:obs-{canon(row['metric'])}-{canon(row['entity'])}-2024-04-01"
    res = f"saf-fin:res-{row['fact_id']}"

    return f"""
{obs}
    a fin:{row['type']} ;
    fin:observedEntity org:{canon(row['entity'])} ;
    core:hasResult {res} ;
    fin:amount {row['value']} ;
    fin:currency "{row['currency']}" .
"""

data = json.load(open("repo/meta/fy2025_crf_seed.json"))

ttl = PREFIXES + "\n"

for r in data:
    ttl += compile_row(r)

out = "repo/staging/fy2025_seed.ttl"
open(out, "w").write(ttl)

print("RDF compiled:", out)
