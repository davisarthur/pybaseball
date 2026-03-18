#!/usr/bin/env python3
"""
Generic player home run analysis script.
Analyzes any player's home runs over a specified time period.

Usage:
    python player_homeruns_analysis.py <last_name> <first_name> [start_year] [end_year]
    
Example:
    python player_homeruns_analysis.py rodriguez julio 2022 2024
    python player_homeruns_analysis.py judge aaron 2022 2024
"""

import sys
import argparse
from pybaseball.playerid_lookup import playerid_lookup
from pybaseball.statcast_batter import statcast_batter
import pandas as pd


def analyze_player_homeruns(last_name, first_name, start_year=2022, end_year=2024):
    """
    Fetch and analyze a player's home runs.
    
    Args:
        last_name (str): Player's last name
        first_name (str): Player's first name
        start_year (int): Starting year for data collection
        end_year (int): Ending year for data collection
    
    Returns:
        dict: Dictionary containing home run statistics and data
    """
    
    print("=" * 70)
    print(f"{first_name.upper()} {last_name.upper()} HOME RUN ANALYSIS")
    print("=" * 70)
    print()
    
    # Look up player with fuzzy matching
    print(f"Looking up {first_name} {last_name}...")
    result = playerid_lookup(last_name, first_name, fuzzy=True)
    
    if len(result) == 0:
        print(f"ERROR: Could not find {first_name} {last_name}")
        return None
    
    # Get player ID (first result should be the right one)
    player_id = result.iloc[0]['key_mlbam']
    player_name = f"{result.iloc[0]['name_first'].title()} {result.iloc[0]['name_last'].title()}"
    
    print(f"✓ Found: {player_name}")
    print(f"  MLBAM ID: {player_id}")
    print(f"  MLB Career: {int(result.iloc[0]['mlb_played_first'])}-{int(result.iloc[0]['mlb_played_last'])}")
    print()
    
    # Get statcast data for the specified years
    start_date = f"{start_year}-01-01"
    end_date = f"{end_year}-12-31"
    
    print(f"Fetching statcast data for {start_year}-{end_year}...")
    player_data = statcast_batter(start_date, end_date, player_id)
    
    if player_data is None or len(player_data) == 0:
        print("ERROR: No data found")
        return None
    
    print(f"✓ Retrieved {len(player_data)} pitches")
    print()
    
    # Filter for home runs
    home_runs = player_data[player_data['events'] == 'home_run'].copy()
    
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
        'player_name': player_name,
        'total_homeruns': len(home_runs),
        'homeruns_by_year': hr_by_year.to_dict(),
        'home_runs_data': home_runs,
        'statcast_data': player_data
    }


def main():
    parser = argparse.ArgumentParser(
        description='Analyze a player\'s home runs using pybaseball statcast data'
    )
    parser.add_argument('last_name', help='Player\'s last name')
    parser.add_argument('first_name', help='Player\'s first name')
    parser.add_argument('--start-year', type=int, default=2022, help='Starting year (default: 2022)')
    parser.add_argument('--end-year', type=int, default=2024, help='Ending year (default: 2024)')
    
    args = parser.parse_args()
    
    results = analyze_player_homeruns(
        args.last_name,
        args.first_name,
        args.start_year,
        args.end_year
    )
    
    if results:
        print("=" * 70)
        print("Analysis complete!")
        print("=" * 70)


if __name__ == "__main__":
    main()
