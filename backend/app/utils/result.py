from typing import Optional
from unittest import result

from pydantic import BaseModel

from app.utils.constant import Constant

class Result[T](BaseModel):
    success: Optional[bool] = True
    message: Optional[str] = ""
    code: Optional[int] = 0
    result: Optional[T] = None

    @staticmethod
    def ok(msg: str = "", data: T = None) -> "Result[T]":
        return Result(success=True, code=Constant.RESULT_CODE_OK, message=msg, result=data)