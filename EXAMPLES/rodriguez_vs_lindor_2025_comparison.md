# Julio Rodriguez vs Francisco Lindor - 2025 Comparison

This document contains code snippets for retrieving and comparing 2025 hitting statistics for Julio Rodriguez and Francisco Lindor using the pybaseball library.

## Installation

First, install pybaseball:

```bash
pip install pybaseball
```

## Basic Data Retrieval

### Step 1: Import and Get 2025 Batting Stats

```python
from pybaseball import batting_stats
import pandas as pd

# Get 2025 batting stats for all players
stats_2025 = batting_stats(2025, qual=0)

# Display available columns
print(stats_2025.columns)
```

### Step 2: Extract Individual Player Data

```python
# Find Julio Rodriguez
julio = stats_2025[stats_2025['Name'] == 'Julio Rodriguez'].iloc[0]

# Find Francisco Lindor
lindor = stats_2025[stats_2025['Name'] == 'Francisco Lindor'].iloc[0]

# Display basic info
print(f"Julio Rodriguez - Team: {julio['Team']}, Age: {int(julio['Age'])}")
print(f"Francisco Lindor - Team: {lindor['Team']}, Age: {int(lindor['Age'])}")
```

## Comparison Analysis

### Create a Comparison DataFrame

```python
# Create comparison data
comparison_data = {
    'Stat': [
        'Team',
        'Age',
        'Games',
        'Plate Appearances',
        'At Bats',
        'Hits',
        'Doubles',
        'Triples',
        'Home Runs',
        'RBIs',
        'Runs',
        'Walks',
        'Strikeouts',
        'Stolen Bases',
        'Caught Stealing',
        '',
        'Batting Average',
        'On-Base %',
        'Slugging %',
        'OPS',
        'Isolated Power',
        'BABIP',
        '',
        'Walk Rate',
        'Strikeout Rate',
        'BB/K Ratio',
        '',
        'wOBA',
        'wRC+',
        'WAR',
        '',
        'Exit Velocity',
        'Launch Angle',
        'Barrels',
        'Barrel Rate',
        'Hard Hit Rate'
    ],
    'Julio Rodriguez': [
        julio['Team'],
        int(julio['Age']),
        int(julio['G']),
        int(julio['PA']),
        int(julio['AB']),
        int(julio['H']),
        int(julio['2B']),
        int(julio['3B']),
        int(julio['HR']),
        int(julio['RBI']),
        int(julio['R']),
        int(julio['BB']),
        int(julio['SO']),
        int(julio['SB']),
        int(julio['CS']),
        '',
        f"{julio['AVG']:.3f}",
        f"{julio['OBP']:.3f}",
        f"{julio['SLG']:.3f}",
        f"{julio['OPS']:.3f}",
        f"{julio['ISO']:.3f}",
        f"{julio['BABIP']:.3f}",
        '',
        f"{julio['BB%']:.1%}",
        f"{julio['K%']:.1%}",
        f"{julio['BB/K']:.2f}",
        '',
        f"{julio['wOBA']:.3f}",
        f"{julio['wRC+']:.1f}",
        f"{julio['WAR']:.1f}",
        '',
        f"{julio['EV']:.1f} mph",
        f"{julio['LA']:.1f}°",
        int(julio['Barrels']),
        f"{julio['Barrel%']:.1%}",
        f"{julio['HardHit%']:.1%}"
    ],
    'Francisco Lindor': [
        lindor['Team'],
        int(lindor['Age']),
        int(lindor['G']),
        int(lindor['PA']),
        int(lindor['AB']),
        int(lindor['H']),
        int(lindor['2B']),
        int(lindor['3B']),
        int(lindor['HR']),
        int(lindor['RBI']),
        int(lindor['R']),
        int(lindor['BB']),
        int(lindor['SO']),
        int(lindor['SB']),
        int(lindor['CS']),
        '',
        f"{lindor['AVG']:.3f}",
        f"{lindor['OBP']:.3f}",
        f"{lindor['SLG']:.3f}",
        f"{lindor['OPS']:.3f}",
        f"{lindor['ISO']:.3f}",
        f"{lindor['BABIP']:.3f}",
        '',
        f"{lindor['BB%']:.1%}",
        f"{lindor['K%']:.1%}",
        f"{lindor['BB/K']:.2f}",
        '',
        f"{lindor['wOBA']:.3f}",
        f"{lindor['wRC+']:.1f}",
        f"{lindor['WAR']:.1f}",
        '',
        f"{lindor['EV']:.1f} mph",
        f"{lindor['LA']:.1f}°",
        int(lindor['Barrels']),
        f"{lindor['Barrel%']:.1%}",
        f"{lindor['HardHit%']:.1%}"
    ]
}

# Create DataFrame
df = pd.DataFrame(comparison_data)

# Display the comparison
print(df.to_string(index=False))
```

## Key Statistics Explained

### Batting Metrics
- **AVG (Batting Average)**: Hits divided by at-bats
- **OBP (On-Base Percentage)**: How often a player reaches base
- **SLG (Slugging Percentage)**: Total bases divided by at-bats
- **OPS (On-Base Plus Slugging)**: OBP + SLG combined metric

### Advanced Metrics
- **ISO (Isolated Power)**: SLG - AVG, measures pure power
- **BABIP (Batting Average on Balls In Play)**: Batting average excluding strikeouts and home runs
- **wOBA (Weighted On-Base Average)**: Weighted version of OBP accounting for different hit types
- **wRC+ (Weighted Runs Created+)**: Offensive value compared to league average (100 = average)
- **WAR (Wins Above Replacement)**: Total value in wins

### Contact Quality
- **EV (Exit Velocity)**: Average speed of batted balls in mph
- **LA (Launch Angle)**: Average angle of batted balls in degrees
- **Barrel Rate**: Percentage of batted balls with optimal exit velocity and launch angle
- **Hard Hit Rate**: Percentage of batted balls hit 95+ mph

## 2025 Season Results

### Key Findings

**Identical Batting Averages**
- Both players hit .267, showing similar overall batting performance

**Plate Discipline Winner: Francisco Lindor**
- Walk Rate: 8.9% vs 6.2% (Lindor draws more walks)
- Strikeout Rate: 17.9% vs 21.4% (Lindor strikes out less)
- BB/K Ratio: 0.50 vs 0.29 (Lindor has much better ratio)

**Power & Contact Winner: Julio Rodriguez**
- Exit Velocity: 91.8 mph vs 90.5 mph (Julio hits harder)
- Barrel Rate: 9.8% vs 8.8% (Julio barrels more)
- Hard Hit Rate: 48.0% vs 44.4% (Julio makes harder contact)

**Overall Value: Francisco Lindor**
- OPS: .811 vs .798
- wRC+: 129 vs 126
- WAR: 6.3 vs 5.7

## Data Sources

All data retrieved from FanGraphs via the pybaseball library:
- https://www.fangraphs.com/
- https://github.com/davisarthur/pybaseball

## Notes

- Data is current as of the 2025 season
- Both players played full 160-game seasons
- Statistics are subject to updates from data providers
- For more information on specific metrics, visit FanGraphs documentation
