from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, 
                             QPushButton, QFrame, QScrollArea, QGraphicsColorizeEffect,
                             QStackedLayout)
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon


class SchedulePage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet("""
            QWidget {
                background-color: transparent;
                color: #1f2a3d;
            }
        """)
        
        layout = QVBoxLayout(self)
        layout.setContentsMargins(10, 8, 10, 10)
        layout.setSpacing(10)
        
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
        layout.setSpacing(10)
        
        # Left side: Date navigation
        left_layout = QHBoxLayout()
        left_layout.setSpacing(8)
        
        # Left arrow
        left_arrow = QPushButton()
        left_arrow.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        try:
            left_arrow.setIcon(QIcon("assets/chevron-left.svg"))
            left_arrow.setIconSize(QSize(20, 20))
            colorize_effect = QGraphicsColorizeEffect()
            colorize_effect.setColor(Qt.GlobalColor.black)
            left_arrow.setGraphicsEffect(colorize_effect)
        except:
            left_arrow.setText("<")
        left_arrow.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                border: none;
                color: #2f3b52;
                font-size: 16px;
            }
        """)
        left_arrow.setFixedSize(20, 20)
        
        # Date display
        date_layout = QVBoxLayout()
        date_layout.setSpacing(4)
        
        day_label = QLabel("Today - Wed, May 6")
        day_label.setStyleSheet("""
            QLabel {
                color: #2f3b52;
                font-size: 18px;
                font-weight: 700;
                border: none;
                background: transparent;
            }
        """)
        
        date_label = QLabel("6 blocks · 4h 45m planned")
        date_label.setStyleSheet("""
            QLabel {
                color: #8590a3;
                font-size: 12px;
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
            right_arrow.setIcon(QIcon("assets/chevron-right.svg"))
            right_arrow.setIconSize(QSize(20, 20))
            colorize_effect = QGraphicsColorizeEffect()
            colorize_effect.setColor(Qt.GlobalColor.black)
            right_arrow.setGraphicsEffect(colorize_effect)
        except:
            right_arrow.setText(">")
        right_arrow.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                border: none;
                color: #2f3b52;
                font-size: 16px;
            }
        """)
        right_arrow.setFixedSize(20, 20)
        
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
                background-color: rgba(255, 255, 255, 0.78);
                border: 1px solid #dbe2ee;
                border-radius: 10px;
            }
        """)
        
        layout = QHBoxLayout(toggle)
        layout.setContentsMargins(3, 3, 3, 3)
        layout.setSpacing(0)
        
        # Day button (active)
        day_btn = QPushButton("Day")
        day_btn.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        day_btn.setStyleSheet("""
            QPushButton {
                background-color: #ffffff;
                color: #334058;
                border: none;
                border-radius: 7px;
                padding: 5px 13px;
                font-size: 12px;
                font-weight: 500;
            }
        """)
        
        # Week button (inactive)
        week_btn = QPushButton("Week")
        week_btn.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        week_btn.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                color: #7e889b;
                border: none;
                border-radius: 7px;
                padding: 5px 13px;
                font-size: 12px;
                font-weight: 500;
            }
            QPushButton:hover {
                color: #445066;
            }
        """)
        
        layout.addWidget(day_btn)
        layout.addWidget(week_btn)
        
        return toggle
    
    def create_timeline(self):
        timeline = QFrame()
        timeline.setStyleSheet("""
            QFrame {
                background-color: rgba(255, 255, 255, 0.84);
                border: 1px solid #e1e6f0;
                border-radius: 10px;
            }
        """)
        
        layout = QVBoxLayout(timeline)
        layout.setContentsMargins(12, 10, 12, 10)
        layout.setSpacing(6)
        
        # Top row: Timeline label and scheduled time
        top_row = QHBoxLayout()
        top_row.setContentsMargins(0, 0, 0, 0)
        
        timeline_label = QLabel("Timeline")
        timeline_label.setStyleSheet("""
            QLabel {
                color: #8a95a8;
                font-size: 12px;
                border: none;
                background: transparent;
            }
        """)
        
        scheduled_label = QLabel("5h scheduled")
        scheduled_label.setStyleSheet("""
            QLabel {
                color: #8a95a8;
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
        track.setFixedHeight(24)
        track.setStyleSheet("""
            QFrame {
                background-color: rgba(245, 248, 253, 0.9);
                border-radius: 12px;
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
                border-radius: 10px;
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
                border-radius: 10px;
            }
        """)
        track_layout.addWidget(brown_block)
        
        track_layout.addStretch()
        
        # Current time indicator
        current_time = QFrame()
        current_time.setFixedSize(2, 24)
        current_time.setStyleSheet("""
            QFrame {
                background-color: #f44e4e;
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
                background-color: rgba(113, 126, 149, 0.28);
                border-radius: 3px;
                min-height: 20px;
            }
            QScrollBar::handle:vertical:hover {
                background-color: rgba(113, 126, 149, 0.4);
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
        container_layout.setSpacing(8)
        
        # Sample tasks
        tasks = [
            ("", "", "Landing Page", "Drag to schedule", "#9aa5b9"),
            ("", "", "CLOUD AI working", "Drag to schedule", "#9aa5b9"),
            ("", "", "UI fixes", "Drag to schedule", "#9aa5b9"),
            ("", "", "dont get plan your day unless check youtube etc??", "Drag to schedule", "#9aa5b9")
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
                background-color: rgba(255, 255, 255, 0.82);
                border: 1px solid #e1e6f0;
                border-radius: 10px;
            }
        """)
        
        layout = QHBoxLayout(item)
        layout.setContentsMargins(12, 10, 12, 10)
        layout.setSpacing(10)
        
        # Time column
        time_layout = QVBoxLayout()
        time_layout.setSpacing(4)
        time_layout.setContentsMargins(0, 0, 0, 0)
        
        start_label = QLabel(start_time)
        start_label.setStyleSheet("""
            QLabel {
                color: #6d7890;
                font-size: 16px;
                font-weight: bold;
                border: none;
                background: transparent;
            }
        """)
        
        end_label = QLabel(end_time)
        end_label.setStyleSheet("""
            QLabel {
                color: #a0aabc;
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
                color: #334057;
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
            checkmark.setPixmap(QIcon("assets/check.svg").pixmap(20, 20))
            colorize_effect = QGraphicsColorizeEffect()
            colorize_effect.setColor(Qt.GlobalColor.black)
            checkmark.setGraphicsEffect(colorize_effect)
        except:
            checkmark.setText("✓")
        checkmark.setStyleSheet("""
            QLabel {
                color: #909aab;
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
                background-color: #ffffff;
                border: 1px solid #dfe5ef;
                color: white;
                border-radius: 30px;
                font-size: 32px;
                font-weight: normal;
                color: #6e7b93;
                padding-bottom: 4px;
            }
            QPushButton:hover {
                background-color: #f3f6fb;
            }
        """)
        
        return fab
