from kernel.financial_observation_factory import FinancialObservationFactory
from kernel.observation_collection_builder import ObservationCollectionBuilder

observations = [

    FinancialObservationFactory.create(
        identifier="SafaricomEPSFY2021",
        company="SafaricomPLC",
        metric="EarningsPerShare",
        reporting_period="FY2021",
        value="1.71",
        scale="NoScale",
        measurement_unit="PerShare",
        evidence="SafaricomAnnualReport2021",
        citation="SafaricomEPSCitationFY2021",
    ),

    FinancialObservationFactory.create(
        identifier="SafaricomEPSFY2022",
        company="SafaricomPLC",
        metric="EarningsPerShare",
        reporting_period="FY2022",
        value="1.74",
        scale="NoScale",
        measurement_unit="PerShare",
        evidence="SafaricomAnnualReport2022",
        citation="SafaricomEPSCitationFY2022",
    ),

    FinancialObservationFactory.create(
        identifier="SafaricomEPSFY2023",
        company="SafaricomPLC",
        metric="EarningsPerShare",
        reporting_period="FY2023",
        value="1.60",
        scale="NoScale",
        measurement_unit="PerShare",
        evidence="SafaricomAnnualReport2023",
        citation="SafaricomEPSCitationFY2023",
    ),

    FinancialObservationFactory.create(
        identifier="SafaricomEPSFY2024",
        company="SafaricomPLC",
        metric="EarningsPerShare",
        reporting_period="FY2024",
        value="1.60",
        scale="NoScale",
        measurement_unit="PerShare",
        evidence="SafaricomAnnualReport2024",
        citation="SafaricomEPSCitationFY2024",
    ),

    FinancialObservationFactory.create(
        identifier="SafaricomEPSFY2025",
        company="SafaricomPLC",
        metric="EarningsPerShare",
        reporting_period="FY2025",
        value="1.70",
        scale="NoScale",
        measurement_unit="PerShare",
        evidence="SafaricomAnnualReport2025",
        citation="SafaricomEPSCitationFY2025",
    ),

]

ObservationCollectionBuilder.write(
    path="schemas/finance/knowledge/safaricom_eps_observations.ttl",
    title="Earnings Per Share Observations",
    observations=observations,
)

print("✓ EPS observations compiled successfully.")
