from typing import Dict, Any


class CollectionContract:

    REQUIRED_FIELDS = {

        "collection",

        "root",

        "ontology",

        "taxonomy",

        "queries",

        "shapes",

        "instances",

    }

    @staticmethod
    def validate(collection: Dict[str, Any]):

        missing = [

            field

            for field in CollectionContract.REQUIRED_FIELDS

            if field not in collection

        ]

        return {

            "valid": len(missing) == 0,

            "missing": missing,

        }

