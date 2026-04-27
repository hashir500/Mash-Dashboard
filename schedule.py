from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, 
                             QPushButton, QFrame, QScrollArea, QGraphicsColorizeEffect,
                             QStackedLayout)
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon


class SchedulePage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet("background-color: transparent;")
        
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 16, 0, 16)
        layout.setSpacing(20)
        
        # Header
        header = self.create_header()
        layout.addWidget(header)
        
        # Timeline bar
        timeline = self.create_timeline()
        layout.addWidget(timeline)
        
        # Task list (scroll area)
        task_scroll = self.create_task_list()
        layout.addWidget(task_scroll)
        
        # FAB (Floating Action Button)
        self.fab = self.create_fab()
        self.fab.setParent(self)
        self.fab.move(self.width() - 80, self.height() - 120)
        self.fab.show()
    
    def resizeEvent(self, event):
        # Update FAB position on resize
        self.fab.move(self.width() - 80, self.height() - 120)
        super().resizeEvent(event)
    
    def create_header(self):
        header = QWidget()
        header.setStyleSheet("background-color: transparent;")
        
        layout = QHBoxLayout(header)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(20)
        
        # Left side: Date navigation
        left_layout = QHBoxLayout()
        left_layout.setSpacing(12)
        
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
                background-color: transparent;
                border: none;
                color: #ffffff;
                font-size: 20px;
            }
        """)
        left_arrow.setFixedSize(24, 24)
        
        # Date display
        date_layout = QVBoxLayout()
        date_layout.setSpacing(4)
        
        day_label = QLabel("Thursday")
        day_label.setStyleSheet("""
            QLabel {
                color: #ffffff;
                font-size: 24px;
                font-weight: bold;
                border: none;
                background: transparent;
            }
        """)
        
        date_label = QLabel("Feb 5 <span style='color: #238636;'>Today</span>")
        date_label.setStyleSheet("""
            QLabel {
                color: #888888;
                font-size: 14px;
                border: none;
                background: transparent;
            }
        """)
        
        date_layout.addWidget(day_label)
        date_layout.addWidget(date_label)
        
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
                background-color: transparent;
                border: none;
                color: #ffffff;
                font-size: 20px;
            }
        """)
        right_arrow.setFixedSize(24, 24)
        
        left_layout.addWidget(left_arrow)
        left_layout.addLayout(date_layout)
        left_layout.addWidget(right_arrow)
        
        # Right side: View toggle
        view_toggle = self.create_view_toggle()
        
        layout.addLayout(left_layout)
        layout.addStretch()
        layout.addWidget(view_toggle)
        
        return header
    
    def create_view_toggle(self):
        toggle = QFrame()
        toggle.setStyleSheet("""
            QFrame {
                background-color: rgba(255, 255, 255, 0.05);
                border: 1px solid rgba(255, 255, 255, 0.1);
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
    
    def create_timeline(self):
        timeline = QFrame()
        timeline.setStyleSheet("""
            QFrame {
                background-color: rgba(255, 255, 255, 0.05);
                border: 1px solid rgba(255, 255, 255, 0.1);
                border-radius: 12px;
            }
        """)
        
        layout = QVBoxLayout(timeline)
        layout.setContentsMargins(16, 12, 16, 12)
        layout.setSpacing(8)
        
        # Top row: Timeline label and scheduled time
        top_row = QHBoxLayout()
        top_row.setContentsMargins(0, 0, 0, 0)
        
        timeline_label = QLabel("Timeline")
        timeline_label.setStyleSheet("""
            QLabel {
                color: #888888;
                font-size: 12px;
                border: none;
                background: transparent;
            }
        """)
        
        scheduled_label = QLabel("5h scheduled")
        scheduled_label.setStyleSheet("""
            QLabel {
                color: #888888;
                font-size: 12px;
                border: none;
                background: transparent;
            }
        """)
        
        top_row.addWidget(timeline_label)
        top_row.addStretch()
        top_row.addWidget(scheduled_label)
        
        # Bottom row: Track with colored blocks
        track = QFrame()
        track.setFixedHeight(30)
        track.setStyleSheet("""
            QFrame {
                background-color: rgba(30, 30, 30, 0.6);
                border-radius: 15px;
            }
        """)
        
        track_layout = QHBoxLayout(track)
        track_layout.setContentsMargins(0, 0, 0, 0)
        track_layout.setSpacing(0)
        
        # Purple block
        purple_block = QFrame()
        purple_block.setMinimumWidth(150)
        purple_block.setStyleSheet("""
            QFrame {
                background-color: rgba(175, 82, 222, 0.6);
                border: none;
                border-radius: 15px;
            }
        """)
        track_layout.addWidget(purple_block)
        
        # Spacer
        track_layout.addSpacing(50)
        
        # Brown block
        brown_block = QFrame()
        brown_block.setMinimumWidth(100)
        brown_block.setStyleSheet("""
            QFrame {
                background-color: rgba(162, 132, 94, 0.6);
                border: none;
                border-radius: 15px;
            }
        """)
        track_layout.addWidget(brown_block)
        
        track_layout.addStretch()
        
        # Current time indicator
        current_time = QFrame()
        current_time.setFixedSize(2, 30)
        current_time.setStyleSheet("""
            QFrame {
                background-color: #FF3B30;
                border-radius: 1px;
            }
        """)
        current_time.setParent(track)
        current_time.move(100, 0)
        current_time.raise_()
        
        layout.addLayout(top_row)
        layout.addWidget(track)
        
        return timeline
    
    def create_task_list(self):
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
        
        # Container widget
        container = QWidget()
        container.setStyleSheet("background-color: transparent;")
        
        container_layout = QVBoxLayout(container)
        container_layout.setContentsMargins(0, 0, 0, 0)
        container_layout.setSpacing(12)
        
        # Sample tasks
        tasks = [
            ("9:00", "12:00", "Build calendar UI", "Coding · 3h", "#AF52DE"),
            ("13:00", "14:30", "Review PRs", "Review · 1.5h", "#FF3B30"),
            ("15:00", "16:00", "Team meeting", "Meeting · 1h", "#FF9500"),
            ("16:30", "18:00", "Documentation", "Writing · 1.5h", "#34C759")
        ]
        
        for start_time, end_time, title, meta, color in tasks:
            task_item = self.create_task_item(start_time, end_time, title, meta, color)
            container_layout.addWidget(task_item)
        
        container_layout.addStretch()
        
        scroll.setWidget(container)
        
        return scroll
    
    def create_task_item(self, start_time, end_time, title, meta, color):
        item = QFrame()
        item.setStyleSheet("""
            QFrame {
                background-color: rgba(255, 255, 255, 0.05);
                border: 1px solid rgba(255, 255, 255, 0.1);
                border-radius: 12px;
            }
        """)
        
        layout = QHBoxLayout(item)
        layout.setContentsMargins(16, 16, 16, 16)
        layout.setSpacing(16)
        
        # Time column
        time_layout = QVBoxLayout()
        time_layout.setSpacing(4)
        time_layout.setContentsMargins(0, 0, 0, 0)
        
        start_label = QLabel(start_time)
        start_label.setStyleSheet("""
            QLabel {
                color: #ffffff;
                font-size: 16px;
                font-weight: bold;
                border: none;
                background: transparent;
            }
        """)
        
        end_label = QLabel(end_time)
        end_label.setStyleSheet("""
            QLabel {
                color: #888888;
                font-size: 13px;
                border: none;
                background: transparent;
            }
        """)
        
        time_layout.addWidget(start_label)
        time_layout.addWidget(end_label)
        
        # Category line
        category_line = QFrame()
        category_line.setFixedWidth(3)
        category_line.setStyleSheet(f"""
            QFrame {{
                background-color: {color};
                border-radius: 1px;
            }}
        """)
        
        # Content column
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
        
        meta_label = QLabel(meta)
        meta_label.setStyleSheet(f"""
            QLabel {{
                color: {color};
                font-size: 13px;
                border: none;
                background: transparent;
            }}
        """)
        
        content_layout.addWidget(title_label)
        content_layout.addWidget(meta_label)
        
        # Status checkmark
        checkmark = QLabel()
        try:
            checkmark.setPixmap(QIcon("check.svg").pixmap(20, 20))
            colorize_effect = QGraphicsColorizeEffect()
            colorize_effect.setColor(Qt.GlobalColor.white)
            checkmark.setGraphicsEffect(colorize_effect)
        except:
            checkmark.setText("✓")
        checkmark.setStyleSheet("""
            QLabel {
                color: #444444;
                font-size: 18px;
                border: none;
                background: transparent;
            }
        """)
        
        layout.addLayout(time_layout)
        layout.addWidget(category_line)
        layout.addLayout(content_layout)
        layout.addStretch()
        layout.addWidget(checkmark)
        
        return item
    
    def create_fab(self):
        fab = QPushButton()
        fab.setFixedSize(60, 60)
        fab.setText("+")
        fab.setFocusPolicy(Qt.FocusPolicy.NoFocus)  # Prevent focus taking
        fab.setStyleSheet("""
            QPushButton {
                background-color: #3399FF;
                color: white;
                border-radius: 30px;
                font-size: 32px;
                font-weight: normal;
                border: none;
                padding-bottom: 4px;
            }
            QPushButton:hover {
                background-color: #4DB8FF;
            }
        """)
        
        return fab
