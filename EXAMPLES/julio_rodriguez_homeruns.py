#!/usr/bin/env python3
"""
Script to analyze Julio Rodriguez's home runs over the past few years.
Uses pybaseball to fetch statcast data and analyze home run statistics.

This example demonstrates:
- Using playerid_lookup to find a player (with fuzzy matching for accented names)
- Using statcast_batter to fetch player-specific statcast data
- Filtering and analyzing home run data
- Computing statistics on launch metrics
"""

from pybaseball.playerid_lookup import playerid_lookup
from pybaseball.statcast_batter import statcast_batter
import pandas as pd
from datetime import datetime


def get_julio_rodriguez_homeruns(start_year=2022, end_year=2024):
    """
    Fetch and analyze Julio Rodriguez's home runs.
    
    Args:
        start_year (int): Starting year for data collection
        end_year (int): Ending year for data collection
    
    Returns:
        dict: Dictionary containing home run statistics and data
    """
    
    print("=" * 70)
    print("JULIO RODRIGUEZ HOME RUN ANALYSIS")
    print("=" * 70)
    print()
    
    # Look up Julio Rodriguez with fuzzy matching (handles the accent in his name)
    print("Looking up Julio Rodriguez...")
    result = playerid_lookup('rodriguez', 'julio', fuzzy=True)
    
    if len(result) == 0:
        print("ERROR: Could not find Julio Rodriguez")
        return None
    
    # Get his player ID (first result should be the right one)
    player_id = result.iloc[0]['key_mlbam']
    print(f"✓ Found: {result.iloc[0]['name_first'].title()} {result.iloc[0]['name_last'].title()}")
    print(f"  MLBAM ID: {player_id}")
    print(f"  MLB Career: {int(result.iloc[0]['mlb_played_first'])}-{int(result.iloc[0]['mlb_played_last'])}")
    print()
    
    # Get statcast data for the specified years
    start_date = f"{start_year}-01-01"
    end_date = f"{end_year}-12-31"
    
    print(f"Fetching statcast data for {start_year}-{end_year}...")
    julio_data = statcast_batter(start_date, end_date, player_id)
    
    if julio_data is None or len(julio_data) == 0:
        print("ERROR: No data found")
        return None
    
    print(f"✓ Retrieved {len(julio_data)} pitches")
    print()
    
    # Filter for home runs
    home_runs = julio_data[julio_data['events'] == 'home_run'].copy()
    
    print("=" * 70)
    print("HOME RUN SUMMARY")
    print("=" * 70)
    print(f"Total Home Runs: {len(home_runs)}")
    print()
    
    # Group by year
    home_runs['year'] = pd.to_datetime(home_runs['game_date']).dt.year
    hr_by_year = home_runs.groupby('year').size()
    
    print("Home Runs by Year:")
    for year, count in hr_by_year.items():
        print(f"  {year}: {count} home runs")
    print()
    
    # Calculate average stats
    print("=" * 70)
    print("HOME RUN STATISTICS")
    print("=" * 70)
    
    # Exit velocity stats
    exit_velo = home_runs['launch_speed'].dropna()
    if len(exit_velo) > 0:
        print(f"Exit Velocity:")
        print(f"  Average: {exit_velo.mean():.1f} mph")
        print(f"  Max: {exit_velo.max():.1f} mph")
        print(f"  Min: {exit_velo.min():.1f} mph")
        print()
    
    # Launch angle stats
    launch_angle = home_runs['launch_angle'].dropna()
    if len(launch_angle) > 0:
        print(f"Launch Angle:")
        print(f"  Average: {launch_angle.mean():.1f}°")
        print(f"  Max: {launch_angle.max():.1f}°")
        print(f"  Min: {launch_angle.min():.1f}°")
        print()
    
    # Distance stats
    distance = home_runs['hit_distance_sc'].dropna()
    if len(distance) > 0:
        print(f"Distance:")
        print(f"  Average: {distance.mean():.0f} feet")
        print(f"  Max: {distance.max():.0f} feet")
        print(f"  Min: {distance.min():.0f} feet")
        print()
    
    # Top 10 longest home runs
    print("=" * 70)
    print("TOP 10 LONGEST HOME RUNS")
    print("=" * 70)
    
    top_10 = home_runs.nlargest(10, 'hit_distance_sc')[
        ['game_date', 'hit_distance_sc', 'launch_speed', 'launch_angle']
    ].copy()
    top_10['game_date'] = pd.to_datetime(top_10['game_date']).dt.strftime('%Y-%m-%d')
    
    for idx, (i, row) in enumerate(top_10.iterrows(), 1):
        print(f"{idx:2d}. {row['game_date']} - {row['hit_distance_sc']:.0f} ft "
              f"({row['launch_speed']:.1f} mph, {row['launch_angle']:.1f}°)")
    print()
    
    # Hardest hit home runs
    print("=" * 70)
    print("TOP 10 HARDEST HIT HOME RUNS")
    print("=" * 70)
    
    top_10_velo = home_runs.nlargest(10, 'launch_speed')[
        ['game_date', 'launch_speed', 'hit_distance_sc', 'launch_angle']
    ].copy()
    top_10_velo['game_date'] = pd.to_datetime(top_10_velo['game_date']).dt.strftime('%Y-%m-%d')
    
    for idx, (i, row) in enumerate(top_10_velo.iterrows(), 1):
        print(f"{idx:2d}. {row['game_date']} - {row['launch_speed']:.1f} mph "
              f"({row['hit_distance_sc']:.0f} ft, {row['launch_angle']:.1f}°)")
    print()
    
    return {
        'player_id': player_id,
        'total_homeruns': len(home_runs),
        'homeruns_by_year': hr_by_year.to_dict(),
        'home_runs_data': home_runs,
        'statcast_data': julio_data
    }


if __name__ == "__main__":
    # Run the analysis
    results = get_julio_rodriguez_homeruns(start_year=2022, end_year=2024)
    
    if results:
        print("=" * 70)
        print("Analysis complete!")
        print("=" * 70)
