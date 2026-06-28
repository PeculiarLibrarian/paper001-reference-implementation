from rdflib.term import Literal, URIRef

class RDFCoercer:

    @staticmethod
    def convert(value):

        # URI → string
        if isinstance(value, URIRef):
            return str(value)

        # Literal → native python
        if isinstance(value, Literal):

            try:
                if value.datatype:
                    dt = str(value.datatype)

                    if "decimal" in dt or "float" in dt:
                        return float(value)

                    if "integer" in dt:
                        return int(value)
            except Exception:
                pass

            return str(value)

        return value
