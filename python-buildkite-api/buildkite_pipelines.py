import requests

class BuildkitePipelines(object):
    def __init__(self):
        self.pipeline = None

    def set_parent(self, parent):
        self.parent_object = parent

    def url_parts(self):
        rv = ["pipelines"]
        if self.pipeline:
            rv.append(self.pipeline)
        return rv

    def url_parameters(self):
        return []

    def list(self):
        url = self.parent_object.build_request(('auth',
                                                'organizations',
                                                'pipelines'))
        r = requests.get(url)
        return r.json()

    def set_pipeline(self, pipeline):
        self.pipeline = pipeline
        return self.parent_object
