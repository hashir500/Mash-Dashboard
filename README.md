# MASH Dashboard

A desktop-based productivity dashboard application built with Python and PyQt6, featuring screen time tracking, habit management, task organization, and more.

## Features

- **Dark Theme UI**: Modern, sleek interface matching GitHub's dark theme
- **Screen Time Tracking**:
  - GitHub-style activity heatmap showing daily usage patterns
  - Total screen time and focused work time tracking
  - Top applications usage breakdown
  - Activity timeline showing recent sessions
  - ActivityWatch integration for real-time data sync
- **Habit Tracking**:
  - Daily habit trackers (water, vitamins, exercise, reading, meditation)
  - Visual progress indicators
  - Reminder system
- **Task Management**:
  - Create, edit, and delete tasks
  - Task categorization
  - Progress tracking
- **Schedule Management**:
  - View scheduled activities with time ranges
  - Daily/weekly calendar view
- **Workspaces**:
  - Organize projects and workspaces
  - File management integration
- **Notes/Think**:
  - Quick note-taking
  - Link and attachment support
- **Navigation**: Easy access to all sections via sidebar

## Requirements

- Python 3.8 or higher
- PyQt6
- requests
- Linux/Windows/macOS with GUI support
- ActivityWatch (optional, for real-time screen time tracking)

## Installation

1. Clone or download this repository:
```bash
cd /home/hashir/Documents/mash-dashboard
```

2. Create a virtual environment:
```bash
python3 -m venv venv
```

3. Activate the virtual environment:

**On Linux/macOS:**
```bash
source venv/bin/activate
```

**On Windows:**
```bash
venv\Scripts\activate
```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

1. Make sure the virtual environment is activated
2. Run the application:
```bash
python3 main_pyqt.py
```

Or use the provided launcher script:
```bash
./launch.sh
```

## Screen Time Tracking

The Screen Time tab provides comprehensive activity tracking:

### ActivityWatch Integration

The dashboard integrates with [ActivityWatch](https://activitywatch.net/) for real-time screen time tracking:

1. Install and run ActivityWatch (it runs on `localhost:5600`)
2. Click the "Sync" button in the Screen Time tab
3. The app will fetch:
   - Daily screen time for the last 7 days
   - App usage breakdown
   - Activity timeline
   - Heatmap data for the last 365 days

### Data Storage

Screen time data is stored in `screentime_data.json` and includes:
- Daily total and focused time
- App usage per day
- Activity timeline
- Heatmap activity levels

### Features

- **Heatmap**: GitHub-style contribution graph showing activity levels (0-4) for each day
- **Stats Panel**: Displays today's total screen time and focused work time
- **Top Apps**: Shows the most used applications with time breakdown
- **Activity Timeline**: Recent activity events with timestamps

## Usage

The dashboard displays multiple tabs:

- **Screen Time**: Activity heatmap, stats, top apps, and timeline
- **Habits**: Daily habit trackers with progress indicators
- **Schedule**: Calendar view of scheduled activities
- **Workspaces**: Project and workspace organization
- **Tasks**: Task management and tracking
- **Think**: Quick note-taking and brainstorming

## Architecture

The application is structured with modular components:
- `main_pyqt.py`: Main application window and navigation
- `screentime.py`: Screen time tracking UI
- `screentime_tracker.py`: Backend data model and storage
- `activitywatch.py`: ActivityWatch API client
- `habits.py`: Habit tracking UI
- `schedule.py`: Schedule management UI
- `workspaces.py`: Workspace management UI
- `tasks.py`: Task management UI
- `think.py`: Notes and brainstorming UI

## Customization

### Screen Time Data

To customize screen time tracking:
1. Modify `screentime_tracker.py` to adjust data models
2. Update `activitywatch.py` for different ActivityWatch configurations
3. Change the sync interval in `screentime.py`

### UI Customization

Each UI module can be customized independently:
- Styles are defined in each module's stylesheet
- Icons are stored in the `assets/` folder
- Layouts can be modified in the respective `create_*` methods

## License

This project is open for customization.
