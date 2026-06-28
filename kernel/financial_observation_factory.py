from kernel.financial_observation import FinancialObservation


class FinancialObservationFactory:

    DEFAULT_SCOPE = "GroupScope"

    DEFAULT_CURRENCY = "KenyanShilling"

    DEFAULT_SCALE = "Million"

    DEFAULT_MEASUREMENT_UNIT = "MonetaryValue"

    DEFAULT_STATUS = "Verified"

    DEFAULT_CONFIDENCE = "HighConfidence"

    @staticmethod
    def create(
        *,
        identifier: str,
        company: str,
        metric: str,
        reporting_period: str,
        value: str,
        evidence: str,
        citation: str,
        reporting_scope: str | None = None,
        currency: str | None = None,
        scale: str | None = None,
        measurement_unit: str | None = None,
        observation_status: str | None = None,
        observation_confidence: str | None = None,
    ) -> FinancialObservation:

        return FinancialObservation(

            identifier=identifier,

            company=company,

            reporting_scope=(
                reporting_scope
                or FinancialObservationFactory.DEFAULT_SCOPE
            ),

            metric=metric,

            reporting_period=reporting_period,

            value=value,

            currency=(
                currency
                or FinancialObservationFactory.DEFAULT_CURRENCY
            ),

            scale=(
                scale
                or FinancialObservationFactory.DEFAULT_SCALE
            ),

            measurement_unit=(
                measurement_unit
                or FinancialObservationFactory.DEFAULT_MEASUREMENT_UNIT
            ),

            evidence=evidence,

            citation=citation,

            observation_status=(
                observation_status
                or FinancialObservationFactory.DEFAULT_STATUS
            ),

            observation_confidence=(
                observation_confidence
                or FinancialObservationFactory.DEFAULT_CONFIDENCE
            ),
        )
