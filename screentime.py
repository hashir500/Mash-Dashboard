from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, 
                             QPushButton, QFrame, QScrollArea, QGraphicsColorizeEffect, QGridLayout, QSizePolicy)
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon, QColor
import random


class ScreenTimePage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet("background-color: transparent;")
        
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
        timeline = self.create_timeline_column()
        layout.addWidget(timeline)
    
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
        
        # Right side: Day/Week toggle
        toggle = self.create_toggle()
        
        layout.addLayout(left_layout)
        layout.addStretch()
        layout.addWidget(toggle)
        
        return header
    
    def create_toggle(self):
        toggle = QFrame()
        toggle.setStyleSheet("""
            QFrame {
                background-color: rgba(255, 255, 255, 0.05);
                border: 1px solid rgba(255, 255, 255, 0.08);
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
                background-color: #007AFF;
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
                background-color: rgba(255, 255, 255, 0.05);
                border: 1px solid rgba(255, 255, 255, 0.08);
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
        
        for row in range(7):
            for col in range(52):
                cell = QFrame()
                cell.setFixedSize(11, 11)
                
                # Generate very dense activity - most cells should have some activity
                rand = random.random()
                if rand < 0.15:
                    color = "rgba(255, 255, 255, 0.05)"  # Empty (only 15%)
                elif rand < 0.4:
                    color = colors[0]
                elif rand < 0.65:
                    color = colors[1]
                elif rand < 0.85:
                    color = colors[2]
                else:
                    color = colors[3]
                
                cell.setStyleSheet(f"""
                    QFrame {{
                        background-color: {color};
                        border-radius: 2px;
                    }}
                """)
                grid.addWidget(cell, row, col)
        
        heatmap_container.addLayout(grid)
        heatmap_layout.addLayout(heatmap_container)
        
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
        
        layout.addWidget(heatmap_frame)
        
        return container
    
    def create_timeline_column(self):
        container = QWidget()
        container.setStyleSheet("background-color: transparent;")
        
        layout = QVBoxLayout(container)
        layout.setSpacing(12)
        
        # Section header
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
        activities = [
            ("Opened Tabbie", "Browsing", "laptop.svg", "08:32 AM"),
            ("GitHub", "Coding", "globe.svg", "09:15 AM"),
            ("Coffee Break", "Break", "coffee.svg", "10:45 AM"),
            ("Deep Work Session", "Coding", "laptop.svg", "11:00 AM"),
            ("Team Meeting", "Communication", "globe.svg", "01:30 PM"),
            ("Completed Task", "Done", "check.svg", "02:30 PM")
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
                border-bottom: 1px solid rgba(255, 255, 255, 0.05);
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
                    background-color: rgba(255, 255, 255, 0.08);
                    border: 1px solid rgba(100, 150, 255, 0.5);
                    border-radius: 10px;
                }
            """)
        else:
            card.setStyleSheet("""
                QFrame {
                    background-color: rgba(255, 255, 255, 0.05);
                    border: 1px solid rgba(255, 255, 255, 0.04);
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
                background-color: rgba(255, 255, 255, 0.05);
                border: 1px solid rgba(255, 255, 255, 0.04);
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
        
        # Time display
        time_label = QLabel("8h 32m")
        time_label.setStyleSheet("""
            QLabel {
                color: #ffffff;
                font-size: 36px;
                font-weight: bold;
                border: none;
                background: transparent;
            }
        """)
        
        # Blocks done - minimalist text only
        blocks_label = QLabel("3/3 blocks done")
        blocks_label.setStyleSheet("""
            QLabel {
                color: #666666;
                font-size: 12px;
                border: none;
                background: transparent;
            }
        """)
        
        layout.addWidget(header)
        layout.addWidget(time_label)
        layout.addWidget(blocks_label)
        
        return panel
    
    def create_top_apps_panel(self):
        panel = QFrame()
        panel.setStyleSheet("""
            QFrame {
                background-color: rgba(255, 255, 255, 0.05);
                border: 1px solid rgba(255, 255, 255, 0.04);
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
        
        apps = [
            ("terminal.svg", "Terminal"),
            ("laptop.svg", "VS Code"),
            ("globe.svg", "Browser"),
            ("coffee.svg", "Slack")
        ]
        
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
                    background-color: rgba(255, 255, 255, 0.05);
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
