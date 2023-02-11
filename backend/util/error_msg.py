class NotFoundError(Exception):
    message = "The specified resource is not found."

    def __str__(self):
        return NotFoundError.message


class ResourceUnavailableError(Exception):
    message = "The specified resource is unavailable."

    def __str__(self):
        return ResourceUnavailableError.message


class OperationIsForbiddenError(Exception):
    message = "The operation is forbidden."

    def __str__(self):
        return OperationIsForbiddenError.message
