import abc
import requests

class BuildkiteBase(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def url_parts(self):
        """What should be concatenated to make these parts of the URL"""
        pass

    @abc.abstractmethod
    def url_parameters(self):
        """What should be concatenated to make the parameter string."""
        pass

    def formatted_request(self, url):
        r = requests.get(url)
        if r.status_code != 200:
            msg = "status code {} {}".format(r.status_code, r.text)
            raise Exception(msg)
        return r.json()
