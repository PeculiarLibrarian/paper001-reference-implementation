from kernel.query_registry import QueryRegistry


class QueryLoader:

    @staticmethod
    def load(name):

        path = QueryRegistry.core(name)

        if not path.exists():

            raise FileNotFoundError(path)

        return path.read_text()

