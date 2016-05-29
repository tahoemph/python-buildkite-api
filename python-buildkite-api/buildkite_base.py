import abc

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
