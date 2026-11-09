from urllib.request import urlopen
import tomli
from project import Project

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        content = urlopen(self._url).read().decode("utf-8")

        parsed_data = tomli.loads(content)

        name = parsed_data.get("project", {}).get("name", "")
        description = parsed_data.get("project", {}).get("description", "")
        dependencies = parsed_data.get("project", {}).get("dependencies", [])
        dev_dependencies = parsed_data.get("dependency-groups", {}).get("dev", [])

        return Project(name, description, dependencies, dev_dependencies)
