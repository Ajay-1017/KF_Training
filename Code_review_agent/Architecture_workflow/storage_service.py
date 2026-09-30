from pathlib import Path


STORAGE_ROOT = Path("storage")

def save_source_code(job_id: int, source_code: str):

    job_directory = STORAGE_ROOT / "reviews" / str(job_id)

    job_directory.mkdir(parents=True, exist_ok=True)

    source_path = job_directory / "source.py"

    source_path.write_text(source_code, encoding="utf-8")

    return str(source_path)


def read_source_code(source_location: str):

    source_path = Path(source_location)

    return source_path.read_text(encoding="utf-8")