class BaseDataSource(object):
    name = ''
    display_name = ''

    def connect(self):
        raise NotImplementedError("Not implemented yet")

    def fetch(self, cinema, date):
        raise NotImplementedError("Not implemeneted yet")

    def close(self):
        raise NotImplementedError("Not implemented yet")
