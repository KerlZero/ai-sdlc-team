from pathlib import Path

def save_playwright_files(files: dict[str, str], base_dir: str = "../automation"):
    base_path = Path(base_dir).resolve()

    for relative_path, content in files.items():
        target_path = (base_path / relative_path).resolve()

        if not str(target_path).startswith(str(base_path)):
            raise ValueError(f"Invalid path detected: {relative_path}")

        target_path.parent.mkdir(parents=True, exist_ok=True)
        target_path.write_text(content, encoding="utf-8")
