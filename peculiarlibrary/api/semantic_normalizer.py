class SemanticNormalizer:

    def normalize_triple(self, s, p, o):
        """
        Ensures consistent semantic structure for reasoning
        """

        # Normalize numeric values
        try:
            if isinstance(o, str) and o.replace('.', '', 1).isdigit():
                o = float(o)
        except:
            pass

        return (s, p, o)
