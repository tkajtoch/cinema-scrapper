class BaseDataParser(object):
    def parse(self, input_data, parameters):
        raise NotImplementedError("Not implemented yet")


class DataParseInputError(Exception):
    pass
