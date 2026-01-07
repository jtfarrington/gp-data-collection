# Soccer/Football Event Data Collection GUI
## A comprehensive desktop application for recording, reviewing, and exporting event data from soccer matches with synchronized video playback.

## Table of Contents
1. Features
2. Screenshots
3. Technologies
4. Installation
5. Usage
6. Database Schema
7. Export Capabilities
8. Roadmap
9. Contributing
10. License

## Features 
### Event Recording
- **Real time event tracking:** Record passes, shots, goals, fouls, cards and more.
- **Player lineup management:** Input and track starting eleven and substitutions.
- **Match clock and playing direction tracking:** Automatic playing direction switches on match clock events (halftime, overtime).
- **Comprehensive event types:** 15+ event categories with detailed attributes and relationships.

### Event review and detailing:
- **Scrollable event list with event filtering**
- **Editable Event fields:** Location, quality-rating, player assignment, event specific fields.
- **Interactive field map:** Clickable field popup to set event locations with team orientation.
- **Incomplete event navigation:** Prev/Next buttons to quickly view missing data.
- **Validation system:** Flags incomplete events for review.

### Video Sychronization (Coming Soon)
- **Automatic timestamp syncing:** Video jumps to event location on event click.
- **MPV Integration:** External video player with IPC control.
- **Multi Format Support:** MP4, AVI, MKV, MOVD.

## Screenshots
### Team lineup and match metadata input window

<img width="1343" height="931" alt="Screenshot 2026-01-02 145410" src="https://github.com/user-attachments/assets/f7ca17f8-ac07-4b4a-923f-ed51e00a31cf" />

### Event collection window

<img width="1342" height="928" alt="Screenshot 2026-01-02 145639" src="https://github.com/user-attachments/assets/08210825-240d-4c25-aced-b3476ae3143e" />

### Event review and detailing window

<img width="1340" height="928" alt="Screenshot 2026-01-02 145725" src="https://github.com/user-attachments/assets/9799c25f-6b66-4638-99e8-3e72af6c0023" />

### Event review and detailing window with location input popup

<img width="1336" height="929" alt="Screenshot 2026-01-02 150724" src="https://github.com/user-attachments/assets/1dfbdc9f-0285-4350-ae60-c922ca9aff4b" />

## Technologies 
### Frontend
- **PySide6:** Qt based GUI framework. 
- **PyVisual:** Custom UI component Library. 
### Backend
- **Python 3.8 > 3.13**: Core app logic.
- **MySQL 8.0+:** Relational database for event storage. 
- **mysql-connector-python:** Database connectivity. 
### Data Processing
- **CSV Module:** Data export functionality.
### Video (planned)
- **MPV:** Lightweight video player with IPC.
- **yt-dlp:** Video download utility. 

## Installation (Full setup and use video: COMING SOON)

### Prerequisites
1. Python 3.8 > 3.13 (https://www.python.org/downloads/release/python-3130/) Make sure you install this Python version somehwere you can find it. 
2. MySQL 8.0+ and MySQL Workbench (https://www.youtube.com/watch?v=u96rVINbAUI)
3. Git (for cloning)

### Step 1: Clone the repository 

**In bash:**

`git clone https://github.com/jtfarrington/gp-data-collection.git`

`cd gp-data-collection`

### Step 2: Create and activate a virtual environment with your Python version. 

**In bash**

`/c/Users/you/folder name with your Python install/py3-13-0/python.exe -m venv .venv`

`source .venv/Scripts/activate`

**Step 3: Install dependencies:**

**In bash**

`pip install -r requirements.txt`

**Step 4 Configure database:** 

**In bash**

Copy the config template 

`cp config_template.py config.py`

In a text editor update `config.py` to have your specific credentials.

Run `table_generation.sql` script in your MySQL workbench. 

**Step 5 Run application:** 

**In bash** 

`python app.py`

## Usage

**Quick Start Guide**

**Page 0 - Setup**

1. Create teams (Home & Away)
2. Add players with jersey numbers
3. Assign coaches
4. Enter venue, competition details and date

**Page 1 - Live Recording**

1. Select which team starts on left
2. Click "Start Match" then "Kickoff" to begin the match.
3. Click player → Click event type → Event recorded
4. Use match clock controls (Kickoff, Halftime, etc.)

**Page 2 - Review and Detailing**

1. View all recorded events
2. Filter by event type or incomplete status
3. Click event to edit details
4. Set locations using field map
5. Use "Save & Next" for efficient workflow
6. Export to CSV when complete

**Event Types**

Ball Actions:

- Pass (Short/Medium/Long, Low/High)
- Shot (Left/Right/Header, On/Off Target)
- Cross (Near Post, Back Post, Central)
- Other Ball Action, Ball Received, Ball Won, Clearance, Shot Block, Shot Save

Set Pieces:

- Corner (Left/Right), Throw-In (Front/Rear)
- Direct/Indirect Free Kick, Penalty, Goal Kick

Disciplinary:

- Foul (with guilty/innocent players)
- Card (Yellow, Second Yellow, Red)

Other:

- Goal, Own Goal, Offside, Handball
- Duel (Ground/Aerial with winner/loser)
- Substitution (In/Out players)

## Database Schema

The application uses a Class Table Inheritance pattern for event types

**Key tables:**

`team` - Team information

`player` - Player roster

`coach` - Coach assignments

`match_metadata` - Match details (venue, competition, score)

`match_sides` - Playing direction tracking

`event` - Base event table with timestamps and locations

See this diagram for a deeper understanding of schema structure. 

[Database ER diagram (crow's foot).pdf](https://github.com/user-attachments/files/24412573/Database.ER.diagram.crow.s.foot.pdf)

## Export capabilities

**Events Export as CSV:**

- All events with complete details
- Event type, timestamp, location (X, Y)
- Player, team, jersey number
- Event-specific attributes (pass type, shot result, etc.)

**Match Summary: (COMING SOON)**

- Team-level statistics
- Shots, passes, fouls, cards by team
- Match metadata (venue, competition, teams)

**Player Statistics: (COMING SOON)**

- Individual performance metrics
- Passes completed, shots taken, goals scored
- Assists, fouls committed, cards received
- Duels won/lost

**Analysis Capabilities (COMING SOON)**

- Pass Completion % - Calculated from event sequences
- Shot Accuracy - On-target percentage
- Pass Networks - Inferred from Ball Received events
- Possession % - Time-based calculation from Ball Received timestamps
- Event-based statistics - Aggregations by team/player

## Roadmap

#### Completed

- Team & player management
- Live match recording with 15+ event types
- Real-time match clock
- Playing direction auto-flip
- Event review & editing interface
- Interactive location selection
- CSV data export
- Incomplete event tracking
- Pass network inference

#### In Progress

- Video synchronization with MPV
- Automatic timestamp syncing
- Video player controls in GUI

#### Planned

- Advanced analytics dashboard
- Shot maps and heat maps
- Pass network visualizations
- Excel export with formatting
- PDF match reports
- Multi-match comparisons
- Season-long statistics
- Player development tracking


## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

**Development Setup**

Fork the repository

Create your feature branch (git checkout -b feature/AmazingFeature)

Commit your changes (git commit -m 'Add some AmazingFeature')

Push to the branch (git push origin feature/AmazingFeature)

Open a Pull Request


## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author 

Jacob Farrington

GitHub: @jtfarrington

Email: jtsfarrington@gmail.com


## Acknowledgments

PyVisual - UI component library (https://www.youtube.com/watch?v=JjV9h042YaY)

PySide6 - Qt bindings for Python

MySQL - Database management

Inspired by professional match analysis tools (Opta, Wyscout, InStat)




