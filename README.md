# Premier League Football Data Analysis

## Project Overview
This project analyzes Premier League match data using Python and Pandas.
The goal is to explore team scoring performance, consistency, clean sheets,
goal difference, home vs away performance, and scoring trends.

## Dataset
The dataset contains match-level information such as:
- Date
- Home team
- Away team
- Home goals
- Away goals
- Match result
- Referee

## Analysis
The project includes:
- Total goals scored by each team
- Home vs away scoring performance
- Team scoring consistency
- Clean sheets and failed-to-score counts
- Monthly scoring trends
- Goal difference ranking
- High-scoring match distribution

## Visualizations
Charts are generated using Matplotlib and saved in the `charts/` folder.

## Project Structure

football-project/
├── main.py
├── clean_data.py
├── analyze.py
├── visualize.py
├── matches.csv
├── matches_cleaned.csv
├── README.md
└── charts/

## Key Findings
- Manchester City scored the most total goals with 77.
- Arsenal has the best defensive record with 18 clean sheets, Burnley and Wolves have the same number of clean sheets. 
- Arsenal had the best goal difference at +44.
- Home teams scored about 1.5 goals per match on average, compared with about 1.2 for away teams.
- High-scoring matches, defined as 3 or more total goals, accounted for 209 out of 380 matches.
- Wolves had one of the lowest scoring averages but were relatively consistent in their scoring output.

## How to Run

1. Install Python
2. Install required libraries:

```bash
pip install pandas matplotlib