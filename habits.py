from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, 
                             QPushButton, QFrame, QScrollArea, QGraphicsColorizeEffect)
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon


class HabitsPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet("background-color: transparent;")
        
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 16, 0, 16)
        layout.setSpacing(20)
        
        # Header
        header = self.create_header()
        layout.addWidget(header)
        
        # Active reminders
        reminders = self.create_active_reminders()
        layout.addWidget(reminders)
        
        # Weekly tracker section
        tracker = self.create_weekly_tracker()
        layout.addWidget(tracker)
    
    def create_header(self):
        header = QWidget()
        header.setStyleSheet("background-color: transparent;")
        
        layout = QHBoxLayout(header)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(20)
        layout.setAlignment(Qt.AlignmentFlag.AlignVCenter)
        
        # Left side: Title and stats
        left_layout = QVBoxLayout()
        left_layout.setSpacing(4)
        
        title = QLabel("Habits")
        title.setStyleSheet("""
            QLabel {
                color: #ffffff;
                font-size: 28px;
                font-weight: bold;
                border: none;
                background: transparent;
            }
        """)
        
        stats = QLabel("4/5 done today · 2 active")
        stats.setStyleSheet("""
            QLabel {
                color: #888888;
                font-size: 14px;
                border: none;
                background: transparent;
            }
        """)
        
        left_layout.addWidget(title)
        left_layout.addWidget(stats)
        
        # Right side: + button
        add_btn = QPushButton("+")
        add_btn.setFixedSize(40, 40)
        add_btn.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        add_btn.setStyleSheet("""
            QPushButton {
                background-color: #007AFF;
                color: white;
                border-radius: 10px;
                font-size: 24px;
                font-weight: normal;
                border: none;
                padding-bottom: 4px;
            }
            QPushButton:hover {
                background-color: #0056CC;
            }
        """)
        
        layout.addLayout(left_layout)
        layout.addStretch()
        layout.addWidget(add_btn)
        
        return header
    
    def create_active_reminders(self):
        container = QWidget()
        container.setStyleSheet("background-color: transparent;")
        
        layout = QVBoxLayout(container)
        layout.setSpacing(12)
        
        # Drink water card
        water_card = self.create_reminder_card("Drink water", "Every 30m · 2:30 PM", "#007AFF", "water.svg")
        layout.addWidget(water_card)
        
        # Take vitamins card
        vitamins_card = self.create_reminder_card("Take vitamins", "Daily · 9:00 AM", "#FF3B30", "vitamin.svg")
        layout.addWidget(vitamins_card)
        
        return container
    
    def create_reminder_card(self, title, schedule, color, icon_path):
        card = QFrame()
        card.setStyleSheet("""
            QFrame {
                background-color: rgba(255, 255, 255, 0.05);
                border: 1px solid rgba(255, 255, 255, 0.08);
                border-radius: 12px;
            }
        """)
        
        layout = QVBoxLayout(card)
        layout.setContentsMargins(16, 16, 16, 16)
        layout.setSpacing(12)
        
        # Top row
        top_row = QHBoxLayout()
        top_row.setSpacing(12)
        
        # Icon
        icon_label = QLabel()
        icon_label.setFixedSize(32, 32)
        icon_label.setPixmap(QIcon(icon_path).pixmap(24, 24))
        icon_label.setStyleSheet("border: none; background: transparent;")
        
        # Title
        title_label = QLabel(title)
        title_label.setStyleSheet("""
            QLabel {
                color: #ffffff;
                font-size: 16px;
                font-weight: bold;
                border: none;
                background: transparent;
            }
        """)
        
        top_row.addWidget(icon_label)
        top_row.addWidget(title_label)
        top_row.addStretch()
        
        # Schedule label
        schedule_label = QLabel(schedule)
        schedule_label.setStyleSheet("""
            QLabel {
                color: #888888;
                font-size: 13px;
                border: none;
                background: transparent;
            }
        """)
        top_row.addWidget(schedule_label)
        
        # Bottom row: Action buttons
        bottom_row = QHBoxLayout()
        bottom_row.setSpacing(10)
        
        # Did it button (colored)
        did_it_btn = QPushButton("✓ Did it")
        did_it_btn.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        did_it_btn.setStyleSheet(f"""
            QPushButton {{
                background-color: {color}33;
                color: {color};
                border: none;
                border-radius: 8px;
                padding: 8px 16px;
                font-size: 13px;
            }}
            QPushButton:hover {{
                background-color: {color}44;
            }}
        """)
        
        # Other buttons (gray glass)
        snooze_btn = QPushButton("⏱ Snooze")
        snooze_btn.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        snooze_btn.setStyleSheet("""
            QPushButton {
                background-color: rgba(255, 255, 255, 0.1);
                color: #888888;
                border: none;
                border-radius: 8px;
                padding: 8px 16px;
                font-size: 13px;
            }
            QPushButton:hover {
                background-color: rgba(255, 255, 255, 0.15);
                color: #ffffff;
            }
        """)
        
        skip_btn = QPushButton("▷ Skip")
        skip_btn.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        skip_btn.setStyleSheet("""
            QPushButton {
                background-color: rgba(255, 255, 255, 0.1);
                color: #888888;
                border: none;
                border-radius: 8px;
                padding: 8px 16px;
                font-size: 13px;
            }
            QPushButton:hover {
                background-color: rgba(255, 255, 255, 0.15);
                color: #ffffff;
            }
        """)
        
        reschedule_btn = QPushButton("↻ Reschedule")
        reschedule_btn.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        reschedule_btn.setStyleSheet("""
            QPushButton {
                background-color: rgba(255, 255, 255, 0.1);
                color: #888888;
                border: none;
                border-radius: 8px;
                padding: 8px 16px;
                font-size: 13px;
            }
            QPushButton:hover {
                background-color: rgba(255, 255, 255, 0.15);
                color: #ffffff;
            }
        """)
        
        bottom_row.addWidget(did_it_btn)
        bottom_row.addWidget(snooze_btn)
        bottom_row.addWidget(skip_btn)
        bottom_row.addWidget(reschedule_btn)
        bottom_row.addStretch()
        
        layout.addLayout(top_row)
        layout.addLayout(bottom_row)
        
        return card
    
    def create_weekly_tracker(self):
        section = QWidget()
        section.setStyleSheet("background-color: transparent;")
        
        layout = QVBoxLayout(section)
        layout.setSpacing(16)
        
        # Navigation header
        nav_header = self.create_tracker_nav()
        layout.addWidget(nav_header)
        
        # Column headers
        col_headers = self.create_column_headers()
        layout.addWidget(col_headers)
        
        # Tracker rows (scroll area)
        tracker_scroll = self.create_tracker_list()
        layout.addWidget(tracker_scroll)
        
        return section
    
    def create_tracker_nav(self):
        nav = QWidget()
        nav.setStyleSheet("background-color: transparent;")
        
        layout = QHBoxLayout(nav)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(12)
        
        # Left arrow
        left_arrow = QPushButton()
        left_arrow.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        try:
            left_arrow.setIcon(QIcon("chevron-left.svg"))
            left_arrow.setIconSize(QSize(20, 20))
            colorize_effect = QGraphicsColorizeEffect()
            colorize_effect.setColor(Qt.GlobalColor.white)
            left_arrow.setGraphicsEffect(colorize_effect)
        except:
            left_arrow.setText("<")
        left_arrow.setStyleSheet("""
            QPushButton {
                background-color: rgba(255, 255, 255, 0.1);
                border: none;
                border-radius: 8px;
                color: #ffffff;
                font-size: 16px;
            }
            QPushButton:hover {
                background-color: rgba(255, 255, 255, 0.15);
            }
        """)
        left_arrow.setFixedSize(32, 32)
        
        # Title
        title = QLabel("This Week")
        title.setStyleSheet("""
            QLabel {
                color: #ffffff;
                font-size: 16px;
                font-weight: 500;
                border: none;
                background: transparent;
            }
        """)
        
        # Right arrow
        right_arrow = QPushButton()
        right_arrow.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        try:
            right_arrow.setIcon(QIcon("chevron-right.svg"))
            right_arrow.setIconSize(QSize(20, 20))
            colorize_effect = QGraphicsColorizeEffect()
            colorize_effect.setColor(Qt.GlobalColor.white)
            right_arrow.setGraphicsEffect(colorize_effect)
        except:
            right_arrow.setText(">")
        right_arrow.setStyleSheet("""
            QPushButton {
                background-color: rgba(255, 255, 255, 0.1);
                border: none;
                border-radius: 8px;
                color: #ffffff;
                font-size: 16px;
            }
            QPushButton:hover {
                background-color: rgba(255, 255, 255, 0.15);
            }
        """)
        right_arrow.setFixedSize(32, 32)
        
        layout.addWidget(left_arrow)
        layout.addStretch()
        layout.addWidget(title)
        layout.addStretch()
        layout.addWidget(right_arrow)
        
        return nav
    
    def create_column_headers(self):
        headers = QWidget()
        headers.setStyleSheet("background-color: transparent;")
        
        layout = QHBoxLayout(headers)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        
        # Habit label
        habit_label = QLabel("Habit")
        habit_label.setStyleSheet("""
            QLabel {
                color: #888888;
                font-size: 12px;
                font-weight: 500;
                border: none;
                background: transparent;
            }
        """)
        habit_label.setFixedWidth(200)
        
        layout.addWidget(habit_label)
        layout.addStretch()
        
        # Day labels with same spacing as checkboxes (8px)
        days = ["M", "T", "W", "T", "F", "S", "S"]
        for i, day in enumerate(days):
            day_label = QLabel(day)
            if i == 1:  # Current day (Tuesday)
                day_label.setStyleSheet("""
                    QLabel {
                        background-color: rgba(0, 122, 255, 0.2);
                        color: #ffffff;
                        padding: 4px 10px;
                        border-radius: 10px;
                        font-size: 12px;
                        font-weight: 500;
                        border: none;
                    }
                """)
            else:
                day_label.setStyleSheet("""
                    QLabel {
                        color: #888888;
                        font-size: 12px;
                        font-weight: 500;
                        border: none;
                        background: transparent;
                    }
                """)
            day_label.setFixedWidth(32)
            day_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            layout.addWidget(day_label)
        
        return headers
    
    def create_tracker_list(self):
        scroll = QScrollArea()
        scroll.setStyleSheet("""
            QScrollArea {
                background-color: transparent;
                border: none;
            }
            QScrollArea > QWidget > QWidget {
                background-color: transparent;
            }
            QScrollBar:vertical {
                background-color: transparent;
                width: 6px;
                border: none;
            }
            QScrollBar::handle:vertical {
                background-color: rgba(255, 255, 255, 0.2);
                border-radius: 3px;
                min-height: 20px;
            }
            QScrollBar::handle:vertical:hover {
                background-color: rgba(255, 255, 255, 0.3);
            }
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                height: 0px;
            }
            QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
                background: none;
            }
        """)
        scroll.setWidgetResizable(True)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        
        # Container
        container = QWidget()
        container.setStyleSheet("background-color: transparent;")
        
        container_layout = QVBoxLayout(container)
        container_layout.setContentsMargins(0, 0, 0, 0)
        container_layout.setSpacing(0)
        
        # Habit rows
        habits = [
            ("Exercise", "10/66d", "30d active", "#FF9500", "exercise.svg"),
            ("Read", "45/66d", "45d active", "#AF52DE", "read.svg"),
            ("Take vitamins", "66/66d", "66d active", "#FF3B30", "vitamin.svg"),
            ("Meditate", "20/66d", "20d active", "#5AC8FA", "meditate.svg")
        ]
        
        for title, progress, active, color, icon in habits:
            row = self.create_tracker_row(title, progress, active, color, icon)
            container_layout.addWidget(row)
        
        scroll.setWidget(container)
        
        return scroll
    
    def create_tracker_row(self, title, progress, active, color, icon_path):
        row = QWidget()
        row.setStyleSheet("""
            QWidget {
                background-color: transparent;
                border-bottom: 1px solid rgba(255, 255, 255, 0.05);
            }
        """)
        row.setFixedHeight(60)
        
        layout = QHBoxLayout(row)
        layout.setContentsMargins(0, 12, 0, 12)
        layout.setSpacing(12)
        
        # Left side: Icon and info
        icon_wrapper = QFrame()
        icon_wrapper.setFixedSize(36, 36)
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
        
        # Info layout
        info_layout = QVBoxLayout()
        info_layout.setSpacing(4)
        
        title_label = QLabel(title)
        title_label.setStyleSheet("""
            QLabel {
                color: #ffffff;
                font-size: 14px;
                font-weight: 500;
                border: none;
                background: transparent;
            }
        """)
        
        progress_label = QLabel(progress)
        progress_label.setStyleSheet(f"""
            QLabel {{
                color: {color};
                font-size: 12px;
                border: none;
                background: transparent;
            }}
        """)
        
        # Metadata row
        meta_row = QHBoxLayout()
        meta_row.setSpacing(8)
        
        active_label = QLabel(active)
        active_label.setStyleSheet("""
            QLabel {
                color: #888888;
                font-size: 11px;
                border: none;
                background: transparent;
            }
        """)
        
        fire_label = QLabel()
        fire_label.setFixedSize(14, 14)
        try:
            fire_label.setPixmap(QIcon("flame.svg").pixmap(12, 12))
            colorize_effect = QGraphicsColorizeEffect()
            colorize_effect.setColor(QColor("#FF9500"))
            fire_label.setGraphicsEffect(colorize_effect)
        except:
            fire_label.setText("")
        fire_label.setStyleSheet("border: none; background: transparent;")
        
        meta_row.addWidget(active_label)
        meta_row.addWidget(fire_label)
        
        info_layout.addWidget(title_label)
        info_layout.addWidget(progress_label)
        info_layout.addLayout(meta_row)
        
        # Checkboxes
        checkboxes = QHBoxLayout()
        checkboxes.setSpacing(8)
        
        # Sample states: checked, checked, checked, checked, unchecked, future, future
        states = ["checked", "checked", "checked", "checked", "unchecked", "future", "future"]
        
        for state in states:
            checkbox = self.create_checkbox(state, color)
            checkboxes.addWidget(checkbox)
        
        layout.addWidget(icon_wrapper)
        layout.addLayout(info_layout)
        layout.addStretch()
        layout.addLayout(checkboxes)
        
        return row
    
    def create_checkbox(self, state, color):
        checkbox = QPushButton()
        checkbox.setFixedSize(32, 32)
        checkbox.setFocusPolicy(Qt.FocusPolicy.NoFocus)  # Prevent focus taking
        
        if state == "checked":
            checkbox.setStyleSheet(f"""
                QPushButton {{
                    background-color: {color};
                    border: none;
                    border-radius: 8px;
                }}
            """)
            try:
                checkbox.setIcon(QIcon("check.svg"))
                checkbox.setIconSize(QSize(16, 16))
                colorize_effect = QGraphicsColorizeEffect()
                colorize_effect.setColor(QColor(color))  # Use category color instead of white
                checkbox.setGraphicsEffect(colorize_effect)
            except:
                checkbox.setText("")
        elif state == "unchecked":
            checkbox.setStyleSheet("""
                QPushButton {
                    background-color: rgba(255, 255, 255, 0.05);
                    border: 1px solid rgba(255, 255, 255, 0.1);
                    border-radius: 8px;
                }
            """)
            try:
                checkbox.setIcon(QIcon("x.svg"))
                checkbox.setIconSize(QSize(14, 14))
                colorize_effect = QGraphicsColorizeEffect()
                colorize_effect.setColor(QColor("#444444"))
                checkbox.setGraphicsEffect(colorize_effect)
            except:
                checkbox.setText("")
        else:  # future
            checkbox.setStyleSheet("""
                QPushButton {
                    background-color: rgba(255, 255, 255, 0.05);
                    border: 1px solid rgba(255, 255, 255, 0.1);
                    border-radius: 8px;
                }
            """)
        
        return checkbox
