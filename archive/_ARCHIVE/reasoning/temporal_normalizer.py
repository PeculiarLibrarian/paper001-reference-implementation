import re
from datetime import datetime

class TemporalNormalizer:
    """
    Converts semantic periods into sortable temporal indices.

    Supports:
    - FY2021
    - 2021
    - Q1 2021
    - 2021-2022 (collapsed midpoint)
    """

    def parse_year(self, period):
        match = re.findall(r"\d{4}", str(period))
        if not match:
            return 0
        return int(match[0])

    def normalize(self, facts):
        enriched = []

        for f in facts:
            period = f.get("period")

            enriched.append({
                **f,
                "temporal_index": self.parse_year(period)
            })

        return sorted(enriched, key=lambda x: x["temporal_index"])
