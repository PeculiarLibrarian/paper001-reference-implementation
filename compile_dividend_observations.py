from kernel.financial_observation_factory import FinancialObservationFactory
from kernel.observation_collection_builder import ObservationCollectionBuilder

observations = [

    FinancialObservationFactory.create(
        identifier="SafaricomDividendFY2021",
        company="SafaricomPLC",
        metric="DividendPerShare",
        reporting_period="FY2021",
        value="1.37",
        scale="NoScale",
        measurement_unit="PerShare",
        evidence="SafaricomAnnualReport2021",
        citation="SafaricomDividendCitationFY2021",
    ),

    FinancialObservationFactory.create(
        identifier="SafaricomDividendFY2022",
        company="SafaricomPLC",
        metric="DividendPerShare",
        reporting_period="FY2022",
        value="1.39",
        scale="NoScale",
        measurement_unit="PerShare",
        evidence="SafaricomAnnualReport2022",
        citation="SafaricomDividendCitationFY2022",
    ),

    FinancialObservationFactory.create(
        identifier="SafaricomDividendFY2023",
        company="SafaricomPLC",
        metric="DividendPerShare",
        reporting_period="FY2023",
        value="1.20",
        scale="NoScale",
        measurement_unit="PerShare",
        evidence="SafaricomAnnualReport2023",
        citation="SafaricomDividendCitationFY2023",
    ),

    FinancialObservationFactory.create(
        identifier="SafaricomDividendFY2024",
        company="SafaricomPLC",
        metric="DividendPerShare",
        reporting_period="FY2024",
        value="1.20",
        scale="NoScale",
        measurement_unit="PerShare",
        evidence="SafaricomAnnualReport2024",
        citation="SafaricomDividendCitationFY2024",
    ),

    FinancialObservationFactory.create(
        identifier="SafaricomDividendFY2025",
        company="SafaricomPLC",
        metric="DividendPerShare",
        reporting_period="FY2025",
        value="1.20",
        scale="NoScale",
        measurement_unit="PerShare",
        evidence="SafaricomAnnualReport2025",
        citation="SafaricomDividendCitationFY2025",
    ),

]

ObservationCollectionBuilder.write(
    path="schemas/finance/knowledge/safaricom_dividend_observations.ttl",
    title="Dividend Per Share Observations",
    observations=observations,
)

print("✓ Dividend observations compiled successfully.")
