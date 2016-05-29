import requests

class BuildkiteOrganizations(object):
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

    def list(self):
        url = self.parent_object.build_request(('auth', 'organizations'))
        r = requests.get(url)
        return r.json()

    def set_organization(self, org):
        self.organization = org
        return self.parent_object
