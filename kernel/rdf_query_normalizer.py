from rdflib.term import Literal, URIRef

class RDFQueryNormalizer:

    @staticmethod
    def normalize_row(row):

        normalized = {}

        for key in row.labels:

            value = row[key]

            # URI → string
            if isinstance(value, URIRef):
                normalized[key] = str(value)

            # Literal → correct type
            elif isinstance(value, Literal):

                try:
                    if value.datatype:
                        dt = str(value.datatype)

                        if "decimal" in dt or "float" in dt:
                            normalized[key] = float(value)
                        elif "integer" in dt:
                            normalized[key] = int(value)
                        else:
                            normalized[key] = str(value)
                    else:
                        normalized[key] = str(value)
                except Exception:
                    normalized[key] = str(value)

            else:
                normalized[key] = value

        return normalized
