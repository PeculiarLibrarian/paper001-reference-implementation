"""
Canonical Mapper
Version: 1.1.0

Produces immutable semantic objects.
"""

from padi.semantic.canonical_fact import CanonicalFact
from padi.semantic.source_document import SourceDocument
from padi.semantic.source_record import SourceRecord


class CanonicalMapper:

    VERSION = "1.1.0"

    def map(self, dataset):

        facts = []

        for row in dataset["facts"]:

            src = row.get("source")

            source_record = None

            if src:

                document = SourceDocument(
                    title=src["document"].replace("_", " ").replace(".pdf", ""),
                    filename=src["document"],
                )

                source_record = SourceRecord(
                    document=document,
                    page=src.get("page"),
                    section=src.get("section"),
                    context=src.get("context"),
                )

            facts.append(

                CanonicalFact(
                    entity=row["subject"],
                    metric=row["predicate"],
                    value=row["object"],
                    period=row["period"],
                    unit=row.get("unit"),
                    source=source_record,
                    confidence=row.get("confidence"),
                )

            )

        return facts
