class FieldResolver:

    @staticmethod
    def pick(row, *keys):

        for k in keys:
            if k in row and row[k] not in [None, "", 0.0]:
                return row[k]

        return None
