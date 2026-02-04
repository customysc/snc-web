import os
import uuid
from http.client import HTTPException
from pathlib import Path

from fastapi import UploadFile, File, APIRouter
from fastapi.responses import FileResponse

from app.api.static.dto import FileDto
from app.api.static.static_constant import StaticConstant
from app.utils.result import Result

BASEDIR = Path(__file__).resolve().parents[4]
UPLOAD_DIR = BASEDIR / StaticConstant.UPLOAD_DIR
print(BASEDIR)
print(UPLOAD_DIR)
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

router = APIRouter(prefix="/static", tags=["static"])

@router.post("/upload", response_model=Result[FileDto])
async def update(file: UploadFile = File(...)):
    data = await file.read()
    size = len(data)

    if size == 0:
        return Result.error("文件为空！")
    if size > StaticConstant.MAX_FILE_SIZE:
        return Result.error("文件过大！")

    # TODO 文件扩展名校验
    # TODO 原始文件名预处理
    ext = Path(file.filename).suffix
    uuid_name = uuid.uuid4().hex + ext
    save_path = UPLOAD_DIR / uuid_name

    save_path.write_bytes(data)

    return Result.ok(msg="上传成功！", data=FileDto(name=uuid_name))

@router.get("/file/{filename}")
def view(filename: str):
    filename = os.path.basename(filename)
    path = UPLOAD_DIR / filename
    if not path.exists() or not path.is_file():
        raise HTTPException(404, "No such file or directory")
    return FileResponse(path)