# AI Coding Agent Instructions for FAANG Stock Analysis Project

## Project Overview
This is a simple data analysis pipeline for plotting FAANG stock prices. It downloads recent hourly data using yfinance, processes multi-index CSV files, generates matplotlib plots, and automates execution via GitHub Actions.

## Key Components
- `faang.py`: Main script that reads latest CSV from `data/` and generates timestamped plot in `plots/`
- `problems.ipynb`: Jupyter notebook containing development code for data download and plotting functions
- `.github/workflows/github-actions-demo.yml`: Automated workflow that runs `faang.py` weekly and commits new plots

## Data Flow
1. `get_data()` in notebook downloads 5-day hourly data for ["META", "AAPL", "AMZN", "NFLX", "GOOG"] using `yf.download(tickers, period="5d", interval="1h")`
2. Saves as multi-index CSV in `data/` with timestamp filename (e.g., `20251220-205019.csv`)
3. `plot_data()` reads latest CSV with `pd.read_csv(..., header=[0,1], index_col=0, parse_dates=True)`
4. Accesses close prices via `df["Close"]["META"]` etc.
5. Generates single figure with all 5 stocks, saves as PNG in `plots/` with current timestamp

## Developer Workflows
- Run locally: `python faang.py` (requires data files in `data/`)
- Install deps: `pip install -r requirements.txt` (includes yfinance, pandas, matplotlib)
- Data format: Always use multi-index CSV with Price/Ticker headers from yfinance
- Plotting: Single figure for all stocks, timestamped PNG filenames

## Conventions
- Folder structure: `data/` for input CSVs, `plots/` for output PNGs
- Filenames: Timestamp format `%Y%m%d-%H%M%S` for both data and plots
- Stock selection: Hardcoded FAANG list - modify `tickers` list if adding/removing
- Plot style: Line plot with labels, legend, date title from `df.index[-1].date()`
- Automation: GitHub Actions commits plots back to main branch automatically

## Dependencies
- yfinance for data download (not in standard library)
- pandas for multi-index DataFrame handling
- matplotlib for plotting (use `plt.close()` to avoid memory issues)

## Automation
- Workflow triggers: Manual (`workflow_dispatch`) or weekly Saturday 08:03 UTC
- Steps: Checkout, setup Python, install deps, run script, commit plots
- Permissions: `contents: write` required for auto-commits</content>
<parameter name="filePath">/workspaces/computer-infrastructure.my-assessment/.github/copilot-instructions.md