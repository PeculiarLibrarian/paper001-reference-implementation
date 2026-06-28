from pathlib import Path

from kernel.financial_observation import FinancialObservation
from kernel.observation_builder import ObservationBuilder


class ObservationCollectionBuilder:

    PREFIXES = """@prefix rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .

@prefix fin: <https://peculiarlibrarian.org/finance/> .
"""

    @staticmethod
    def build(
        title: str,
        observations: list[FinancialObservation],
    ) -> str:

        blocks = [
            ObservationBuilder.build(observation)
            for observation in observations
        ]

        return (
            ObservationCollectionBuilder.PREFIXES
            + "\n\n"
            + "####################################################\n"
            + f"# {title}\n"
            + "####################################################\n\n"
            + "\n\n".join(blocks)
            + "\n"
        )

    @staticmethod
    def write(
        path: str,
        title: str,
        observations: list[FinancialObservation],
    ) -> None:

        Path(path).write_text(
            ObservationCollectionBuilder.build(
                title=title,
                observations=observations,
            ),
            encoding="utf-8",
        )
