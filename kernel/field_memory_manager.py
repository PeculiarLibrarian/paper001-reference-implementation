class FieldMemoryManager:

    def __init__(self):
        self.state = {
            "field_history": []
        }

    def update(self, field):

        self.state["field_history"].append(field)

        return field
