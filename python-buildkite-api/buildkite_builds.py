from buildkite_base import BuildkiteBase

class BuildkiteBuilds(BuildkiteBase):
    def __init__(self):
        self.pipeline = None

    def set_parent(self, parent):
        self.parent_object = parent

    def url_parts(self):
        rv = ["builds"]
        if self.pipeline:
            rv.append(self.pipeline)
        return rv

    def url_parameters(self):
        return []

    # TODO: a protocol where if the sub-object (e.g. organization) doesn't
    # have a parameter it does something reasonable (stays out of the way).
    def list(self, build=None, organization=False, pipeline=False):
        if pipeline and not organization:
            raise ValueError
        arguments = []
        if organization:
            arguments.append('organizations')
        if pipeline:
            arguments.append('pipelines')
        arguments.append('builds')
        if build:
            arguments.append(build)
        url = self.parent_object.build_request(arguments)
        return self.formatted_request(url)

    def set_pipeline(self, pipeline):
        self.pipeline = pipeline
        return self.parent_object
