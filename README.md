1. Setup:
    - `uv venv -p 3.11`
    - `uv pip install -r requirements.txt`
2. CLI:
    - (If you havea`src`folder:set`PYTHONPATH=src` first)
    - `uv run python -m csv_profiler.cli profile data sample.csv --out-dir outputs`
3. Verify:
    - `outputs/report.json`and `outputs/report.md` exist
4. GUI:
    - (If you have a `src/` folder: set `PYTHONPATH=src` first)
    - `uv run streamlit run src/app.py`
5. Export:
    - download JSON + Markdown from the UI



## Smoke Test

1) Run the CLI:
    # If you have a `src/` folder: set `PYTHONPATH=src` first
    uv run python -m csv_profiler.cli profile data/sample.csv --out-dir outputs

2) Check the output files exist:
    # Mac/Linux
    ls outputs
    
    # Windows PowerShell
    dir outputs
    
You should see `report.json` and `report.md`.

## Image
<img width="1916" height="854" alt="image" src="https://github.com/user-attachments/assets/870dbb38-38da-45ab-9cf3-0ed60dbb470c" />
<img width="905" height="872" alt="image" src="https://github.com/user-attachments/assets/b76cb470-3f02-4609-ae79-e42ebb381022" />

