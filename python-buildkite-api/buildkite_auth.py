class BuildkiteAuth(object):
    def set_parent(self, parent):
        self.parent_object = parent

    def access_token(self, t):
        self.token = t

    def url_parts(self):
        return []

    def url_parameters(self):
        return ["access_token=" + self.token]
