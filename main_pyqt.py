import sys
from datetime import datetime
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QLabel, QPushButton, QFrame, QSizePolicy)
from PyQt6.QtCore import Qt, QPoint, QSize
from PyQt6.QtGui import QIcon, QPainter, QColor, QPen, QFont


class TitleBar(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedHeight(50)
        self.setStyleSheet("""
            QWidget {
                background-color: transparent;
            }
        """)
        
        layout = QHBoxLayout(self)
        layout.setContentsMargins(16, 8, 16, 8)
        layout.setSpacing(12)
        
        # Traffic lights
        traffic_lights = QHBoxLayout()
        traffic_lights.setSpacing(8)
        
        self.close_btn = self.create_traffic_light("#ff5f56", self.close_window)
        self.minimize_btn = self.create_traffic_light("#ffbd2e", self.show_minimized)
        self.maximize_btn = self.create_traffic_light("#27c93f", self.toggle_maximize)
        
        traffic_lights.addWidget(self.close_btn)
        traffic_lights.addWidget(self.minimize_btn)
        traffic_lights.addWidget(self.maximize_btn)
        
        layout.addLayout(traffic_lights)
        layout.addStretch()
        
        # Status indicator
        status_layout = QHBoxLayout()
        status_layout.setSpacing(8)
        
        status_dot = QLabel()
        status_dot.setFixedSize(8, 8)
        status_dot.setStyleSheet("""
            QLabel {
                background-color: #27c93f;
                border-radius: 4px;
            }
        """)
        
        status_label = QLabel("Mash")
        status_label.setStyleSheet("color: #ffffff; font-size: 13px; font-weight: 500;")
        
        settings_btn = QPushButton()
        settings_btn.setText("⚙")
        settings_btn.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                color: #888888;
                border: none;
                font-size: 14px;
                padding: 4px;
            }
            QPushButton:hover {
                color: #ffffff;
            }
        """)
        settings_btn.setFixedSize(24, 24)
        
        expand_btn = QPushButton()
        expand_btn.setText("⤢")
        expand_btn.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                color: #888888;
                border: none;
                font-size: 14px;
                padding: 4px;
            }
            QPushButton:hover {
                color: #ffffff;
            }
        """)
        expand_btn.setFixedSize(24, 24)
        
        cmd_badge = QLabel("⌘ K")
        cmd_badge.setStyleSheet("""
            QLabel {
                background-color: #3a3a3a;
                color: #888888;
                padding: 4px 8px;
                border-radius: 4px;
                font-size: 11px;
            }
        """)
        
        status_layout.addWidget(status_dot)
        status_layout.addWidget(status_label)
        status_layout.addWidget(settings_btn)
        status_layout.addWidget(expand_btn)
        status_layout.addWidget(cmd_badge)
        
        layout.addLayout(status_layout)
        
        self.parent_window = parent
        self.start_pos = QPoint()
        
    def create_traffic_light(self, color, callback):
        btn = QPushButton()
        btn.setFixedSize(12, 12)
        btn.setStyleSheet(f"""
            QPushButton {{
                background-color: {color};
                border-radius: 6px;
                border: none;
            }}
            QPushButton:hover {{
                background-color: {color};
                opacity: 0.8;
            }}
        """)
        btn.clicked.connect(callback)
        return btn
    
    def close_window(self):
        if self.parent_window:
            self.parent_window.close()
    
    def show_minimized(self):
        if self.parent_window:
            self.parent_window.showMinimized()
    
    def toggle_maximize(self):
        if self.parent_window:
            if self.parent_window.isMaximized():
                self.parent_window.showNormal()
            else:
                self.parent_window.showMaximized()
    
    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.start_pos = event.globalPosition().toPoint()
    
    def mouseMoveEvent(self, event):
        if self.start_pos:
            delta = event.globalPosition().toPoint() - self.start_pos
            if self.parent_window:
                self.parent_window.move(self.parent_window.pos() + delta)
            self.start_pos = event.globalPosition().toPoint()


class Header(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet("background-color: transparent;")
        
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 16, 0, 8)
        layout.setSpacing(4)
        
        # Time with clock icon
        time_layout = QHBoxLayout()
        time_layout.setSpacing(6)
        
        clock_label = QLabel("🕐")
        clock_label.setStyleSheet("font-size: 14px;")
        
        current_time = datetime.now().strftime("%I:%M %p")
        time_label = QLabel(current_time)
        time_label.setStyleSheet("color: #888888; font-size: 18px;")
        
        time_layout.addWidget(clock_label)
        time_layout.addWidget(time_label)
        time_layout.addStretch()
        
        layout.addLayout(time_layout)
        
        # Greeting
        current_hour = datetime.now().hour
        if current_hour < 12:
            greeting = "Good morning"
        elif current_hour < 18:
            greeting = "Good afternoon"
        else:
            greeting = "Good evening"
        
        greeting_label = QLabel(greeting)
        greeting_label.setStyleSheet("""
            QLabel {
                color: #ffffff;
                font-size: 36px;
                font-weight: bold;
            }
        """)
        
        layout.addWidget(greeting_label)


class Timeline(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet("background-color: transparent;")
        
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 8, 0, 16)
        layout.setSpacing(12)
        
        # Header
        header_layout = QHBoxLayout()
        
        today_label = QLabel("TODAY")
        today_label.setStyleSheet("""
            QLabel {
                color: #ffffff;
                font-size: 16px;
                font-weight: 600;
                letter-spacing: 1px;
            }
        """)
        
        progress_label = QLabel("75% OF DAY")
        progress_label.setStyleSheet("""
            QLabel {
                color: #888888;
                font-size: 13px;
                font-weight: 500;
                letter-spacing: 1px;
            }
        """)
        
        header_layout.addWidget(today_label)
        header_layout.addStretch()
        header_layout.addWidget(progress_label)
        
        layout.addLayout(header_layout)
        
        # Timeline track
        track_wrapper = QWidget()
        track_layout = QVBoxLayout(track_wrapper)
        track_layout.setContentsMargins(0, 0, 0, 0)
        track_layout.setSpacing(4)
        
        # Track with blocks container
        track_container = QWidget()
        track_container.setFixedHeight(45)
        track_container.setStyleSheet("""
            QWidget {
                background-color: #2a2a2a;
                border-radius: 22px;
            }
        """)
        
        track_container_layout = QHBoxLayout(track_container)
        track_container_layout.setContentsMargins(6, 6, 6, 6)
        track_container_layout.setSpacing(4)
        
        # Blue block (Deep work) with text
        blue_block = self.create_timeline_block("Deep work", "#007AFF", 120)
        track_container_layout.addWidget(blue_block)
        
        # Spacer
        track_container_layout.addStretch()
        
        # Gray block (empty)
        gray_block = self.create_timeline_block("", "#3a3a3a", 80)
        track_container_layout.addWidget(gray_block)
        
        # Orange block (Bug fixes) with text
        orange_block = self.create_timeline_block("Bug fixes", "#FF9500", 100)
        track_container_layout.addWidget(orange_block)
        
        # Green block with text
        green_block = self.create_timeline_block("Docs", "#34C759", 80)
        track_container_layout.addWidget(green_block)
        
        track_container_layout.addStretch()
        
        track_layout.addWidget(track_container)
        
        # Red current time indicator (overlay)
        current_time_indicator = QFrame()
        current_time_indicator.setFixedSize(2, 45)
        current_time_indicator.setStyleSheet("""
            QFrame {
                background-color: #FF3B30;
                border-radius: 1px;
            }
        """)
        current_time_indicator.move(200, 0)
        current_time_indicator.setParent(track_container)
        current_time_indicator.raise_()
        
        # Time labels
        time_labels = QHBoxLayout()
        time_labels.setSpacing(0)
        
        times = ["6a", "9a", "12p", "3p", "6p", "9p"]
        for time in times:
            label = QLabel(time)
            label.setStyleSheet("color: #666666; font-size: 12px;")
            time_labels.addWidget(label)
            time_labels.addStretch()
        
        track_layout.addLayout(time_labels)
        
        layout.addWidget(track_wrapper)
    
    def create_timeline_block(self, text, color, width):
        block = QFrame()
        block.setFixedSize(width, 33)
        block.setStyleSheet(f"""
            QFrame {{
                background-color: {color};
                border-radius: 16px;
            }}
        """)
        
        if text:
            block_layout = QVBoxLayout(block)
            block_layout.setContentsMargins(0, 0, 0, 0)
            block_layout.setSpacing(0)
            
            label = QLabel(text)
            label.setStyleSheet("""
                QLabel {
                    color: #ffffff;
                    font-size: 11px;
                    font-weight: 600;
                }
            """)
            label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            block_layout.addWidget(label)
        
        return block


class StatCards(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet("background-color: transparent;")
        
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 8, 0, 16)
        layout.setSpacing(12)
        
        # Card 1 - Focused
        card1 = self.create_card("Focused", "4h 30m")
        layout.addWidget(card1)
        
        # Card 2 - Blocks done
        card2 = self.create_card("Blocks done", "3/3")
        layout.addWidget(card2)
    
    def create_card(self, subtitle, main_text):
        card = QFrame()
        card.setMinimumHeight(100)
        card.setStyleSheet("""
            QFrame {
                background-color: #2b2b2b;
                border-radius: 12px;
            }
        """)
        
        card_layout = QVBoxLayout(card)
        card_layout.setContentsMargins(20, 16, 20, 16)
        card_layout.setSpacing(8)
        
        subtitle_label = QLabel(subtitle)
        subtitle_label.setStyleSheet("""
            QLabel {
                color: #888888;
                font-size: 14px;
                font-weight: 500;
            }
        """)
        
        main_label = QLabel(main_text)
        main_label.setStyleSheet("""
            QLabel {
                color: #ffffff;
                font-size: 32px;
                font-weight: bold;
            }
        """)
        
        card_layout.addWidget(subtitle_label)
        card_layout.addWidget(main_label)
        
        return card


class ScheduleItem(QWidget):
    def __init__(self, title, time_range, color, parent=None):
        super().__init__(parent)
        self.setFixedHeight(70)
        self.setStyleSheet("""
            QWidget {
                background-color: #2b2b2b;
                border-radius: 12px;
            }
        """)
        
        layout = QHBoxLayout(self)
        layout.setContentsMargins(15, 15, 15, 15)
        layout.setSpacing(15)
        
        # Color indicator
        indicator = QFrame()
        indicator.setFixedWidth(5)
        indicator.setStyleSheet(f"""
            QFrame {{
                background-color: {color};
                border-radius: 2px;
            }}
        """)
        
        # Content
        content_layout = QVBoxLayout()
        content_layout.setSpacing(4)
        
        title_label = QLabel(title)
        title_label.setStyleSheet("""
            QLabel {
                color: #ffffff;
                font-size: 16px;
                font-weight: 500;
            }
        """)
        
        time_label = QLabel(time_range)
        time_label.setStyleSheet("""
            QLabel {
                color: #888888;
                font-size: 14px;
            }
        """)
        
        content_layout.addWidget(title_label)
        content_layout.addWidget(time_label)
        
        # Checkmark
        checkmark = QLabel("✓")
        checkmark.setStyleSheet("""
            QLabel {
                color: #444444;
                font-size: 18px;
                font-weight: bold;
            }
        """)
        
        layout.addWidget(indicator)
        layout.addLayout(content_layout)
        layout.addStretch()
        layout.addWidget(checkmark)


class Schedule(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet("background-color: transparent;")
        
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 8, 0, 16)
        layout.setSpacing(8)
        
        # Header
        schedule_label = QLabel("SCHEDULE")
        schedule_label.setStyleSheet("""
            QLabel {
                color: #ffffff;
                font-size: 16px;
                font-weight: 600;
                letter-spacing: 1px;
            }
        """)
        
        layout.addWidget(schedule_label)
        
        # Schedule items
        items = [
            ("Deep work", "9a - 12p", "#007AFF"),
            ("Lunch", "12p - 1p", "#FF9500"),
            ("Bug fixes", "2p - 3:30p", "#FF3B30"),
            ("Documentation", "4p - 5p", "#34C759")
        ]
        
        for title, time_range, color in items:
            item = ScheduleItem(title, time_range, color)
            layout.addWidget(item)


class NavigationBar(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet("background-color: transparent;")
        
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        
        # Dock container
        dock = QFrame()
        dock.setStyleSheet("""
            QFrame {
                background-color: #1a1a1a;
                border-radius: 16px;
            }
        """)
        
        dock_layout = QHBoxLayout(dock)
        dock_layout.setContentsMargins(12, 8, 12, 8)
        dock_layout.setSpacing(8)
        
        # Icons with SVG paths
        icons = [
            ("home.svg", True),
            ("clock.svg", False),
            ("calendar.svg", False),
            ("layers.svg", False),
            ("flame.svg", False),
            ("chart.svg", False),
            ("trophy.svg", False)
        ]
        
        for icon_path, active in icons:
            btn = QPushButton()
            try:
                btn.setIcon(QIcon(icon_path))
                btn.setIconSize(QSize(24, 24))
            except:
                # Fallback if SVG doesn't exist
                btn.setText("•")
            
            if active:
                btn.setStyleSheet("""
                    QPushButton {
                        background-color: transparent;
                        border: none;
                        padding: 8px;
                        border-radius: 8px;
                    }
                    QPushButton:hover {
                        background-color: #2a2a2a;
                    }
                """)
            else:
                btn.setStyleSheet("""
                    QPushButton {
                        background-color: transparent;
                        border: none;
                        padding: 8px;
                        border-radius: 8px;
                    }
                    QPushButton:hover {
                        background-color: #2a2a2a;
                    }
                """)
            btn.setFixedSize(48, 48)
            dock_layout.addWidget(btn)
        
        layout.addStretch()
        layout.addWidget(dock)
        layout.addStretch()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setFixedSize(850, 700)
        
        # Main container with rounded corners and shadow
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        
        self.central_widget.setStyleSheet("""
            QWidget {
                background-color: #1e1e1e;
                border-radius: 12px;
            }
        """)
        
        main_layout = QVBoxLayout(self.central_widget)
        main_layout.setContentsMargins(30, 30, 30, 30)
        main_layout.setSpacing(20)
        
        # Title bar
        self.title_bar = TitleBar(self)
        main_layout.addWidget(self.title_bar)
        
        # Content area
        content = QWidget()
        content.setStyleSheet("background-color: transparent;")
        content_layout = QVBoxLayout(content)
        content_layout.setContentsMargins(0, 0, 0, 0)
        content_layout.setSpacing(20)
        
        # Header
        self.header = Header()
        content_layout.addWidget(self.header)
        
        # Timeline
        self.timeline = Timeline()
        content_layout.addWidget(self.timeline)
        
        # Stat cards
        self.stat_cards = StatCards()
        content_layout.addWidget(self.stat_cards)
        
        # Schedule
        self.schedule = Schedule()
        content_layout.addWidget(self.schedule)
        
        main_layout.addWidget(content)
        
        # Navigation bar
        self.nav_bar = NavigationBar()
        main_layout.addWidget(self.nav_bar)
        
        self.start_pos = QPoint()
    
    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.start_pos = event.globalPosition().toPoint()
    
    def mouseMoveEvent(self, event):
        if self.start_pos:
            delta = event.globalPosition().toPoint() - self.start_pos
            self.move(self.pos() + delta)
            self.start_pos = event.globalPosition().toPoint()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Set font
    font = QFont("Segoe UI", 10)
    app.setFont(font)
    
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec())
