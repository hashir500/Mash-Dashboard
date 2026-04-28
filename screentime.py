from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, 
                             QPushButton, QFrame, QStackedWidget, QGraphicsColorizeEffect, QSizePolicy, QGridLayout)
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon, QColor
import random
from screentime_tracker import tracker


class HeatmapCell(QPushButton):
    def __init__(self, date_str, total_minutes, focused_minutes, parent=None):
        super().__init__(parent)
        self.date_str = date_str
        self.total_minutes = total_minutes
        self.focused_minutes = focused_minutes
        self.hover_info_callback = None
    
    def enterEvent(self, event):
        if self.hover_info_callback:
            self.hover_info_callback(self.date_str, self.total_minutes, self.focused_minutes)
        super().enterEvent(event)
    
    def leaveEvent(self, event):
        if self.hover_info_callback:
            self.hover_info_callback("", 0, 0)
        super().leaveEvent(event)


class ScreenTimePage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet("background-color: transparent;")
        
        # Generate sample data if none exists
        if not tracker.data["heatmap_data"]:
            tracker.generate_sample_data()
        
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 16, 0, 16)
        layout.setSpacing(20)
        
        # Header
        header = self.create_header()
        layout.addWidget(header)
        
        # Top section: Heatmap and Stats side by side
        top_section = QHBoxLayout()
        top_section.setSpacing(20)
        
        # GitHub-style heatmap
        heatmap = self.create_heatmap()
        top_section.addWidget(heatmap)
        
        # Right column: Stats & Top Apps
        stats_panel = self.create_stats_column()
        top_section.addWidget(stats_panel)
        
        layout.addLayout(top_section)
        
        # Timeline section (full width below)
        timeline = self.create_github_style_timeline()
        layout.addWidget(timeline)
    
    def update_hover_info(self, date_str, total_minutes, focused_minutes):
        """Update the hover info label when hovering over a heatmap cell"""
        if date_str:
            text = f"{date_str} | Total: {tracker.format_minutes(total_minutes)} | Focused: {tracker.format_minutes(focused_minutes)}"
            self.hover_info_label.setText(text)
        else:
            self.hover_info_label.setText("")
    
    def create_github_style_timeline(self):
        """Create GitHub-style activity timeline"""
        container = QFrame()
        container.setStyleSheet("""
            QFrame {
                background-color: #161b22;
                border: 1px solid #30363d;
                border-radius: 12px;
            }
        """)
        
        layout = QVBoxLayout(container)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(16)
        
        # Header
        header = QLabel("TODAY ACTIVITY")
        header.setStyleSheet("""
            QLabel {
                color: #888888;
                font-size: 13px;
                font-weight: 500;
                border: none;
                background: transparent;
            }
        """)
        layout.addWidget(header)
        
        # GitHub-style activity list
        # Get real activities from tracker
        activities_data = tracker.get_today_activities(limit=6)
        
        if activities_data:
            activities = [(a["title"], a["subtitle"], a["icon"], a["timestamp"]) for a in activities_data]
        else:
            # Fallback to default activities if no data
            activities = [
                ("Opened Tabbie", "Browsing", "assets/laptop.svg", "08:32 AM"),
                ("GitHub", "Coding", "assets/globe.svg", "09:15 AM"),
                ("Coffee Break", "Break", "assets/coffee.svg", "10:45 AM"),
                ("Deep Work Session", "Coding", "assets/laptop.svg", "11:00 AM"),
                ("Team Meeting", "Communication", "assets/globe.svg", "01:30 PM"),
                ("Completed Task", "Done", "assets/check.svg", "02:30 PM")
            ]
        
        for title, subtitle, icon, time in activities:
            item = self.create_github_style_item(title, subtitle, icon, time)
            layout.addWidget(item)
        
        layout.addStretch()
        
        return container
    
    def create_header(self):
        header = QWidget()
        header.setStyleSheet("background-color: transparent;")
        
        layout = QHBoxLayout(header)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(20)
        layout.setAlignment(Qt.AlignmentFlag.AlignVCenter)
        
        # Left side: Title and subtitle
        left_layout = QVBoxLayout()
        left_layout.setSpacing(4)
        
        title = QLabel("Screen Time")
        title.setStyleSheet("""
            QLabel {
                color: #ffffff;
                font-size: 28px;
                font-weight: bold;
                border: none;
                background: transparent;
            }
        """)
        
        subtitle = QLabel("Today")
        subtitle.setStyleSheet("""
            QLabel {
                color: #888888;
                font-size: 14px;
                border: none;
                background: transparent;
            }
        """)
        
        left_layout.addWidget(title)
        left_layout.addWidget(subtitle)
        
        layout.addLayout(left_layout)
        layout.addStretch()
        
        # Sync button
        sync_btn = QPushButton("Sync")
        sync_btn.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        sync_btn.setStyleSheet("""
            QPushButton {
                background-color: #238636;
                color: #ffffff;
                border: none;
                border-radius: 6px;
                padding: 6px 12px;
                font-size: 12px;
                font-weight: 500;
            }
            QPushButton:hover {
                background-color: #2ea043;
            }
        """)
        sync_btn.clicked.connect(self.sync_activitywatch)
        layout.addWidget(sync_btn)
        
        # Right side: Day/Week toggle
        toggle = self.create_toggle()
        layout.addWidget(toggle)
        
        return header
    
    def sync_activitywatch(self):
        """Sync data from ActivityWatch"""
        success = tracker.sync_from_activitywatch(days=7)
        if success:
            # Refresh the UI
            from PyQt6.QtWidgets import QMessageBox
            QMessageBox.information(self, "Sync Complete", "Data synced from ActivityWatch successfully!")
        else:
            from PyQt6.QtWidgets import QMessageBox
            QMessageBox.warning(self, "Sync Failed", "Could not connect to ActivityWatch. Make sure it's running on localhost:5600")
    
    def create_toggle(self):
        toggle = QFrame()
        toggle.setStyleSheet("""
            QFrame {
                background-color: #161b22;
                border: 1px solid #30363d;
                border-radius: 8px;
            }
        """)
        
        layout = QHBoxLayout(toggle)
        layout.setContentsMargins(4, 4, 4, 4)
        layout.setSpacing(0)
        
        # Day button (active)
        day_btn = QPushButton("Day")
        day_btn.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        day_btn.setStyleSheet("""
            QPushButton {
                background-color: #238636;
                color: #ffffff;
                border: none;
                border-radius: 6px;
                padding: 6px 16px;
                font-size: 13px;
                font-weight: 500;
            }
        """)
        
        # Week button (inactive)
        week_btn = QPushButton("Week")
        week_btn.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        week_btn.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                color: #888888;
                border: none;
                border-radius: 6px;
                padding: 6px 16px;
                font-size: 13px;
                font-weight: 500;
            }
            QPushButton:hover {
                color: #ffffff;
            }
        """)
        
        layout.addWidget(day_btn)
        layout.addWidget(week_btn)
        
        return toggle
    
    def create_heatmap(self):
        container = QWidget()
        container.setStyleSheet("background-color: transparent;")
        container.setSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        
        layout = QVBoxLayout(container)
        layout.setSpacing(12)
        
        # Heatmap frame
        heatmap_frame = QFrame()
        heatmap_frame.setStyleSheet("""
            QFrame {
                background-color: #161b22;
                border: 1px solid #30363d;
                border-radius: 12px;
            }
        """)
        
        heatmap_layout = QVBoxLayout(heatmap_frame)
        heatmap_layout.setContentsMargins(20, 20, 20, 20)
        heatmap_layout.setSpacing(12)
        heatmap_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # Main heatmap container with day labels on left
        heatmap_container = QHBoxLayout()
        heatmap_container.setSpacing(8)
        heatmap_container.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # Day labels (vertical)
        day_labels = QVBoxLayout()
        day_labels.setSpacing(0)
        
        days = ["Mon", "", "Wed", "", "Fri", "", ""]
        for day in days:
            label = QLabel(day)
            label.setStyleSheet("""
                QLabel {
                    color: #666666;
                    font-size: 10px;
                    border: none;
                    background: transparent;
                }
            """)
            label.setFixedHeight(14)
            day_labels.addWidget(label)
        
        heatmap_container.addLayout(day_labels)
        
        # GitHub-style grid
        grid = QGridLayout()
        grid.setSpacing(2)
        grid.setContentsMargins(0, 0, 0, 0)
        
        # 7 rows x 52 columns (full year - 52 weeks x 7 days)
        colors = [
            "#0e4429",  # Level 1
            "#006d32",  # Level 2
            "#26a641",  # Level 3
            "#39d353"   # Level 4 (Max)
        ]
        
        # Get real heatmap data from tracker
        heatmap_data = tracker.get_heatmap_data(364)  # 364 days = 52 weeks
        
        for row in range(7):
            for col in range(52):
                # Calculate which day in the data
                # GitHub-style: columns are weeks (oldest to newest), rows are days of week
                # Row 0 = Sunday, Row 6 = Saturday (or similar)
                # Col 0 = oldest week, Col 51 = newest week
                day_index = col * 7 + row
                if day_index < len(heatmap_data):
                    level = heatmap_data[day_index]["level"]
                    date_str = heatmap_data[day_index]["date"]
                else:
                    level = 0
                    date_str = ""
                
                # Get daily stats
                if date_str:
                    total_minutes = tracker.data["daily_data"].get(date_str, {}).get("total_minutes", 0)
                    focused_minutes = tracker.data["daily_data"].get(date_str, {}).get("focused_minutes", 0)
                else:
                    total_minutes = 0
                    focused_minutes = 0
                
                cell = HeatmapCell(date_str, total_minutes, focused_minutes)
                cell.setFixedSize(11, 11)
                cell.hover_info_callback = self.update_hover_info
                
                # Map level to color
                if level == 0:
                    color = "rgba(255, 255, 255, 0.05)"  # Empty
                elif level == 1:
                    color = colors[0]
                elif level == 2:
                    color = colors[1]
                elif level == 3:
                    color = colors[2]
                else:
                    color = colors[3]
                
                cell.setStyleSheet(f"""
                    QPushButton {{
                        background-color: {color};
                        border-radius: 2px;
                        border: none;
                        padding: 0px;
                    }}
                """)
                
                grid.addWidget(cell, row, col)
        
        heatmap_container.addLayout(grid)
        heatmap_layout.addLayout(heatmap_container)
        
        # Hover info label
        self.hover_info_label = QLabel()
        self.hover_info_label.setStyleSheet("""
            QLabel {
                color: #888888;
                font-size: 12px;
                border: none;
                background: transparent;
            }
        """)
        self.hover_info_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        heatmap_layout.addWidget(self.hover_info_label)
        
        # Month labels (horizontal)
        months_layout = QHBoxLayout()
        months_layout.setSpacing(0)
        months_layout.addSpacing(30)  # Space for day labels
        months_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        
        months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        for month in months:
            label = QLabel(month)
            label.setStyleSheet("""
                QLabel {
                    color: #666666;
                    font-size: 10px;
                    border: none;
                    background: transparent;
                }
            """)
            label.setFixedWidth(42)
            months_layout.addWidget(label)
        
        months_layout.addStretch()
        heatmap_layout.addLayout(months_layout)
        
        # Legend (GitHub-style intensity legend)
        legend_layout = QHBoxLayout()
        legend_layout.setSpacing(4)
        
        less_label = QLabel("Less")
        less_label.setStyleSheet("""
            QLabel {
                color: #666666;
                font-size: 10px;
                border: none;
                background: transparent;
            }
        """)
        
        legend_layout.addWidget(less_label)
        
        # Add color squares from empty to max
        legend_colors = ["rgba(255, 255, 255, 0.05)", "#0e4429", "#006d32", "#26a641", "#39d353"]
        for color in legend_colors:
            square = QFrame()
            square.setFixedSize(10, 10)
            square.setStyleSheet(f"""
                QFrame {{
                    background-color: {color};
                    border-radius: 2px;
                }}
            """)
            legend_layout.addWidget(square)
        
        more_label = QLabel("More")
        more_label.setStyleSheet("""
            QLabel {
                color: #666666;
                font-size: 10px;
                border: none;
                background: transparent;
            }
        """)
        
        legend_layout.addWidget(more_label)
        legend_layout.addStretch()
        heatmap_layout.addLayout(legend_layout)
        
        # Add the heatmap frame to the container layout
        layout.addWidget(heatmap_frame)
        
        return container
    
    def create_github_style_timeline(self):
        """Create GitHub-style activity timeline"""
        container = QFrame()
        container.setStyleSheet("""
            QFrame {
                background-color: #161b22;
                border: 1px solid #30363d;
                border-radius: 12px;
            }
        """)
        
        layout = QVBoxLayout(container)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(16)
        
        # Header
        header = QLabel("TODAY ACTIVITY")
        header.setStyleSheet("""
            QLabel {
                color: #888888;
                font-size: 13px;
                font-weight: 500;
                border: none;
                background: transparent;
            }
        """)
        layout.addWidget(header)
        
        # GitHub-style activity list
        # Get real activities from tracker
        activities_data = tracker.get_today_activities(limit=6)
        
        if activities_data:
            activities = [(a["title"], a["subtitle"], a["icon"], a["timestamp"]) for a in activities_data]
        else:
            # Fallback to default activities if no data
            activities = [
                ("Opened Tabbie", "Browsing", "assets/laptop.svg", "08:32 AM"),
                ("GitHub", "Coding", "assets/globe.svg", "09:15 AM"),
                ("Coffee Break", "Break", "assets/coffee.svg", "10:45 AM"),
                ("Deep Work Session", "Coding", "assets/laptop.svg", "11:00 AM"),
                ("Team Meeting", "Communication", "assets/globe.svg", "01:30 PM"),
                ("Completed Task", "Done", "assets/check.svg", "02:30 PM")
            ]
        
        for title, subtitle, icon, time in activities:
            item = self.create_github_style_item(title, subtitle, icon, time)
            layout.addWidget(item)
        
        layout.addStretch()
        
        return container
    
    def create_github_style_item(self, title, subtitle, icon_path, time):
        item = QWidget()
        item.setStyleSheet("""
            QWidget {
                background-color: transparent;
                border-bottom: 1px solid rgba(255, 255, 255, 0.03);
            }
        """)
        item.setFixedHeight(50)
        
        layout = QHBoxLayout(item)
        layout.setContentsMargins(0, 8, 0, 8)
        layout.setSpacing(12)
        
        # Icon
        icon_label = QLabel()
        icon_label.setFixedSize(16, 16)
        icon_label.setStyleSheet("border: none; background: transparent;")
        icon_label.setPixmap(QIcon(icon_path).pixmap(14, 14))
        colorize_effect = QGraphicsColorizeEffect()
        colorize_effect.setColor(QColor("#666666"))
        icon_label.setGraphicsEffect(colorize_effect)
        
        # Text
        text_layout = QVBoxLayout()
        text_layout.setSpacing(2)
        
        title_label = QLabel(title)
        title_label.setStyleSheet("""
            QLabel {
                color: #ffffff;
                font-size: 13px;
                border: none;
                background: transparent;
            }
        """)
        
        subtitle_label = QLabel(subtitle)
        subtitle_label.setStyleSheet("""
            QLabel {
                color: #666666;
                font-size: 11px;
                border: none;
                background: transparent;
            }
        """)
        
        text_layout.addWidget(title_label)
        text_layout.addWidget(subtitle_label)
        
        # Time
        time_label = QLabel(time)
        time_label.setStyleSheet("""
            QLabel {
                color: #666666;
                font-size: 11px;
                border: none;
                background: transparent;
            }
        """)
        
        layout.addWidget(icon_label)
        layout.addLayout(text_layout)
        layout.addStretch()
        layout.addWidget(time_label)
        
        return item
    
    def create_timeline_item(self, time, title, subtitle, icon_path, color, duration, badge, is_active):
        item = QWidget()
        item.setStyleSheet("""
            QWidget {
                background-color: transparent;
                border-bottom: 1px solid #30363d;
            }
        """)
        item.setFixedHeight(85)
        
        layout = QHBoxLayout(item)
        layout.setContentsMargins(0, 12, 0, 12)
        layout.setSpacing(16)
        
        # Timeline line and dot
        timeline_container = QWidget()
        timeline_container.setFixedWidth(40)
        timeline_container.setStyleSheet("background-color: transparent;")
        
        timeline_layout = QVBoxLayout(timeline_container)
        timeline_layout.setContentsMargins(0, 0, 0, 0)
        timeline_layout.setSpacing(0)
        
        # Dot
        dot = QFrame()
        dot.setFixedSize(12, 12)
        dot.setStyleSheet(f"""
            QFrame {{
                background-color: {color};
                border-radius: 6px;
            }}
        """)
        
        # Line
        line = QFrame()
        line.setFixedHeight(73)
        line.setStyleSheet("""
            QFrame {
                background-color: rgba(255, 255, 255, 0.1);
            }
        """)
        
        timeline_layout.addWidget(dot)
        timeline_layout.addWidget(line)
        
        # Time
        time_label = QLabel(time)
        time_label.setStyleSheet("""
            QLabel {
                color: #888888;
                font-size: 12px;
                border: none;
                background: transparent;
            }
        """)
        time_label.setFixedWidth(70)
        
        # Glassmorphic card
        card = QFrame()
        if is_active:
            card.setStyleSheet("""
                QFrame {
                    background-color: rgba(35, 134, 54, 0.2);
                    border: 1px solid #238636;
                    border-radius: 10px;
                }
            """)
        else:
            card.setStyleSheet("""
                QFrame {
                    background-color: #161b22;
                    border: 1px solid #30363d;
                    border-radius: 10px;
                }
            """)
        
        card_layout = QHBoxLayout(card)
        card_layout.setContentsMargins(12, 12, 12, 12)
        card_layout.setSpacing(12)
        
        # Icon wrapper
        icon_wrapper = QFrame()
        icon_wrapper.setFixedSize(40, 40)
        icon_wrapper.setStyleSheet(f"""
            QFrame {{
                background-color: {color}22;
                border-radius: 8px;
            }}
        """)
        
        icon_layout = QVBoxLayout(icon_wrapper)
        icon_layout.setContentsMargins(0, 0, 0, 0)
        icon_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        icon_label = QLabel()
        icon_label.setStyleSheet("border: none; background: transparent;")
        icon_label.setPixmap(QIcon(icon_path).pixmap(20, 20))
        colorize_effect = QGraphicsColorizeEffect()
        colorize_effect.setColor(Qt.GlobalColor.white)
        icon_label.setGraphicsEffect(colorize_effect)
        
        icon_layout.addWidget(icon_label)
        
        # Text info
        text_layout = QVBoxLayout()
        text_layout.setSpacing(4)
        
        title_label = QLabel(title)
        title_label.setStyleSheet(f"""
            QLabel {{
                color: #ffffff;
                font-size: 14px;
                font-weight: 500;
                border: none;
                background: transparent;
            }}
        """)
        
        subtitle_label = QLabel(subtitle)
        subtitle_label.setStyleSheet("""
            QLabel {
                color: #888888;
                font-size: 12px;
                border: none;
                background: transparent;
            }
        """)
        
        text_layout.addWidget(title_label)
        text_layout.addWidget(subtitle_label)
        
        # Duration
        duration_layout = QHBoxLayout()
        duration_layout.setSpacing(8)
        
        duration_label = QLabel(duration)
        duration_label.setStyleSheet("""
            QLabel {
                color: #888888;
                font-size: 13px;
                font-weight: 500;
                border: none;
                background: transparent;
            }
        """)
        
        duration_layout.addWidget(duration_label)
        
        if badge == "red":
            badge_label = QLabel("Completed")
            badge_label.setStyleSheet("""
                QLabel {
                    background-color: rgba(255, 59, 48, 0.2);
                    color: #FF3B30;
                    padding: 2px 8px;
                    border-radius: 6px;
                    font-size: 10px;
                    border: none;
                }
            """)
            duration_layout.addWidget(badge_label)
        
        card_layout.addWidget(icon_wrapper)
        card_layout.addLayout(text_layout)
        card_layout.addStretch()
        card_layout.addLayout(duration_layout)
        
        layout.addWidget(timeline_container)
        layout.addWidget(time_label)
        layout.addSpacing(15)
        layout.addWidget(card, 1)
        
        return item
    
    def create_stats_column(self):
        container = QWidget()
        container.setStyleSheet("background-color: transparent;")
        
        layout = QVBoxLayout(container)
        layout.setSpacing(16)
        
        # Stats panel
        stats_panel = self.create_stats_panel()
        layout.addWidget(stats_panel)
        
        # Top Apps panel
        apps_panel = self.create_top_apps_panel()
        layout.addWidget(apps_panel)
        
        layout.addStretch()
        
        return container
    
    def create_stats_panel(self):
        panel = QFrame()
        panel.setStyleSheet("""
            QFrame {
                background-color: #161b22;
                border: 1px solid #30363d;
                border-radius: 12px;
            }
        """)
        
        layout = QVBoxLayout(panel)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(16)
        
        # Header
        header = QLabel("Focused time")
        header.setStyleSheet("""
            QLabel {
                color: #888888;
                font-size: 13px;
                font-weight: 500;
                border: none;
                background: transparent;
            }
        """)
        layout.addWidget(header)
        
        # Get real stats from tracker
        stats = tracker.get_today_stats()
        focused_minutes = stats.get("focused_minutes", 0)
        total_minutes = stats.get("total_minutes", 0)
        
        # Time label
        time_label = QLabel(tracker.format_minutes(focused_minutes))
        time_label.setStyleSheet("""
            QLabel {
                color: #ffffff;
                font-size: 28px;
                font-weight: 600;
                border: none;
                background: transparent;
            }
        """)
        layout.addWidget(time_label)
        
        # Total time label
        total_label = QLabel(f"Total: {tracker.format_minutes(total_minutes)}")
        total_label.setStyleSheet("""
            QLabel {
                color: #666666;
                font-size: 12px;
                border: none;
                background: transparent;
            }
        """)
        layout.addWidget(total_label)
        
        # Blocks done label (simple text)
        blocks_label = QLabel("3/3 blocks done")
        blocks_label.setStyleSheet("""
            QLabel {
                color: #666666;
                font-size: 11px;
                border: none;
                background: transparent;
            }
        """)
        layout.addWidget(blocks_label)
        
        return panel
    
    def create_top_apps_panel(self):
        panel = QFrame()
        panel.setStyleSheet("""
            QFrame {
                background-color: #161b22;
                border: 1px solid #30363d;
                border-radius: 12px;
            }
        """)
        
        layout = QVBoxLayout(panel)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(16)
        
        # Header
        header = QLabel("Top apps")
        header.setStyleSheet("""
            QLabel {
                color: #888888;
                font-size: 13px;
                font-weight: 500;
                border: none;
                background: transparent;
            }
        """)
        
        # Apps grid
        apps_grid = QGridLayout()
        apps_grid.setSpacing(12)
        
        # Get real top apps from tracker
        top_apps = tracker.get_top_apps(limit=4)
        
        # Map app names to icons
        icon_map = {
            "VS Code": "assets/laptop.svg",
            "Browser": "assets/globe.svg",
            "Terminal": "assets/terminal.svg",
            "Slack": "assets/coffee.svg"
        }
        
        # Default icons if app not in map
        default_apps = [
            ("assets/terminal.svg", "Terminal"),
            ("assets/laptop.svg", "VS Code"),
            ("assets/globe.svg", "Browser"),
            ("assets/coffee.svg", "Slack")
        ]
        
        if top_apps:
            apps = [(icon_map.get(app, "assets/laptop.svg"), app) for app, _ in top_apps]
        else:
            apps = default_apps
        
        for i, (icon, name) in enumerate(apps):
            app_btn = QPushButton()
            app_btn.setFixedSize(50, 50)
            app_btn.setFocusPolicy(Qt.FocusPolicy.NoFocus)
            app_btn.setStyleSheet("""
                QPushButton {
                    background-color: transparent;
                    border: none;
                    border-radius: 8px;
                }
                QPushButton:hover {
                    background-color: rgba(35, 134, 54, 0.1);
                }
            """)
            
            app_layout = QVBoxLayout(app_btn)
            app_layout.setContentsMargins(0, 0, 0, 0)
            app_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
            
            icon_label = QLabel()
            icon_label.setStyleSheet("border: none; background: transparent;")
            icon_label.setPixmap(QIcon(icon).pixmap(24, 24))
            colorize_effect = QGraphicsColorizeEffect()
            colorize_effect.setColor(Qt.GlobalColor.white)
            icon_label.setGraphicsEffect(colorize_effect)
            
            app_layout.addWidget(icon_label)
            
            row = i // 2
            col = i % 2
            apps_grid.addWidget(app_btn, row, col)
        
        layout.addWidget(header)
        layout.addLayout(apps_grid)
        
        return panel
