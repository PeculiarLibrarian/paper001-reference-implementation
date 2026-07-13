from pathlib import Path
import json

from padi.semantic.entity import Entity
from padi.semantic.metric import Metric
from padi.semantic.reporting_period import ReportingPeriod
from padi.semantic.measurement_unit import MeasurementUnit
from padi.semantic.source_document import SourceDocument
from padi.semantic.source_record import SourceRecord
from padi.semantic.canonical_fact import CanonicalFact


class IngestionPipeline:
    """
    Deterministic semantic ingestion.

    Responsibility:

        Raw dataset
            ↓
        Canonical semantic objects

    Never produces RDF.
    """

    def compile(self, dataset_path):
        return self.load_dataset(dataset_path)

    def load_dataset(self, dataset_path):

        path = Path(dataset_path)

        if not path.exists():
            raise FileNotFoundError(dataset_path)

        if dataset_path.endswith(".json"):
            return self._load_json(path)

        raise ValueError("Only canonical JSON datasets are supported.")

    def _load_json(self, path):

        with open(path, "r") as f:
            data = json.load(f)

        facts = []

        for item in data.get("facts", []):

            src = item.get("source")

            source = None

            if src:

                document = SourceDocument(
                    title=src["document"],
                    filename=src["document"],
                )

                source = SourceRecord(
                    document=document,
                    page=src.get("page"),
                    section=src.get("section"),
                    context=src.get("context"),
                )

            facts.append(

                CanonicalFact(

                    entity=Entity(item["subject"]),

                    metric=Metric(item["predicate"]),

                    value=item["object"],

                    period=ReportingPeriod(item["period"]),

                    unit=MeasurementUnit(item["unit"])
                    if item.get("unit")
                    else None,

                    source=source,

                    confidence=item.get("confidence", 1.0),
                )
            )

        return {
            "__type__": "canonical.dataset",
            "facts": facts,
        }
