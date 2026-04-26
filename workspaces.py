from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, 
                             QPushButton, QFrame, QGridLayout, QGraphicsColorizeEffect)
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon


class WorkspacesPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet("background-color: transparent;")
        
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 16, 0, 16)
        layout.setSpacing(20)
        
        # Header
        header = self.create_header()
        layout.addWidget(header)
        
        # Category selector
        categories = self.create_category_selector()
        layout.addWidget(categories)
        
        # Active workspace details card
        details_card = self.create_details_card()
        layout.addWidget(details_card)
        
        # Items section
        items_section = self.create_items_section()
        layout.addWidget(items_section)
    
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
        
        title = QLabel("Workspaces")
        title.setStyleSheet("""
            QLabel {
                color: #ffffff;
                font-size: 28px;
                font-weight: bold;
                border: none;
                background: transparent;
            }
        """)
        
        subtitle = QLabel("Launch your apps, tabs & folders together")
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
        
        # Right side: New Workspace button
        new_btn = QPushButton("+ New Workspace")
        new_btn.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        new_btn.setStyleSheet("""
            QPushButton {
                background-color: #007AFF;
                color: #ffffff;
                border-radius: 8px;
                padding: 10px 20px;
                font-weight: bold;
                border: none;
            }
            QPushButton:hover {
                background-color: #0056CC;
            }
        """)
        
        layout.addLayout(left_layout)
        layout.addStretch()
        layout.addWidget(new_btn)
        
        return header
    
    def create_category_selector(self):
        container = QFrame()
        container.setFixedHeight(60)
        container.setStyleSheet("""
            QFrame {
                background-color: rgba(255, 255, 255, 0.05);
                border: 1px solid rgba(255, 255, 255, 0.08);
                border-radius: 12px;
            }
        """)
        
        layout = QHBoxLayout(container)
        layout.setContentsMargins(10, 0, 10, 0)
        layout.setSpacing(10)
        
        categories = [
            ("Coding", True, 5),
            ("Design", False, 3),
            ("Communication", False, 2),
            ("Research", False, 1)
        ]
        
        for name, active, count in categories:
            cat_btn = self.create_category_button(name, active, count)
            layout.addWidget(cat_btn)
        
        layout.addStretch()
        
        return container
    
    def create_category_button(self, name, active, count):
        btn = QPushButton(f"  {name} {count}")
        btn.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        
        # Map category names to icon files
        icon_map = {
            "Coding": "coding.svg",
            "Design": "design.svg",
            "Communication": "communication.svg",
            "Research": "research.svg"
        }
        
        # Add colorful icon without white colorization
        if name in icon_map:
            try:
                btn.setIcon(QIcon(icon_map[name]))
                btn.setIconSize(QSize(18, 18))
            except:
                pass
        
        if active:
            btn.setStyleSheet("""
                QPushButton {
                    background-color: rgba(0, 122, 255, 0.2);
                    color: #ffffff;
                    border: 1px solid rgba(0, 122, 255, 0.5);
                    border-radius: 16px;
                    padding: 6px 16px;
                    font-size: 14px;
                }
            """)
        else:
            btn.setStyleSheet("""
                QPushButton {
                    background-color: rgba(255, 255, 255, 0.05);
                    color: #ffffff;
                    border: 1px solid rgba(255, 255, 255, 0.1);
                    border-radius: 16px;
                    padding: 6px 16px;
                    font-size: 14px;
                }
                QPushButton:hover {
                    background-color: rgba(255, 255, 255, 0.1);
                }
            """)
        
        return btn
    
    def create_details_card(self):
        card = QFrame()
        card.setFixedHeight(130)
        card.setStyleSheet("""
            QFrame {
                background-color: rgba(255, 255, 255, 0.05);
                border: 1px solid rgba(255, 255, 255, 0.08);
                border-radius: 12px;
            }
        """)
        
        layout = QVBoxLayout(card)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(10)
        
        # Top row: Title, badge, and action buttons
        top_row = QHBoxLayout()
        top_row.setSpacing(12)
        
        title = QLabel("Coding")
        title.setStyleSheet("""
            QLabel {
                color: #ffffff;
                font-size: 20px;
                font-weight: bold;
                border: none;
                background: transparent;
            }
        """)
        
        badge = QLabel("Used 2h ago")
        badge.setFixedHeight(24)
        badge.setStyleSheet("""
            QLabel {
                background-color: rgba(255, 255, 255, 0.1);
                border-radius: 12px;
                padding: 0px 10px;
                font-size: 11px;
                color: #AAAAAA;
                border: none;
            }
        """)
        
        top_row.addWidget(title)
        top_row.addWidget(badge)
        top_row.addStretch()
        
        # Action buttons
        edit_btn = QPushButton()
        edit_btn.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        try:
            edit_btn.setIcon(QIcon("edit.svg"))
            edit_btn.setIconSize(QSize(16, 16))
            colorize_effect = QGraphicsColorizeEffect()
            colorize_effect.setColor(Qt.GlobalColor.white)
            edit_btn.setGraphicsEffect(colorize_effect)
        except:
            edit_btn.setText("✎")
        edit_btn.setStyleSheet("""
            QPushButton {
                background-color: rgba(255, 255, 255, 0.1);
                border: none;
                border-radius: 8px;
                padding: 8px;
            }
            QPushButton:hover {
                background-color: rgba(255, 255, 255, 0.15);
            }
        """)
        edit_btn.setFixedSize(36, 36)
        
        delete_btn = QPushButton()
        delete_btn.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        try:
            delete_btn.setIcon(QIcon("trash.svg"))
            delete_btn.setIconSize(QSize(16, 16))
            colorize_effect = QGraphicsColorizeEffect()
            colorize_effect.setColor(Qt.GlobalColor.white)
            delete_btn.setGraphicsEffect(colorize_effect)
        except:
            delete_btn.setText("🗑")
        delete_btn.setStyleSheet("""
            QPushButton {
                background-color: rgba(255, 59, 48, 0.2);
                border: none;
                border-radius: 8px;
                padding: 8px;
            }
            QPushButton:hover {
                background-color: rgba(255, 59, 48, 0.3);
            }
        """)
        delete_btn.setFixedSize(36, 36)
        
        launch_btn = QPushButton("▶ Launch")
        launch_btn.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        launch_btn.setStyleSheet("""
            QPushButton {
                background-color: #007AFF;
                color: #ffffff;
                border: none;
                border-radius: 8px;
                padding: 10px 20px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #0056CC;
            }
        """)
        
        top_row.addWidget(edit_btn)
        top_row.addWidget(delete_btn)
        top_row.addWidget(launch_btn)
        
        # Bottom row: Description
        subtitle = QLabel("Full dev environment with editor, terminal, and docs")
        subtitle.setStyleSheet("""
            QLabel {
                color: #888888;
                font-size: 14px;
                border: none;
                background: transparent;
            }
        """)
        
        layout.addLayout(top_row)
        layout.addWidget(subtitle)
        
        return card
    
    def create_items_section(self):
        section = QWidget()
        section.setStyleSheet("background-color: transparent;")
        
        layout = QVBoxLayout(section)
        layout.setSpacing(12)
        
        # Section header
        header = QLabel("ITEMS (5)")
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
        
        # Items grid
        grid = QGridLayout()
        grid.setSpacing(12)
        
        # Sample items
        items = [
            ("VS Code", "Code Editor", "APP"),
            ("Terminal", "Shell", "APP"),
            ("Chrome", "Browser", "APP"),
            ("GitHub", "Repository", "URL"),
            ("Docs", "Documentation", "FOLDER")
        ]
        
        for i, (title, subtitle, badge_text) in enumerate(items):
            item_card = self.create_item_card(title, subtitle, badge_text)
            row = i // 3
            col = i % 3
            grid.addWidget(item_card, row, col)
        
        # Add item card
        add_card = self.create_add_item_card()
        grid.addWidget(add_card, 1, 2)
        
        layout.addLayout(grid)
        
        return section
    
    def create_item_card(self, title, subtitle, badge_text):
        card = QFrame()
        card.setStyleSheet("""
            QFrame {
                background-color: rgba(255, 255, 255, 0.05);
                border: 1px solid rgba(255, 255, 255, 0.08);
                border-radius: 12px;
            }
        """)
        
        layout = QHBoxLayout(card)
        layout.setContentsMargins(12, 12, 12, 12)
        layout.setSpacing(12)
        
        # Icon wrapper
        icon_wrapper = QFrame()
        icon_wrapper.setFixedSize(40, 40)
        icon_wrapper.setStyleSheet("""
            QFrame {
                background-color: rgba(255, 255, 255, 0.1);
                border-radius: 8px;
            }
        """)
        
        icon_layout = QVBoxLayout(icon_wrapper)
        icon_layout.setContentsMargins(0, 0, 0, 0)
        icon_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        icon_label = QLabel()
        icon_label.setStyleSheet("border: none; background: transparent;")
        try:
            icon_label.setPixmap(QIcon("file.svg").pixmap(20, 20))
            colorize_effect = QGraphicsColorizeEffect()
            colorize_effect.setColor(Qt.GlobalColor.white)
            icon_label.setGraphicsEffect(colorize_effect)
        except:
            icon_label.setText("📄")
        
        icon_layout.addWidget(icon_label)
        
        # Content
        content_layout = QVBoxLayout()
        content_layout.setSpacing(4)
        
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
        
        subtitle_label = QLabel(subtitle)
        subtitle_label.setStyleSheet("""
            QLabel {
                color: #888888;
                font-size: 12px;
                border: none;
                background: transparent;
            }
        """)
        
        content_layout.addWidget(title_label)
        content_layout.addWidget(subtitle_label)
        
        # Right side: badge and close button
        right_layout = QHBoxLayout()
        right_layout.setSpacing(8)
        
        badge = QLabel(badge_text)
        badge.setStyleSheet("""
            QLabel {
                background-color: rgba(255, 255, 255, 0.1);
                color: #888888;
                padding: 2px 8px;
                border-radius: 6px;
                font-size: 10px;
                border: none;
            }
        """)
        
        close_btn = QPushButton("×")
        close_btn.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                color: #888888;
                border: none;
                font-size: 16px;
                padding: 0px;
            }
            QPushButton:hover {
                color: #ffffff;
            }
        """)
        close_btn.setFixedSize(20, 20)
        
        right_layout.addWidget(badge)
        right_layout.addWidget(close_btn)
        
        layout.addWidget(icon_wrapper)
        layout.addLayout(content_layout)
        layout.addStretch()
        layout.addLayout(right_layout)
        
        return card
    
    def create_add_item_card(self):
        card = QFrame()
        card.setStyleSheet("""
            QFrame {
                background-color: transparent;
                border: 1px dashed rgba(255, 255, 255, 0.2);
                border-radius: 12px;
            }
        """)
        
        layout = QVBoxLayout(card)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        add_label = QLabel("+ Add Item")
        add_label.setStyleSheet("""
            QLabel {
                color: #007AFF;
                font-size: 14px;
                font-weight: 500;
                border: none;
                background: transparent;
            }
        """)
        
        layout.addWidget(add_label)
        
        return card
