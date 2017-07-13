from enum import IntEnum

class ErrorCode(IntEnum):
    Success = 0
    CommonInvalidParam1 = 100


class IndyError(Exception):
    error_code: ErrorCode

    def __init__(self, error_code: ErrorCode):
        self.error_code = error_code
