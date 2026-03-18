# Julio Rodriguez Home Run Analysis

This script demonstrates how to use pybaseball to analyze a specific player's home run statistics using Statcast data.

## Overview

The script fetches Julio Rodriguez's statcast data from 2022-2024 and provides comprehensive home run analysis including:

- **Home run totals by year**
- **Launch metrics statistics** (exit velocity, launch angle, distance)
- **Top 10 longest home runs**
- **Top 10 hardest hit home runs**

## Key Features

### Player Lookup with Fuzzy Matching
The script demonstrates how to handle player names with special characters (like Julio Rodríguez's accent) using fuzzy matching:

```python
result = playerid_lookup('rodriguez', 'julio', fuzzy=True)
```

### Statcast Data Retrieval
Fetches player-specific statcast data for a date range:

```python
julio_data = statcast_batter('2022-01-01', '2024-12-31', player_id)
```

### Data Analysis
Filters for home runs and computes statistics on launch metrics:

```python
home_runs = julio_data[julio_data['events'] == 'home_run'].copy()
exit_velo = home_runs['launch_speed'].dropna()
```

## Results Summary

**Julio Rodriguez (2022-2024)**
- **Total Home Runs:** 87
- **By Year:** 2022: 31 HR, 2023: 34 HR, 2024: 22 HR
- **Average Exit Velocity:** 105.7 mph
- **Average Launch Angle:** 28.0°
- **Average Distance:** 397 feet
- **Longest Home Run:** 454 feet (May 7, 2023)
- **Hardest Hit:** 117.2 mph (September 11, 2022)

## Usage

```bash
python EXAMPLES/julio_rodriguez_homeruns.py
```

## Requirements

- pybaseball
- pandas

## Notes

- Julio Rodriguez is a Seattle Mariners outfielder who debuted in 2022
- The script uses fuzzy matching to handle the accent in his last name
- Some early season games (Spring Training) may have missing launch metric data
- Data is sourced from MLB's Statcast system via Baseball Savant
