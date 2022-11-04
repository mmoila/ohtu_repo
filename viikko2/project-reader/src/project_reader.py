from urllib import request
from project import Project
import toml

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        parsed_content = toml.loads(content)
        tool_content = parsed_content["tool"]["poetry"]
        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(
            tool_content["name"],
            tool_content["description"],
            list(tool_content["dependencies"]),
            list(tool_content["dev-dependencies"])
            )
