from contracts.data_contract import TaxonomyBundle


class TaxonomyManager:

    def discover(self):
        return self

    def load(self):
        return self

    def parse(self):
        return self

    def bind(self, context):
        return context

    def validate(self, context):
        return True

    def expose(self):

        return {
            "taxonomy_instances": {
                "competency_map": ["Query", "Reasoning", "Ontology"]
            }
        }
