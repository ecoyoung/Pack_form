**English** | [简体中文](README.md)

# Pack Form Labeling Program

## Features
Intelligently analyzes product descriptions in an Excel spreadsheet, automatically identifies the pack form, and fills it into the empty `Pack form` column.

## Pack Form Categories
- **Capsule** - Capsule forms (soft capsules, hard capsules, etc.)
- **Tablet** - Tablet forms (regular tablets, chewable tablets, lozenges, etc.)
- **Powder** - Powder forms (powders, drink mixes, granules, etc.)
- **Gummy** - Gummy forms (gummies, chews, jellies, etc.)
- **Drop** - Drop forms (drops, droplets, tinctures, etc.)
- **Softgel** - Softgel forms
- **Liquid** - Liquid forms (oral liquids, syrups, suspensions, etc.)
- **Mixed** - Multiple pack forms combined (multiple forms detected at once)
- **Others** - Other pack forms

## Usage

### Method 1: Command-Line Tool
```bash
# Install dependencies
pip install -r requirements.txt

# Run the program
python pack_form_labeler.py
```

### Method 2: Web Interface Tool (Recommended)
```bash
# Install dependencies
pip install -r requirements.txt

# Start the web app
streamlit run streamlit_app.py
```

**Windows users**: double-click the `run_app.bat` file
**Linux/Mac users**: run the `./run_app.sh` script

## Input Requirements
The Excel file must contain:
- `Pack form` - the pack form column (may contain empty values)
- `Product` - the product description column

## Output
The program generates a new file containing:
- **Pack form** - the pack form actually filled in
- **Matched_Pack_Form** - the matched pack form
- **Match_Source** - the specific text that was matched
- **Is_Originally_Empty** - flag indicating whether the cell was originally empty
- **Confidence_Score** - match confidence score

## How Matching Works
1. Uses regular expressions to match pack form keywords in both Chinese and English
2. Automatically handles case and singular/plural forms
3. Marks the entry as Mixed when multiple pack forms are detected
4. Computes a match confidence score

## Web Tool Highlights
- 🖥️ Clean and user-friendly web interface
- 📊 Real-time data preview and statistics
- 📈 Visualized pack form distribution charts
- 📥 One-click download of processed results
- 🔍 Detailed processing trace

## Notes
- Make sure the Excel file is properly formatted
- The more detailed the Product column descriptions, the higher the matching accuracy
- Back up the original file before processing
- The background image must be named `@logo.jpeg` and placed in the same directory

## Development & Maintenance
**IDC Team** - a professional data processing solution provider
