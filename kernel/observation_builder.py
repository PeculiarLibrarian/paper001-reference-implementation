from kernel.financial_observation import FinancialObservation


class ObservationBuilder:

    @staticmethod
    def build(observation: FinancialObservation) -> str:

        return f"""
fin:{observation.identifier}
    rdf:type fin:Observation ;
    fin:observesCompany fin:{observation.company} ;
    fin:hasReportingScope fin:{observation.reporting_scope} ;
    fin:hasMetric fin:{observation.metric} ;
    fin:hasReportingPeriod fin:{observation.reporting_period} ;
    fin:value "{observation.value}"^^xsd:decimal ;
    fin:hasCurrency fin:{observation.currency} ;
    fin:hasScale fin:{observation.scale} ;
    fin:hasMeasurementUnit fin:{observation.measurement_unit} ;
    fin:derivedFromEvidence fin:{observation.evidence} ;
    fin:hasCitation fin:{observation.citation} ;
    fin:hasObservationStatus fin:{observation.observation_status} ;
    fin:hasObservationConfidence fin:{observation.observation_confidence} .
""".strip()
