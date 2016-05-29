from buildkite_base import BuildkiteBase
import requests

class BuildkiteOrganizations(BuildkiteBase):
    def __init__(self):
        self.organization = None

    def set_parent(self, parent):
        self.parent_object = parent

    def url_parts(self):
        rv = ["organizations"]
        if self.organization:
            rv.append(self.organization)
        return rv

    def url_parameters(self):
        return []

    def list(self, org=None):
        path_components = ['auth', 'organizations']
        if org:
            path_components.append(org)
        url = self.parent_object.build_request(path_components)
        r = requests.get(url)
        return r.json()

    def set_organization(self, org):
        self.organization = org
        return self.parent_object
