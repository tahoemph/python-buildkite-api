from buildkite_auth import BuildkiteAuth
from buildkite_base import BuildkiteBase
from buildkite_builds import BuildkiteBuilds
from buildkite_organizations import BuildkiteOrganizations
from buildkite_pipelines import BuildkitePipelines

class Buildkite(BuildkiteBase):
    def __init__(self):
        self.api_objects = {
            'auth': BuildkiteAuth(),
            'organizations': BuildkiteOrganizations(),
            'pipelines': BuildkitePipelines(),
            'builds': BuildkiteBuilds()
        }
        for k in self.api_objects:
            self.api_objects[k].set_parent(self)

    def build_request(self, url_pieces):
        url = self.url_parts()
        parameters = []
        for index, piece in enumerate(url_pieces):
            protocol_object = self.api_objects.get(piece)
            # If the last component isn't an object then treat it like
            # a slug.
            if not protocol_object and index == len(url_pieces) - 1:
                url_parts = [piece]
                parameter_parts = []
            else:
                url_parts = protocol_object.url_parts()
                parameter_parts = protocol_object.url_parameters()
            for part in url_parts:
                url = '/'.join((url, part))
            parameters.extend(parameter_parts)
        if parameters:
            url = url + '?' + ''.join(parameters)
        return url

    def url_parts(self):
        return "https://api.buildkite.com/v2"

    def url_parameters(self):
        return []

    # TODO: generate these from the api_objects map.
    def auth(self):
        return self.api_objects['auth']

    def organization(self):
        return self.api_objects['organizations']

    def pipelines(self):
        return self.api_objects['pipelines']

    def builds(self):
        return self.api_objects['builds']
