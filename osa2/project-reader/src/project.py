class Project:
    def __init__(self, name, description, dependencies, dev_dependencies):
        self.name = name
        self.description = description
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    def __str__(self):
        return (
            f"Name: {self.name}\n"
            f"Description: {self.description}\n"
            f"Dependencies:\n- " + "\n- ".join(self.dependencies) + "\n\n"
            f"Development dependencies:\n- " + "\n- ".join(self.dev_dependencies)
        )
