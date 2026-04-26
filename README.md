# MASH Dashboard

A desktop-based dashboard application for tracking virtual agent activity, built with Python and CustomTkinter.

## Features

- **Dark Theme UI**: Modern, sleek interface matching the reference design
- **Activity Tracking**: 
  - Total laptop usage hours
  - Applications used with time breakdown
  - Productivity metrics (productive hours vs total time)
  - Tasks completed today
- **Today Overview**: 
  - Day progress timeline
  - Focused work blocks (Deep work, Bug fixes, etc.)
  - Block completion status
- **Schedule Management**: View scheduled activities with time ranges
- **Navigation**: Easy access to Home, Calendar, Stats, and Settings

## Requirements

- Python 3.8 or higher
- Linux/Windows/macOS with GUI support

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
python main.py
```

## Usage

The dashboard displays:
- **Header**: Dynamic greeting based on time of day and current time
- **TODAY Section**: Progress bar showing day completion, work blocks with color coding, and focus statistics
- **ACTIVITY Section**: Laptop usage time, top applications with usage duration, productivity percentage, and completed tasks
- **SCHEDULE Section**: List of scheduled activities with time ranges
- **Navigation Bar**: Quick access to different sections (Home, Calendar, Stats, Settings)

## Customization

The application uses placeholder data. To integrate with actual activity tracking:

1. Modify the `create_metrics_section()` method to fetch real data
2. Update the `create_today_section()` method to reflect actual work blocks
3. Adjust the `create_schedule_section()` method to pull from your calendar/schedule system

## Architecture

The application is structured as a single-file Python application (`main.py`) with the `DashboardApp` class. This makes it easy for your virtual agent to:
- Read and modify the code
- Add new features
- Integrate with other systems
- Make changes to the UI

## Future Enhancements

- Real-time activity tracking integration
- Calendar API integration
- Task management system
- Statistics and analytics
- Settings customization
- Data persistence
- Agent control interface

## License

This project is open for customization by your virtual agent.
