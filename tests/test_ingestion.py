from managers.ingestion_manager import IngestionManager
from rdflib import Graph

ing = IngestionManager()

# Test 1: RDF Graph passthrough
g = Graph()
g2 = ing.load(g)

print("TEST 1 TYPE:", type(g2))

# Test 2: TTL string ingestion (minimal safe case)
ttl = """
@prefix ex: <http://example.org/> .
ex:a ex:rel ex:b .
"""

g3 = ing.load(ttl)

print("TEST 2 TYPE:", type(g3))
print("VALIDATION:", ing.validate(g3))

# Test 3: expose identity
print("EXPOSE TYPE:", type(ing.expose(g3)))
