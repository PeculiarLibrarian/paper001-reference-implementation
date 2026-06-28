from pathlib import Path

class QueryRegistry:

    ROOT = Path("schemas/queries")

    @classmethod
    def query(cls, *parts):
        return cls.ROOT.joinpath(*parts)

    @classmethod
    def core(cls, name):
        return cls.query("core", f"{name}.sparql")

    @classmethod
    def finance(cls, name):
        return cls.query("finance", f"{name}.sparql")
