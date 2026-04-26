import sys
from datetime import datetime
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QLabel, QPushButton, QFrame, QSizePolicy,
                             QGraphicsColorizeEffect, QSpacerItem, QStackedWidget)
from PyQt6.QtCore import Qt, QPoint, QSize
from PyQt6.QtGui import QIcon, QPainter, QColor, QPen, QFont
from tasks import TasksPage
from think import ThinkPage
from schedule import SchedulePage
from workspaces import WorkspacesPage
from habits import HabitsPage


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
        status_label.setStyleSheet("color: #ffffff; font-size: 13px; font-weight: 500; border: none; background: transparent;")
        
        settings_btn = QPushButton()
        try:
            settings_btn.setIcon(QIcon("settings.svg"))
            settings_btn.setIconSize(QSize(18, 18))
            # Colorize icon to white
            colorize_effect = QGraphicsColorizeEffect()
            colorize_effect.setColor(Qt.GlobalColor.white)
            settings_btn.setGraphicsEffect(colorize_effect)
        except:
            settings_btn.setText("⚙")
        settings_btn.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                border: none;
                padding: 4px;
                border-radius: 4px;
            }
            QPushButton:hover {
                background-color: rgba(255, 255, 255, 0.1);
            }
        """)
        settings_btn.setFixedSize(28, 28)
        
        expand_btn = QPushButton()
        try:
            expand_btn.setIcon(QIcon("expand.svg"))
            expand_btn.setIconSize(QSize(18, 18))
            # Colorize icon to white
            colorize_effect = QGraphicsColorizeEffect()
            colorize_effect.setColor(Qt.GlobalColor.white)
            expand_btn.setGraphicsEffect(colorize_effect)
        except:
            expand_btn.setText("⤢")
        expand_btn.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                border: none;
                padding: 4px;
                border-radius: 4px;
            }
            QPushButton:hover {
                background-color: rgba(255, 255, 255, 0.1);
            }
        """)
        expand_btn.setFixedSize(28, 28)
        
        cmd_badge = QLabel("⌘ K")
        cmd_badge.setStyleSheet("""
            QLabel {
                background-color: #3a3a3a;
                color: #888888;
                padding: 4px 8px;
                border-radius: 4px;
                font-size: 11px;
                border: none;
            }
        """)
        
        status_layout.addWidget(status_dot)
        status_layout.addWidget(status_label)
        status_layout.addWidget(settings_btn)
        status_layout.addWidget(expand_btn)
        status_layout.addWidget(cmd_badge)
        
        layout.addLayout(status_layout)
        
        # Windows-style window controls
        window_controls = QHBoxLayout()
        window_controls.setSpacing(4)
        
        self.minimize_btn = self.create_window_button("─", self.show_minimized)
        self.maximize_btn = self.create_window_button("□", self.toggle_maximize)
        self.close_btn = self.create_window_button("✕", self.close_window)
        
        window_controls.addWidget(self.minimize_btn)
        window_controls.addWidget(self.maximize_btn)
        window_controls.addWidget(self.close_btn)
        
        layout.addLayout(window_controls)
        
        self.parent_window = parent
        self.start_pos = QPoint()
        
    def create_window_button(self, symbol, callback):
        btn = QPushButton(symbol)
        btn.setFixedSize(30, 30)
        btn.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                color: #ffffff;
                border: none;
                font-size: 16px;
                font-weight: normal;
            }
            QPushButton:hover {
                background-color: rgba(255, 255, 255, 0.1);
            }
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
        
        clock_label = QLabel("")
        clock_label.setStyleSheet("font-size: 14px; border: none; background: transparent;")
        
        current_time = datetime.now().strftime("%I:%M %p")
        time_label = QLabel(current_time)
        time_label.setStyleSheet("color: #888888; font-size: 18px; border: none; background: transparent;")
        
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
                border: none;
                background: transparent;
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
                border: none;
                background: transparent;
            }
        """)
        
        progress_label = QLabel("75% OF DAY")
        progress_label.setStyleSheet("""
            QLabel {
                color: #888888;
                font-size: 13px;
                font-weight: 500;
                letter-spacing: 1px;
                border: none;
                background: transparent;
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
        track_container.setFixedHeight(100)
        track_container.setStyleSheet("""
            QWidget {
                background-color: rgba(30, 30, 30, 0.6);
                border-radius: 20px;
                border: 1px solid rgba(255, 255, 255, 0.08);
            }
        """)
        
        track_container_layout = QHBoxLayout(track_container)
        track_container_layout.setContentsMargins(0, 0, 0, 0)
        track_container_layout.setSpacing(0)
        
        # 6am to 9am spacer (3 hours = 300px total, but this is empty)
        track_container_layout.addSpacing(0)
        
        # Blue block (Deep work 9am-12pm = 3 hours = 300px)
        blue_block = self.create_timeline_block("Deep work", "rgba(64, 169, 255, 0.25)", 300)
        track_container_layout.addWidget(blue_block)
        
        # 12pm to 1pm spacer (1 hour = 100px)
        track_container_layout.addSpacing(100)
        
        # Orange block (Bug fixes 2pm-3:30pm = 1.5 hours = 150px)
        orange_block = self.create_timeline_block("Bug fixes", "rgba(255, 159, 10, 0.25)", 150)
        track_container_layout.addWidget(orange_block)
        
        # 3:30pm to 4pm spacer (0.5 hour = 50px)
        track_container_layout.addSpacing(50)
        
        # Green block (Docs 4pm-5pm = 1 hour = 100px)
        green_block = self.create_timeline_block("Docs", "rgba(48, 209, 88, 0.25)", 100)
        track_container_layout.addWidget(green_block)
        
        track_container_layout.addStretch()
        
        track_layout.addWidget(track_container)
        
        # Red current time indicator (overlay)
        current_time_indicator = QFrame()
        current_time_indicator.setFixedSize(2, 100)
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
        
        times = ["6am", "9am", "12pm", "3pm", "6pm", "9pm"]
        for time in times:
            label = QLabel(time)
            label.setStyleSheet("color: #666666; font-size: 12px; border: none; background: transparent;")
            time_labels.addWidget(label)
            time_labels.addStretch()
        
        track_layout.addLayout(time_labels)
        
        layout.addWidget(track_wrapper)
    
    def create_timeline_block(self, text, color, width):
        block = QFrame()
        block.setMinimumWidth(width)
        block.setFixedHeight(100)
        block.setStyleSheet(f"""
            QFrame {{
                background-color: {color};
                border: 1px solid {color.replace('0.25', '0.5')};
                border-radius: 12px;
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
                    border: none;
                    background: transparent;
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
        card.setMinimumHeight(120)
        card.setStyleSheet("""
            QFrame {
                background-color: rgba(255, 255, 255, 0.05);
                border-radius: 12px;
                border: 1px solid rgba(255, 255, 255, 0.08);
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
                border: none;
                background: transparent;
            }
        """)
        
        main_label = QLabel(main_text)
        main_label.setStyleSheet("""
            QLabel {
                color: #ffffff;
                font-size: 32px;
                font-weight: bold;
                border: none;
                background: transparent;
            }
        """)
        
        card_layout.addWidget(subtitle_label)
        card_layout.addWidget(main_label)
        
        return card


class ScheduleItem(QWidget):
    def __init__(self, title, time_range, color, parent=None):
        super().__init__(parent)
        self.setStyleSheet("background-color: transparent;")
        
        # Create wrapper frame for glassmorphic background
        wrapper = QFrame()
        wrapper.setStyleSheet("""
            QFrame {
                background-color: rgba(255, 255, 255, 0.05);
                border: 1px solid rgba(255, 255, 255, 0.1);
                border-radius: 10px;
            }
        """)
        
        wrapper_layout = QHBoxLayout(wrapper)
        wrapper_layout.setContentsMargins(15, 15, 15, 15)
        wrapper_layout.setSpacing(15)
        
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
                border: none;
                background: transparent;
            }
        """)
        
        time_label = QLabel(time_range)
        time_label.setStyleSheet("""
            QLabel {
                color: #888888;
                font-size: 14px;
                border: none;
                background: transparent;
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
                border: none;
                background: transparent;
            }
        """)
        
        wrapper_layout.addWidget(indicator)
        wrapper_layout.addLayout(content_layout)
        wrapper_layout.addStretch()
        wrapper_layout.addWidget(checkmark)
        
        # Main layout
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.addWidget(wrapper)


class Schedule(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet("background-color: transparent;")
        
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 8, 0, 16)
        layout.setSpacing(10)
        
        # Header
        schedule_label = QLabel("SCHEDULE")
        schedule_label.setStyleSheet("""
            QLabel {
                color: #ffffff;
                font-size: 16px;
                font-weight: 600;
                letter-spacing: 1px;
                border: none;
                background: transparent;
            }
        """)
        
        layout.addWidget(schedule_label)
        
        # Schedule items
        items = [
            ("Deep work", "9am - 12pm", "#007AFF"),
            ("Lunch", "12pm - 1pm", "#FF9500"),
            ("Bug fixes", "2pm - 3:30pm", "#FF3B30"),
            ("Documentation", "4pm - 5pm", "#34C759")
        ]
        
        for title, time_range, color in items:
            item = ScheduleItem(title, time_range, color)
            layout.addWidget(item)


class NavigationBar(QWidget):
    def __init__(self, navigate_callback=None, parent=None):
        super().__init__(parent)
        self.setFixedHeight(50)
        self.setStyleSheet("background-color: transparent;")
        self.navigate_callback = navigate_callback
        self.nav_buttons = {}  # Store button references for updating active state
        
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        
        # Dock container
        dock = QFrame()
        dock.setStyleSheet("""
            QFrame {
                background-color: rgba(255, 255, 255, 0.05);
                border-radius: 16px;
                border: 1px solid rgba(255, 255, 255, 0.08);
            }
        """)
        
        dock_layout = QHBoxLayout(dock)
        dock_layout.setContentsMargins(8, 6, 8, 6)
        dock_layout.setSpacing(6)
        
        # Icons with SVG paths - Home is now active
        icons = [
            ("home.svg", True, "dashboard"),
            ("clock.svg", False, "tasks"),
            ("calendar.svg", False, "schedule"),
            ("layers.svg", False, "workspaces"),
            ("brain.svg", False, "think"),
            ("flame.svg", False, "habits"),
            ("chart.svg", False, None)
        ]
        
        for icon_path, active, page_name in icons:
            btn = QPushButton()
            try:
                btn.setIcon(QIcon(icon_path))
                btn.setIconSize(QSize(20, 20))
                # Colorize icon to white
                colorize_effect = QGraphicsColorizeEffect()
                colorize_effect.setColor(Qt.GlobalColor.white)
                btn.setGraphicsEffect(colorize_effect)
            except:
                # Fallback if SVG doesn't exist
                btn.setText("•")
            
            if active:
                btn.setStyleSheet("""
                    QPushButton {
                        background-color: rgba(255, 255, 255, 0.15);
                        border: none;
                        padding: 6px;
                        border-radius: 6px;
                    }
                    QPushButton:hover {
                        background-color: rgba(255, 255, 255, 0.2);
                    }
                """)
            else:
                btn.setStyleSheet("""
                    QPushButton {
                        background-color: transparent;
                        border: none;
                        padding: 6px;
                        border-radius: 6px;
                    }
                    QPushButton:hover {
                        background-color: rgba(255, 255, 255, 0.1);
                    }
                """)
            btn.setFixedSize(36, 36)
            
            # Connect button to navigation callback
            if page_name and self.navigate_callback:
                btn.clicked.connect(lambda checked, p=page_name: self.navigate_callback(p))
            
            # Store button reference
            if page_name:
                self.nav_buttons[page_name] = btn
            
            dock_layout.addWidget(btn)
        
        layout.addStretch()
        layout.addWidget(dock)
        layout.addStretch()
    
    def set_active_page(self, page_name):
        # Reset all buttons to inactive
        for btn in self.nav_buttons.values():
            btn.setStyleSheet("""
                QPushButton {
                    background-color: transparent;
                    border: none;
                    padding: 6px;
                    border-radius: 6px;
                }
                QPushButton:hover {
                    background-color: rgba(255, 255, 255, 0.1);
                }
            """)
        
        # Set active button
        if page_name in self.nav_buttons:
            self.nav_buttons[page_name].setStyleSheet("""
                QPushButton {
                    background-color: rgba(255, 255, 255, 0.15);
                    border: none;
                    padding: 6px;
                    border-radius: 6px;
                }
                QPushButton:hover {
                    background-color: rgba(255, 255, 255, 0.2);
                }
            """)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.showMaximized()
        
        # Main container with rounded corners and shadow
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        
        self.central_widget.setStyleSheet("""
            QWidget {
                background-color: #000000;
                border-radius: 12px;
            }
        """)
        
        main_layout = QVBoxLayout(self.central_widget)
        main_layout.setContentsMargins(40, 25, 40, 25)
        main_layout.setSpacing(25)
        
        # Title bar
        self.title_bar = TitleBar(self)
        main_layout.addWidget(self.title_bar)
        
        # Content area with stacked widget for page switching
        content = QWidget()
        content.setStyleSheet("background-color: transparent;")
        content_layout = QVBoxLayout(content)
        content_layout.setContentsMargins(0, 0, 0, 0)
        content_layout.setSpacing(0)
        
        # Stacked widget for page switching
        self.stacked_widget = QStackedWidget()
        self.stacked_widget.setStyleSheet("background-color: transparent;")
        
        # Dashboard page
        self.dashboard_page = QWidget()
        self.dashboard_page.setStyleSheet("background-color: transparent;")
        dashboard_layout = QVBoxLayout(self.dashboard_page)
        dashboard_layout.setContentsMargins(0, 0, 0, 0)
        dashboard_layout.setSpacing(25)
        
        # Header
        self.header = Header()
        dashboard_layout.addWidget(self.header)
        
        # Timeline
        self.timeline = Timeline()
        dashboard_layout.addWidget(self.timeline)
        
        # Stat cards
        self.stat_cards = StatCards()
        dashboard_layout.addWidget(self.stat_cards)
        
        # Schedule
        self.schedule = Schedule()
        dashboard_layout.addWidget(self.schedule)
        
        # Tasks page
        self.tasks_page = TasksPage()
        
        # Think page
        self.think_page = ThinkPage()
        
        # Schedule page
        self.schedule_page = SchedulePage()
        
        # Workspaces page
        self.workspaces_page = WorkspacesPage()
        
        # Habits page
        self.habits_page = HabitsPage()
        
        # Add pages to stacked widget
        self.stacked_widget.addWidget(self.dashboard_page)
        self.stacked_widget.addWidget(self.tasks_page)
        self.stacked_widget.addWidget(self.think_page)
        self.stacked_widget.addWidget(self.schedule_page)
        self.stacked_widget.addWidget(self.workspaces_page)
        self.stacked_widget.addWidget(self.habits_page)
        
        # Set dashboard as default
        self.stacked_widget.setCurrentWidget(self.dashboard_page)
        
        content_layout.addWidget(self.stacked_widget)
        
        main_layout.addWidget(content)
        
        # Navigation bar with navigation callbacks
        self.nav_bar = NavigationBar(self.navigate_to_page)
        main_layout.addWidget(self.nav_bar)
        
        self.current_page = "dashboard"
        
        self.start_pos = QPoint()
    
    def navigate_to_page(self, page_name):
        if page_name == "dashboard":
            self.stacked_widget.setCurrentWidget(self.dashboard_page)
            self.current_page = "dashboard"
        elif page_name == "tasks":
            self.stacked_widget.setCurrentWidget(self.tasks_page)
            self.current_page = "tasks"
        elif page_name == "think":
            self.stacked_widget.setCurrentWidget(self.think_page)
            self.current_page = "think"
        elif page_name == "schedule":
            self.stacked_widget.setCurrentWidget(self.schedule_page)
            self.current_page = "schedule"
        elif page_name == "workspaces":
            self.stacked_widget.setCurrentWidget(self.workspaces_page)
            self.current_page = "workspaces"
        elif page_name == "habits":
            self.stacked_widget.setCurrentWidget(self.habits_page)
            self.current_page = "habits"
        
        # Update navigation bar active state
        self.nav_bar.set_active_page(page_name)
    
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
