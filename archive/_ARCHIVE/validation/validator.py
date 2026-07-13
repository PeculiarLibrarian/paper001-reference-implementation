class Validator:

    def validate(self, dataset, commands, graph):
        self.validate_dataset(dataset)
        self.validate_commands(commands)
        self.validate_graph(graph)

    def validate_dataset(self, dataset):
        if dataset is None:
            raise ValueError("Invalid dataset")
        return True

    def validate_commands(self, commands):
        if not isinstance(commands, list):
            raise ValueError("Commands must be list")
        return True

    def validate_graph(self, graph):
        # graph may be None during early compilation stages
        return True
