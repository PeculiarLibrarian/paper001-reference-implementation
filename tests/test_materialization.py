from padi.materializer.rdf_materializer import RDFMaterializer
from padi.semantic.canonical_fact import CanonicalFact
from padi.semantic.source_document import SourceDocument
from padi.semantic.source_record import SourceRecord


def test_with_source():
    fact = CanonicalFact(
        entity="Safaricom PLC",
        metric="service_revenue",
        value=371415.4,
        period="FY2025",
        unit="KES Millions",
        source=SourceRecord(
            document=SourceDocument(
                title="Annual Report 2025",
                filename="2025_Annual_Report.pdf"
            ),
            page=49,
            section="Notes",
            context="Service revenue line item",
        ),
        confidence=1.0,
    )

    g = RDFMaterializer().materialize([fact])

    print("WITH SOURCE")
    print("Triples:", len(g))
    assert len(g) > 0


def test_without_source():
    fact = CanonicalFact(
        entity="Test Entity",
        metric="service_revenue",
        value=100,
        period="FY2025",
        unit="KES",
        source=None,
        confidence=1.0,
    )

    g = RDFMaterializer().materialize([fact])

    print("\nWITHOUT SOURCE")
    print("Triples:", len(g))
    assert len(g) > 0


if __name__ == "__main__":
    test_with_source()
    test_without_source()
    print("\n✓ MATERIALIZER VALIDATION PASSED")
