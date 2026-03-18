# AGENTS.md - Pybaseball Repository Guide

## Repository Overview

**pybaseball** is a comprehensive Python package for baseball data analysis and web scraping. It provides seamless access to advanced baseball statistics from multiple authoritative sources including Baseball Reference, Baseball Savant (Statcast), and FanGraphs.

**Repository**: https://github.com/davisarthur/pybaseball  
**Maintainer**: Davis Arthur (davisarthur)  
**Original Author**: James LeDoux  
**Current Maintainer**: Moshe Schorr  
**License**: MIT  
**Python Support**: 3.8, 3.9, 3.10, 3.11

---

## Project Purpose & Scope

### Core Mission
Pybaseball eliminates the need for manual web scraping by providing a unified Python interface to retrieve:
- **Pitch-level Statcast data** from Baseball Savant
- **Season-level aggregated statistics** from FanGraphs and Baseball Reference
- **Historical and current standings** and team records
- **Player-specific performance metrics** (batting, pitching, fielding)
- **Advanced sabermetric calculations** (WAR, wOBA, expected stats, etc.)
- **Draft and prospect data**

### Key Features
1. **Multi-source data aggregation** - Consolidates data from 5+ authoritative baseball databases
2. **Flexible time-range queries** - Pull data for specific dates, seasons, or custom periods
3. **Player-specific filtering** - Query individual pitcher/batter performance
4. **Caching system** - Local data caching for faster repeated queries
5. **Advanced metrics** - Includes modern sabermetric calculations (Run Value, Barrel%, etc.)
6. **Visualization tools** - Built-in plotting functions for data analysis

---

## Repository Structure

### Root Level Files
```
pybaseball/
├── README.md                 # Main documentation and quick start guide
├── CHANGELOG.md              # Version history and breaking changes
├── contributing.md           # Contribution guidelines
├── setup.py                  # Package configuration and dependencies
├── pyproject.toml            # Modern Python project metadata
├── pytest.ini                # Testing configuration
├── mypy.ini                  # Type checking configuration
├── Makefile                  # Development automation commands
├── LICENSE                   # MIT License
└── MANIFEST.in               # Package data manifest
```

### Main Package Directory: `/pybaseball`

#### Core Data Retrieval Modules
- **`statcast.py`** - Main Statcast data retrieval (pitch-level data from Baseball Savant)
- **`statcast_pitcher.py`** - Pitcher-specific Statcast queries with advanced metrics
- **`statcast_batter.py`** - Batter-specific Statcast queries
- **`statcast_fielding.py`** - Fielding metrics from Statcast data
- **`statcast_pitcher_spin.py`** - Spin rate and pitch movement analysis
- **`statcast_running.py`** - Base running and sprint speed metrics

#### Season-Level Statistics
- **`league_batting_stats.py`** - League-wide batting statistics (FanGraphs)
- **`league_pitching_stats.py`** - League-wide pitching statistics (FanGraphs)
- **`team_batting.py`** - Team batting aggregates
- **`team_pitching.py`** - Team pitching aggregates
- **`team_fielding.py`** - Team fielding statistics
- **`team_game_logs.py`** - Game-by-game team results

#### Player & Team Information
- **`playerid_lookup.py`** - Convert player names to MLB IDs (MLBAM, Retrosheet, BBRef, FanGraphs)
- **`teamid_lookup.py`** - Team ID lookups and conversions
- **`standings.py`** - Division standings and historical records
- **`team_results.py`** - Team game results and schedules

#### Specialized Data Sources
- **`lahman.py`** - Access to Sean Lahman's historical baseball database
- **`retrosheet.py`** - Retrosheet data integration (historical play-by-play)
- **`amateur_draft.py`** - MLB amateur draft data
- **`amateur_draft_by_team.py`** - Draft picks by team
- **`top_prospects.py`** - Top prospect rankings
- **`split_stats.py`** - Player statistics split by various categories

#### Utilities & Helpers
- **`utils.py`** - Core utility functions (web scraping, data cleaning, caching)
- **`plotting.py`** - Visualization functions (heatmaps, scatter plots, etc.)
- **`__init__.py`** - Package initialization and public API exports
- **`version.py`** - Version string

#### Subdirectories
- **`/datasources`** - Data source adapters and scrapers
- **`/datahelpers`** - Data transformation and cleaning utilities
- **`/analysis`** - Analysis tools and calculations
- **`/enums`** - Enumeration definitions (pitch types, positions, etc.)
- **`/cache`** - Caching system implementation
- **`/data`** - Static data files (team mappings, etc.)

### Testing & Documentation
- **`/tests`** - Comprehensive test suite (pytest)
- **`/docs`** - Detailed function documentation and examples
- **`/EXAMPLES`** - Example notebooks and scripts
- **`/.github`** - GitHub Actions CI/CD workflows

---

## Key Dependencies

### Core Dependencies
```python
numpy>=1.13.0              # Numerical computing
pandas>=1.0.3              # Data manipulation and analysis
beautifulsoup4>=4.4.0      # HTML/XML parsing
requests>=2.18.1           # HTTP requests (legacy)
curl_cffi>=0.10.0          # Modern HTTP requests (replaces requests for some use cases)
lxml>=4.2.1                # XML/HTML processing
pyarrow>=1.0.1             # Parquet file support
pygithub>=1.51             # GitHub API integration
scipy>=1.4.0               # Scientific computing
matplotlib>=2.0.0          # Data visualization
tqdm>=4.50.0               # Progress bars
attrs>=20.3.0              # Class decorators
```

### Development Dependencies
```python
pytest>=6.0.2              # Testing framework
mypy>=0.782                # Static type checking
pytest-cov>=2.10.1         # Code coverage
pytest-xdist>=2.1.0        # Parallel test execution
types-requests>=2.18.1     # Type hints for requests
```

---

## Main API Functions

### Statcast Data (Pitch-Level)
```python
statcast(start_dt, end_dt, verbose=False)
statcast_pitcher(start_dt, end_dt, player_id, verbose=False)
statcast_batter(start_dt, end_dt, player_id, verbose=False)
statcast_fielding(start_dt, end_dt)
statcast_pitcher_spin(start_dt, end_dt, player_id)
statcast_running(start_dt, end_dt)
```

### Season-Level Statistics
```python
pitching_stats(start_season, end_season)
batting_stats(start_season, end_season)
pitching_stats_range(start_dt, end_dt)
batting_stats_range(start_dt, end_dt)
pitching_stats_bref(season)
batting_stats_bref(season)
```

### Team Statistics
```python
team_pitching(season, qual=1)
team_batting(season, qual=1)
team_fielding(season)
team_game_logs(season, team)
schedule_and_record(season, team)
standings(season)
```

### Player & Team Lookups
```python
playerid_lookup(last_name, first_name)
playerid_reverse_lookup(player_id, id_type)
teamid_lookup(team_name)
```

### Historical Data
```python
lahman_pitching(start_season, end_season)
lahman_batting(start_season, end_season)
retrosheet(season)
```

### Draft & Prospects
```python
amateur_draft(year)
amateur_draft_by_team(year, team)
top_prospects(year)
```

---

## Data Sources & Attribution

### Primary Data Sources
1. **Baseball Savant** (MLB Advanced Media)
   - Statcast pitch-level data
   - Advanced metrics (exit velocity, launch angle, spin rate)
   - Expected statistics (xBA, xSLG, xwOBA)

2. **FanGraphs**
   - Season-level batting and pitching statistics
   - Advanced sabermetric calculations (WAR, wOBA, FIP)
   - Leaderboards and rankings

3. **Baseball Reference**
   - Historical statistics
   - Team records and standings
   - Game logs and schedules

4. **Retrosheet**
   - Historical play-by-play data
   - Game results and box scores

5. **Sean Lahman's Baseball Database**
   - Historical statistics (1871-present)
   - Player biographical data
   - Team information

---

## Recent Development Activity

### Latest Commits (as of Jan 2026)
1. **BR URLs HTTPS Migration** - Updated Baseball Reference URLs from HTTP to HTTPS to avoid 503 errors
2. **Statcast Run Value** - Added run value calculations and fixed statcast filtering
3. **Reliever/Starter Filters** - Added team_pitching_starters and team_pitching_relievers functions
4. **Team Game Logs Fix** - Updated table IDs and improved data cleanup
5. **Pandas Compatibility** - Fixed FutureWarnings for pandas concatenation and datetime handling
6. **curl_cffi Integration** - Replaced requests library with curl_cffi for better reliability

### Known Issues & Maintenance Notes
- Statcast data is subject to change even for prior seasons (700,000+ pitches per season)
- Cache may contain stale data for future dates - use `cache.purge()` if needed
- Some functions require multiprocessing workarounds on Windows/OSX
- Baseball Reference URLs occasionally change, requiring maintenance updates

---

## Development Workflow

### Testing
```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=pybaseball

# Run tests in parallel
pytest -n auto
```

### Code Quality
```bash
# Type checking
mypy pybaseball

# Code formatting (if configured)
make format
```

### Building & Distribution
```bash
# Install in development mode
pip install -e .

# Build package
python setup.py sdist bdist_wheel

# Install from source
pip install .
```

---

## Contributing Guidelines

### How to Contribute
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Make changes and add tests
4. Run test suite and type checking
5. Submit pull request with clear description

### Areas for Contribution
- **Bug fixes** - Report and fix issues with data retrieval
- **New data sources** - Add support for additional baseball databases
- **Performance improvements** - Optimize data retrieval and caching
- **Documentation** - Improve docstrings and examples
- **Tests** - Increase test coverage
- **Features** - Add new analysis functions

See `contributing.md` for detailed guidelines.

---

## Caching System

### Enable Caching
```python
from pybaseball import cache
cache.enable()
```

### Disable Caching
```python
from pybaseball import cache
cache.disable()
```

### Clear Cache
```python
from pybaseball import cache
cache.purge()
```

### Benefits
- Faster repeated queries
- Reduced load on data sources
- Offline data access (after initial download)

---

## Common Use Cases

### 1. Analyze a Pitcher's Performance
```python
from pybaseball import playerid_lookup, statcast_pitcher
pitcher_id = playerid_lookup('kershaw', 'clayton')['key_mlbam'].values[0]
data = statcast_pitcher('2023-04-01', '2023-10-01', pitcher_id)
```

### 2. Compare League-Wide Batting Stats
```python
from pybaseball import batting_stats
stats = batting_stats(2022, 2023)
```

### 3. Get Team Standings
```python
from pybaseball import standings
divisions = standings(2023)
```

### 4. Analyze Statcast Data
```python
from pybaseball import statcast
data = statcast('2023-06-01', '2023-06-30')
hard_hit = data[data['launch_speed'] > 95]
```

---

## Performance Considerations

### Data Volume
- **Statcast**: ~700,000 pitches per season
- **Season stats**: ~1,000+ players per season
- **Historical data**: Available from 1871 onwards

### Query Optimization
- Use date ranges to limit data retrieval
- Enable caching for repeated queries
- Filter data after retrieval when possible
- Use player_id for specific player queries

### Network Considerations
- Respect rate limits on data sources
- Use caching to minimize requests
- Consider batch processing for large queries

---

## Troubleshooting

### Common Issues

**Issue**: `BrokenProcessPool` error
- **Solution**: Wrap code in `if __name__ == '__main__':` block

**Issue**: Stale cache data
- **Solution**: Run `cache.purge()` to clear cache

**Issue**: 503 errors from Baseball Reference
- **Solution**: Ensure using HTTPS URLs (fixed in recent versions)

**Issue**: Missing data for recent dates
- **Solution**: Statcast data may not be available immediately; wait 24-48 hours

---

## Version History

### Current Version
- Latest: Check `pybaseball/version.py`
- Python Support: 3.8+
- Status: Beta (Development Status 4)

### Release Process
- Periodic updates published to PyPI
- Latest development version available on GitHub
- Breaking changes documented in CHANGELOG.md

---

## Community & Support

### Getting Help
- **Discord**: Join the community Discord (link in README)
- **GitHub Issues**: Report bugs and request features
- **Documentation**: See `/docs` folder for comprehensive guides
- **Examples**: Check `/EXAMPLES` for usage patterns

### Contributing Back
- Submit pull requests for improvements
- Report bugs with reproducible examples
- Share analysis examples and use cases
- Help improve documentation

---

## Key Metrics & Statistics

### Repository Stats
- **Stars**: 1,600+
- **Forks**: 400+
- **Open Issues**: 139
- **Contributors**: 50+
- **Last Updated**: January 2026

### Data Coverage
- **Statcast**: 2015-present
- **FanGraphs**: 1871-present
- **Baseball Reference**: 1871-present
- **Retrosheet**: 1871-present

---

## Related Resources

### External Documentation
- [Baseball Savant CSV Documentation](https://baseballsavant.mlb.com/csv-docs)
- [FanGraphs Glossary](https://www.fangraphs.com/library/)
- [Baseball Reference](https://www.baseball-reference.com/)
- [Retrosheet](https://www.retrosheet.org/)

### Similar Projects
- [baseballr](https://github.com/billpetti/baseballr) - R package (inspiration for pybaseball)
- [pybaseball_live](https://github.com/Jensen-holm/pybaseball_live) - Live MLB API wrapper
- [pybaseballstats](https://github.com/nico671/pybaseballstats) - Alternative Python package

---

## License & Attribution

**License**: MIT License

**Original Author**: James LeDoux  
**Current Maintainer**: Moshe Schorr  
**Repository Owner**: Davis Arthur

**Data Attribution**:
- Statcast data © MLB Advanced Media
- FanGraphs data © FanGraphs
- Baseball Reference data © Sports Reference LLC
- Retrosheet data © Retrosheet
- Lahman Database © Sean Lahman

---

## Quick Start for Developers

### Clone & Setup
```bash
git clone https://github.com/davisarthur/pybaseball.git
cd pybaseball
pip install -e ".[test]"
```

### Run Tests
```bash
pytest -v
```

### Check Types
```bash
mypy pybaseball
```

### Make a Change
1. Create feature branch
2. Modify code
3. Add tests
4. Run test suite
5. Submit PR

---

**Last Updated**: February 2026  
**Maintained By**: Davis Arthur (@davisarthur)  
**For Issues**: https://github.com/davisarthur/pybaseball/issues
