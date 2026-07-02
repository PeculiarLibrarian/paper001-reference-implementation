from rdflib import (
    Graph,
    Literal,
    RDF,
    RDFS,
    Namespace,
    OWL,
    XSD,
    BNode,
)
from rdflib.namespace import SH, SKOS

PADI = Namespace("http://padi.s.m.gitandu.bs/core#")

g = Graph()

g.bind("rdf", RDF)
g.bind("rdfs", RDFS)
g.bind("owl", OWL)
g.bind("sh", SH)
g.bind("skos", SKOS)
g.bind("xsd", XSD)
g.bind("padi", PADI)

# ------------------------------------------------------------------
# Ontology Metadata
# ------------------------------------------------------------------

ONTOLOGY = PADI[""]

g.add((ONTOLOGY, RDF.type, OWL.Ontology))
g.add((ONTOLOGY, RDFS.label, Literal("PADI Core Constitution")))
g.add((
    ONTOLOGY,
    RDFS.comment,
    Literal(
        "Constitutional ontology defining the invariant semantic "
        "contracts shared by every Peculiar Library domain."
    ),
))
g.add((ONTOLOGY, OWL.versionInfo, Literal("0.2.2")))

# ------------------------------------------------------------------
# Root Classes
# ------------------------------------------------------------------

classes = {
    PADI.Entity:
        ("Entity",
         "Root class for every semantic object."),

    PADI.Organization:
        ("Organization",
         "A legally or administratively recognised institutional entity."),

    PADI.Person:
        ("Person",
         "A natural human being."),

    PADI.Country:
        ("Country",
         "A sovereign geopolitical entity."),

    PADI.Jurisdiction:
        ("Jurisdiction",
         "A territorial or legal boundary of authority."),

    PADI.ReportingPeriod:
        ("Reporting Period",
         "A bounded reporting interval."),

    PADI.LegalStatus:
        ("Legal Status",
         "The legal classification of an organisation."),
}

for cls, (label, comment) in classes.items():

    g.add((cls, RDF.type, OWL.Class))
    g.add((cls, RDFS.label, Literal(label)))
    g.add((cls, RDFS.comment, Literal(comment)))

    if cls != PADI.Entity:
        g.add((cls, RDFS.subClassOf, PADI.Entity))

# ------------------------------------------------------------------
# Constitutional Properties
# ------------------------------------------------------------------

properties = [

    (
        PADI.identifier,
        OWL.DatatypeProperty,
        PADI.Entity,
        XSD.string,
        "Identifier",
        "Canonical immutable identifier.",
        True,
    ),

    (
        PADI.hasLegalStatus,
        OWL.ObjectProperty,
        PADI.Organization,
        PADI.LegalStatus,
        "Legal status",
        "Associates an organisation with its legal status.",
        True,
    ),

    (
        PADI.hasJurisdiction,
        OWL.ObjectProperty,
        PADI.Organization,
        PADI.Jurisdiction,
        "Jurisdiction",
        "Associates an organisation with its jurisdiction.",
        True,
    ),

    (
        PADI.hasReportingPeriod,
        OWL.ObjectProperty,
        PADI.Organization,
        PADI.ReportingPeriod,
        "Reporting period",
        "Associates an organisation with a reporting period.",
        True,
    ),
]

for uri, ptype, domain, range_, label, comment, functional in properties:

    g.add((uri, RDF.type, ptype))

    if functional:
        g.add((uri, RDF.type, OWL.FunctionalProperty))

    g.add((uri, RDFS.domain, domain))
    g.add((uri, RDFS.range, range_))
    g.add((uri, RDFS.label, Literal(label)))
    g.add((uri, RDFS.comment, Literal(comment)))

# ------------------------------------------------------------------
# SHACL Constitutional Contract
# ------------------------------------------------------------------

shape = PADI.OrganizationShape

g.add((shape, RDF.type, SH.NodeShape))
g.add((shape, SH.targetClass, PADI.Organization))

def constraint(path,
               minimum,
               maximum=None,
               datatype=None,
               target_class=None):

    node = BNode()

    g.add((shape, SH.property, node))
    g.add((node, SH.path, path))
    g.add((node, SH.minCount, Literal(minimum)))

    if maximum is not None:
        g.add((node, SH.maxCount, Literal(maximum)))

    if datatype is not None:
        g.add((node, SH.datatype, datatype))

    if target_class is not None:
        g.add((node, SH["class"], target_class))

constraint(PADI.identifier, 1, 1, datatype=XSD.string)
constraint(SKOS.prefLabel, 1, 1, datatype=XSD.string)
constraint(PADI.hasLegalStatus, 1, 1, target_class=PADI.LegalStatus)
constraint(PADI.hasJurisdiction, 1, target_class=PADI.Jurisdiction)
constraint(PADI.hasReportingPeriod, 1, target_class=PADI.ReportingPeriod)

# ------------------------------------------------------------------
# Constitutional Disjointness
# ------------------------------------------------------------------

g.add((PADI.Organization, OWL.disjointWith, PADI.Person))
g.add((PADI.Organization, OWL.disjointWith, PADI.Country))

# ------------------------------------------------------------------
# Serialize
# ------------------------------------------------------------------

print(g.serialize(format="turtle"))

