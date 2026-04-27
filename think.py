from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, 
                             QPushButton, QFrame, QScrollArea, QTextEdit,
                             QGraphicsColorizeEffect)
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon


class ThinkPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet("background-color: transparent;")
        
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 16, 0, 16)
        layout.setSpacing(20)
        
        # Header
        header = self.create_header()
        layout.addWidget(header)
        
        # Filter chips
        filter_chips = self.create_filter_chips()
        layout.addWidget(filter_chips)
        
        # Thoughts list (scroll area)
        thoughts_scroll = self.create_thoughts_list()
        layout.addWidget(thoughts_scroll)
        
        # Floating composer
        composer = self.create_composer()
        layout.addWidget(composer)
    
    def create_header(self):
        header = QWidget()
        header.setStyleSheet("background-color: transparent;")
        
        layout = QHBoxLayout(header)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(12)
        
        # Left side: Title and subtitle
        left_layout = QVBoxLayout()
        left_layout.setSpacing(4)
        
        title = QLabel("Think")
        title.setStyleSheet("""
            QLabel {
                color: #ffffff;
                font-size: 24px;
                font-weight: bold;
                border: none;
                background: transparent;
            }
        """)
        
        subtitle = QLabel("6 thoughts")
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
        
        # Right side: Filter and Search icons
        right_layout = QHBoxLayout()
        right_layout.setSpacing(8)
        
        filter_btn = QPushButton()
        filter_btn.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        try:
            filter_btn.setIcon(QIcon("assets/filter.svg"))
            filter_btn.setIconSize(QSize(20, 20))
            colorize_effect = QGraphicsColorizeEffect()
            colorize_effect.setColor(Qt.GlobalColor.white)
            filter_btn.setGraphicsEffect(colorize_effect)
        except:
            filter_btn.setText("⚡")
        filter_btn.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                border: none;
                color: #ffffff;
            }
        """)
        filter_btn.setFixedSize(32, 32)
        
        search_btn = QPushButton()
        search_btn.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        try:
            search_btn.setIcon(QIcon("assets/search.svg"))
            search_btn.setIconSize(QSize(20, 20))
            colorize_effect = QGraphicsColorizeEffect()
            colorize_effect.setColor(Qt.GlobalColor.white)
            search_btn.setGraphicsEffect(colorize_effect)
        except:
            search_btn.setText("🔍")
        search_btn.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                border: none;
                color: #ffffff;
            }
        """)
        search_btn.setFixedSize(32, 32)
        
        right_layout.addWidget(filter_btn)
        right_layout.addWidget(search_btn)
        
        layout.addLayout(left_layout)
        layout.addStretch()
        layout.addLayout(right_layout)
        
        return header
    
    def create_filter_chips(self):
        chips_widget = QWidget()
        chips_widget.setStyleSheet("background-color: transparent;")
        
        layout = QHBoxLayout(chips_widget)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(8)
        
        chips = [
            ("All 6", True, "assets/list.svg"),
            ("Text 4", False, "assets/text.svg"),
            ("Images 1", False, "assets/image.svg"),
            ("Links 1", False, "assets/link.svg")
        ]
        
        for text, active, icon_path in chips:
            chip = QPushButton(text)
            chip.setFocusPolicy(Qt.FocusPolicy.NoFocus)
            if active:
                chip.setStyleSheet("""
                    QPushButton {
                        background-color: rgba(255, 255, 255, 0.15);
                        color: #ffffff;
                        border: 1px solid rgba(255, 255, 255, 0.1);
                        padding: 6px 16px;
                        border-radius: 16px;
                        font-size: 13px;
                    }
                """)
            else:
                chip.setStyleSheet("""
                    QPushButton {
                        background-color: rgba(255, 255, 255, 0.05);
                        color: #ffffff;
                        border: 1px solid rgba(255, 255, 255, 0.1);
                        padding: 6px 16px;
                        border-radius: 16px;
                        font-size: 13px;
                    }
                    QPushButton:hover {
                        background-color: rgba(255, 255, 255, 0.1);
                    }
                """)
            layout.addWidget(chip)
        
        layout.addStretch()
        
        return chips_widget
    
    def create_thoughts_list(self):
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
        
        # Container widget for scroll area
        container = QWidget()
        container.setStyleSheet("background-color: transparent;")
        
        container_layout = QVBoxLayout(container)
        container_layout.setContentsMargins(0, 0, 0, 0)
        container_layout.setSpacing(15)
        
        # Sample thoughts
        thoughts = [
            ("text", "Remember to review the pull request tomorrow morning", "Jan 31 8:00 PM"),
            ("text", "The new design system looks great but needs more spacing", "Jan 31 6:30 PM"),
            ("link", "https://github.com/hashir500/Mash-Dashboard", "Jan 31 4:15 PM"),
            ("text", "Need to add more glassmorphic effects to the UI", "Jan 31 2:00 PM"),
            ("text", "Meeting with the team at 3pm tomorrow", "Jan 31 11:00 AM"),
            ("text", "Don't forget to push the changes to GitHub", "Jan 30 9:00 PM")
        ]
        
        for thought_type, content, timestamp in thoughts:
            thought_item = self.create_thought_item(thought_type, content, timestamp)
            container_layout.addWidget(thought_item)
        
        container_layout.addStretch()
        
        scroll.setWidget(container)
        
        return scroll
    
    def create_thought_item(self, thought_type, content, timestamp):
        item = QFrame()
        item.setStyleSheet("""
            QFrame {
                background-color: rgba(255, 255, 255, 0.05);
                border: 1px solid rgba(255, 255, 255, 0.08);
                border-radius: 12px;
            }
        """)
        
        layout = QHBoxLayout(item)
        layout.setContentsMargins(16, 16, 16, 16)
        layout.setSpacing(16)
        
        # Bullet point circle
        bullet = QLabel()
        bullet.setFixedSize(8, 8)
        bullet.setStyleSheet("""
            QLabel {
                background-color: transparent;
                border: 2px solid #666666;
                border-radius: 4px;
            }
        """)
        
        # Content layout
        content_layout = QVBoxLayout()
        content_layout.setSpacing(8)
        
        # Main content
        if thought_type == "link":
            content_label = QLabel(content)
            content_label.setStyleSheet("""
                QLabel {
                    color: #5AC8FA;
                    font-size: 15px;
                    border: none;
                    background: transparent;
                }
            """)
        else:
            content_label = QLabel(content)
            content_label.setStyleSheet("""
                QLabel {
                    color: #ffffff;
                    font-size: 15px;
                    border: none;
                    background: transparent;
                }
            """)
        
        # Timestamp
        timestamp_label = QLabel(timestamp)
        timestamp_label.setStyleSheet("""
            QLabel {
                color: #888888;
                font-size: 12px;
                border: none;
                background: transparent;
            }
        """)
        
        content_layout.addWidget(content_label)
        content_layout.addWidget(timestamp_label)
        
        layout.addWidget(bullet)
        layout.addLayout(content_layout)
        layout.addStretch()
        
        return item
    
    def create_composer(self):
        composer = QFrame()
        composer.setFixedHeight(80)
        composer.setStyleSheet("""
            QFrame {
                background-color: rgba(255, 255, 255, 0.05);
                border: 1px solid rgba(255, 255, 255, 0.08);
                border-radius: 12px;
            }
        """)
        
        layout = QHBoxLayout(composer)
        layout.setContentsMargins(16, 12, 16, 12)
        layout.setSpacing(12)
        
        # Paperclip icon
        paperclip_btn = QPushButton()
        paperclip_btn.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        try:
            paperclip_btn.setIcon(QIcon("assets/paperclip.svg"))
            paperclip_btn.setIconSize(QSize(20, 20))
            colorize_effect = QGraphicsColorizeEffect()
            colorize_effect.setColor(Qt.GlobalColor.white)
            paperclip_btn.setGraphicsEffect(colorize_effect)
        except:
            paperclip_btn.setText("📎")
        paperclip_btn.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                border: none;
                color: #ffffff;
            }
        """)
        paperclip_btn.setFixedSize(32, 32)
        
        # Text edit
        text_edit = QTextEdit()
        text_edit.setPlaceholderText("What's on your mind?")
        text_edit.setMaximumHeight(80)
        text_edit.setStyleSheet("""
            QTextEdit {
                background-color: transparent;
                border: none;
                color: #ffffff;
                font-size: 14px;
                padding: 4px;
            }
            QTextEdit::placeholder {
                color: #666666;
            }
        """)
        
        # Helper text
        helper_text = QLabel("Enter · ⇧ Newline · ⌘V Image")
        helper_text.setStyleSheet("""
            QLabel {
                color: #666666;
                font-size: 11px;
                border: none;
                background: transparent;
            }
        """)
        
        layout.addWidget(paperclip_btn)
        layout.addWidget(text_edit)
        layout.addWidget(helper_text)
        
        return composer
