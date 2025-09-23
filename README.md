# NBA Basketball Players Analysis (2000-2009)

This project contains a comprehensive analysis of NBA basketball players' performance data from the 2000 to 2009 seasons. The analysis includes three main parts: double-digit stats analysis, most valuable players calculation, and team performance analysis.

## Project Structure

```
/Users/taher/Projects/NBA/
├── Data/
│   └── NBA2000-2009.csv          # Raw NBA performance data
├── Notebook/
│   └── NBA.ipynb                 # Original notebook with analysis
├── Result/
│   ├── nba_analysis.ipynb        # Updated notebook with proper structure
    ├── nba_analysis.py               # Python implementation
│   ├── double_double.csv         # Results from Part One
│   ├── best_player.csv           # Results from Part Two
│   └── max_PTS_of_year.csv       # Results from Part Three
├── Result.zip                    # Compressed results file
└── README.md                     # This file
```

## Analysis Overview

### Part One: Double-Digit Stats Analysis

**Objective**: Identify players who achieved double-digit stats (≥10) in at least 2 of 5 main statistical categories:

- Points (PTS)
- Rebounds (REB) - sum of offensive and defensive rebounds
- Assists (AST)
- Steals (STL)
- Blocks (BLK)

**Output**: `double_double.csv` containing players and seasons meeting the criteria, sorted by year then player name.

### Part Two: Most Valuable Players

**Objective**: Calculate player value using the formula:

```
VALUE = (PTS + OREB + DREB + AST + STL + BLK) - (TOV + Missed FG + Missed FT)
```

Where:

- Missed FG = Field Goals Attempted - Field Goals Made
- Missed FT = Free Throws Attempted - Free Throws Made

**Output**: `best_player.csv` with players ranked by their average value over 10 seasons.

### Part Three: Team Performance Analysis

**Objective**: Find the team with the highest average points per year.

**Output**: `max_PTS_of_year.csv` showing the top-performing team for each year.

## How to Run

### Option 1: Using Python Script

```bash
cd /Users/taher/Projects/NBA
python3 nba_analysis.py
```

### Option 2: Using Jupyter Notebook

```bash
cd /Users/taher/Projects/NBA/Result
jupyter notebook nba_analysis.ipynb
```

**Note**: The updated notebook in the `Result/` directory has better structure and proper file paths.

### Option 3: Quick Results

The pre-computed results are available in the CSV files:

- `double_double.csv` - Players with double-digit stats
- `best_player.csv` - Most valuable players ranking
- `max_PTS_of_year.csv` - Team performance by year

## Key Results

### Top Double-Digit Players (2000)

| PLAYER          | YEAR | PTS  | AST | REB  | STL | BLK |
| --------------- | ---- | ---- | --- | ---- | --- | --- |
| Antonio Davis   | 2000 | 13.7 | 1.4 | 10.1 | 0.3 | 1.9 |
| Antonio McDyess | 2000 | 20.8 | 2.1 | 12.0 | 0.6 | 1.5 |
| Chris Webber    | 2000 | 27.1 | 4.2 | 11.1 | 1.3 | 1.7 |

### Most Valuable Players (2000-2009)

| PLAYER           | VALUE |
| ---------------- | ----- |
| Kevin Garnett    | 29.74 |
| LeBron James     | 27.90 |
| Chris Paul       | 26.57 |
| Shaquille O'Neal | 26.55 |
| Dwyane Wade      | 26.12 |

### Top Teams by Year

| YEAR | TEAM | PTS   |
| ---- | ---- | ----- |
| 2000 | SAC  | 100.2 |
| 2001 | LAL  | 95.9  |
| 2002 | ORL  | 97.0  |
| 2003 | DEN  | 96.0  |
| 2004 | BOS  | 106.2 |

## Dataset Information

- **Source**: NBA2000-2009.csv
- **Rows**: 1,832 entries
- **Columns**: 18 statistical categories
- **Period**: 2000-2009 seasons (10 years)
- **Players**: Individual player performance per season

### Column Descriptions

- `PLAYER`: Player's name
- `TEAM`: Team abbreviation
- `YEAR`: Season year
- `GP`: Games played
- `MIN`: Average minutes played
- `PTS`: Average points
- `FGM/FGA`: Field goals made/attempted
- `3PM/3PA`: 3-point field goals made/attempted
- `FTM/FTA`: Free throws made/attempted
- `OREB/DREB`: Offensive/defensive rebounds
- `AST`: Average assists
- `STL`: Average steals
- `BLK`: Average blocks
- `TOV`: Average turnovers

## Technical Implementation

### Libraries Used

- **pandas**: Data manipulation and analysis
- **numpy**: Numerical computations
- **zipfile**: File compression

### Key Operations

1. Data loading and preprocessing
2. Statistical calculations and filtering
3. Group operations and aggregations
4. Data sorting and formatting
5. Results export to CSV files

## Output Files

### double_double.csv

- Players achieving ≥10 in at least 2 statistical categories
- Sorted by year, then player name
- Includes PTS, AST, REB, STL, BLK columns

### best_player.csv

- Player value calculated using the custom formula
- Average value across all seasons played
- Sorted by value (descending), then player name
- Values rounded to 2 decimal places

### max_PTS_of_year.csv

- Team with highest average points per year
- Points calculated as sum of all players' averages
- Sorted by year (ascending)
- Values rounded to 2 decimal places

## Submission Package

The `result.zip` file contains:

- `double_double.csv`
- `best_player.csv`
- `max_PTS_of_year.csv`
- `NBA.ipynb` (original notebook)

This compressed file is ready for submission and contains all required deliverables.

## Analysis Insights

1. **Player Excellence**: Kevin Garnett emerges as the most valuable player with exceptional all-around performance
2. **Team Dominance**: Sacramento Kings started the decade strong with the highest scoring average
3. **Statistical Achievement**: Multiple players consistently achieved double-digit stats across multiple categories
4. **Career Consistency**: Top players maintained high performance across multiple seasons

## Notes

- All calculations follow the specified formulas and requirements
- Data integrity maintained throughout the analysis
- Results validated against expected output formats
- Ready for further statistical analysis or visualization
