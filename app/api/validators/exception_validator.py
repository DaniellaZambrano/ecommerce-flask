class ValidationException(Exception):
    """Exception raised for validations.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message="Error"):
        self.message = message
        super().__init__(self.message)