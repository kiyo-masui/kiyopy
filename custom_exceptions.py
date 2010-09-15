"""Custom Exceptions."""

class DataError(Exception) :
    """Exception to raise if data of some sort is invalid or does not have
    expected properties."""
    pass

class FileParameterTypeError(TypeError) :
    """Exception to raise if a parameter read from file should be a certain
    type and is not."""
    pass
