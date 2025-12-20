## Overview
This repository contains a data analysis pipeline for plotting FAANG stock prices. It includes data download, processing, visualization, and automation components.

## Contents

### problems.ipynb
A Jupyter notebook containing the assessment problems and solutions.

#### Problem 1: Data from yfinance
- Downloads the last 5 days of hourly data for FAANG stocks using yfinance
- Saves data as timestamped CSV files in the `data/` folder

#### Problem 2: Plotting Data
- Reads the latest CSV from `data/`
- Plots Close prices for all FAANG stocks on a single figure
- Saves the plot as a timestamped PNG in `plots/`

#### Problem 3: Script
The script `faang.py` automates the plotting process:

1. Finds the latest CSV file in the `data` folder.
2. Reads the Close prices for five FAANG stocks.
3. Plots all stock prices on a single figure.
4. Adds axis labels, a legend, and the date as the title.
5. Saves the plot as a PNG file in the `plots` folder with a timestamped filename.

**How It Works**
- **Shebang Line**: `#!/usr/bin/env python` ensures the system uses Python to run the script.
- **Main Function**: The main logic is wrapped in a `plot_data()` function.
- **Execution**: The script only runs the function if executed directly using `if __name__ == "__main__": plot_data()`
- **Plotting**: Uses matplotlib to create the line plot for all FAANG stock Close prices.
- **Saving**: Generates a PNG filename based on the current date and time, saves in `plots/`, and closes the plot to avoid memory issues.

**How to Run**
1. Clone the repository: `git clone <repository_url>` and `cd <repository_name>`
2. Ensure Python is installed
3. Install required libraries: `pip install -r requirements.txt`
4. Run the script: `python faang.py` or `./faang.py` (on Unix/Linux)

**Requirements**: pandas, matplotlib, yfinance, datetime, os

#### Problem 4: Automation with GitHub Actions
To automate the plotting process, GitHub Actions is used. The workflow runs the `faang.py` script automatically and saves the generated plot to the repository.

**Workflow File Location**: `.github/workflows/github-actions-demo.yml`

**Workflow Triggers**:
- Manual trigger using `workflow_dispatch`
- Scheduled trigger using `cron`, which runs every Saturday at 08:03 UTC

**Workflow Steps**:
1. **Checkout repository**: Clones the repository for access to `faang.py` and other files
2. **Setup Python**: Installs Python 3.x on the GitHub runner
3. **Install dependencies**: Installs packages from `requirements.txt`
4. **Run FAANG script**: Executes `faang.py` to generate the plot
5. **Commit and push new plots**: Stages, commits, and pushes new plot files automatically
6. **List plots**: Optionally lists `plots/` contents for verification

**Permissions**: Uses `contents: write` for auto-commits

**Automation Result**: When the workflow runs, it reads the latest CSV, creates a new plot, and commits it to the main branch, eliminating manual execution.

## Project Structure
- `faang.py`: Main plotting script
- `problems.ipynb`: Development notebook with problems and solutions
- `requirements.txt`: Python dependencies
- `data/`: Folder for input CSV files (timestamped)
- `plots/`: Folder for output PNG plots (timestamped)
- `.github/workflows/github-actions-demo.yml`: GitHub Actions workflow for automation
