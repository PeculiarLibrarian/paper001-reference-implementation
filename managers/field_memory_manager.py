from contracts.data_contract import FieldMemoryBundle


class FieldMemoryManager:

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
            "instances": {
                "system": {
                    "competencies": [],
                    "opportunities": [],
                    "meta": "initialized"
                }
            }
        }
