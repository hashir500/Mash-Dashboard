from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, 
                             QPushButton, QFrame, QLineEdit, QRadioButton,
                             QGraphicsColorizeEffect)
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon


class TabNavigation(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet("background-color: transparent;")
        
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(8)
        
        # Segmented control
        tab_container = QFrame()
        tab_container.setStyleSheet("""
            QFrame {
                background-color: rgba(255, 255, 255, 0.78);
                border: 1px solid #dde3ee;
                border-radius: 10px;
            }
        """)
        
        tab_layout = QHBoxLayout(tab_container)
        tab_layout.setContentsMargins(3, 3, 3, 3)
        tab_layout.setSpacing(4)
        
        # Tab buttons
        tabs = [
            ("Open", True),
            ("Done", False),
            ("Trash", False),
            ("Workspace", False),
            ("All", False),
            ("Today", False)
        ]
        
        for tab_name, active in tabs:
            btn = QPushButton(tab_name)
            btn.setFocusPolicy(Qt.FocusPolicy.NoFocus)
            if active:
                btn.setStyleSheet("""
                    QPushButton {
                        background-color: #ffffff;
                        color: #344159;
                        border: none;
                        padding: 6px 10px;
                        border-radius: 8px;
                        font-size: 12px;
                        font-weight: 600;
                    }
                """)
            else:
                btn.setStyleSheet("""
                    QPushButton {
                        background-color: transparent;
                        color: #7d8799;
                        border: none;
                        padding: 6px 10px;
                        border-radius: 8px;
                        font-size: 12px;
                        font-weight: 500;
                    }
                    QPushButton:hover {
                        color: #3f4a60;
                        background-color: #eef2f9;
                    }
                """)
            tab_layout.addWidget(btn)
        
        layout.addStretch()
        layout.addWidget(tab_container)
        layout.addStretch()


class TaskInput(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet("background-color: transparent;")
        
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(12)
        
        # Glassmorphic container
        container = QFrame()
        container.setStyleSheet("""
            QFrame {
                background-color: rgba(255, 255, 255, 0.84);
                border: 1px solid #dde3ee;
                border-radius: 10px;
            }
        """)
        
        container_layout = QHBoxLayout(container)
        container_layout.setContentsMargins(12, 10, 12, 10)
        container_layout.setSpacing(12)
        
        # Plus icon
        plus_btn = QPushButton()
        plus_btn.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        try:
            plus_btn.setIcon(QIcon("assets/plus.svg"))
            plus_btn.setIconSize(QSize(20, 20))
            colorize_effect = QGraphicsColorizeEffect()
            colorize_effect.setColor(Qt.GlobalColor.black)
            plus_btn.setGraphicsEffect(colorize_effect)
        except:
            plus_btn.setText("+")
        plus_btn.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                border: none;
                color: #3d4961;
                font-size: 20px;
            }
        """)
        plus_btn.setFixedSize(32, 32)
        
        # Input field
        input_field = QLineEdit()
        input_field.setPlaceholderText("Add a task...")
        input_field.setStyleSheet("""
            QLineEdit {
                background-color: transparent;
                border: none;
                color: #39455d;
                font-size: 14px;
                padding: 4px;
            }
            QLineEdit::placeholder {
                color: #95a0b3;
            }
        """)
        
        container_layout.addWidget(plus_btn)
        container_layout.addWidget(input_field)
        
        layout.addWidget(container)


class TaskItem(QWidget):
    def __init__(self, title, parent=None):
        super().__init__(parent)
        self.setStyleSheet("background-color: transparent;")
        
        # Glassmorphic wrapper
        wrapper = QFrame()
        wrapper.setStyleSheet("""
            QFrame {
                background-color: rgba(255, 255, 255, 0.84);
                border: 1px solid #e0e6f0;
                border-radius: 10px;
            }
        """)
        wrapper.setStyleSheet(wrapper.styleSheet() + """
            QFrame:hover {
                background-color: #f9fbff;
            }
        """)
        
        wrapper_layout = QHBoxLayout(wrapper)
        wrapper_layout.setContentsMargins(12, 10, 12, 10)
        wrapper_layout.setSpacing(12)
        
        # Radio button for completion
        radio = QRadioButton()
        radio.setStyleSheet("""
            QRadioButton {
                background-color: transparent;
                border: 2px solid #c8d0de;
                border-radius: 10px;
                width: 20px;
                height: 20px;
            }
            QRadioButton::indicator {
                width: 20px;
                height: 20px;
                border-radius: 10px;
                background-color: transparent;
                border: 2px solid #c8d0de;
            }
            QRadioButton::indicator:checked {
                background-color: #5f7cff;
                border: 2px solid #5f7cff;
            }
        """)
        radio.setFixedSize(20, 20)
        
        # Content layout
        content_layout = QVBoxLayout()
        content_layout.setSpacing(8)
        
        # Task title
        title_label = QLabel(title)
        title_label.setStyleSheet("""
            QLabel {
                color: #2f3a50;
                font-size: 16px;
                font-weight: 500;
                border: none;
                background: transparent;
            }
        """)
        
        # Metadata pills
        pills_layout = QHBoxLayout()
        pills_layout.setSpacing(8)
        
        # Time pill
        time_pill = self.create_pill("30m worked", "rgba(64, 169, 255, 0.2)")
        pills_layout.addWidget(time_pill)
        
        # Stats pill
        stats_pill = self.create_pill("$ ○ 1/2 ⋯", "rgba(255, 255, 255, 0.1)")
        pills_layout.addWidget(stats_pill)
        
        # Deadline pill
        deadline_pill = self.create_pill("Tomorrow", "rgba(255, 159, 10, 0.2)")
        pills_layout.addWidget(deadline_pill)
        
        # Tag pill
        tag_pill = self.create_pill("< > Coding", "rgba(48, 209, 88, 0.2)")
        pills_layout.addWidget(tag_pill)
        
        content_layout.addWidget(title_label)
        content_layout.addLayout(pills_layout)
        
        # Edit icon (hidden by default, shown on hover)
        edit_btn = QPushButton()
        edit_btn.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        try:
            edit_btn.setIcon(QIcon("assets/edit.svg"))
            edit_btn.setIconSize(QSize(16, 16))
            colorize_effect = QGraphicsColorizeEffect()
            colorize_effect.setColor(Qt.GlobalColor.black)
            edit_btn.setGraphicsEffect(colorize_effect)
        except:
            edit_btn.setText("✎")
        edit_btn.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                border: none;
                color: #4f5c74;
                font-size: 16px;
            }
        """)
        edit_btn.setFixedSize(24, 24)
        edit_btn.hide()
        
        wrapper_layout.addWidget(radio)
        wrapper_layout.addLayout(content_layout)
        wrapper_layout.addStretch()
        wrapper_layout.addWidget(edit_btn)
        
        # Main layout
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.addWidget(wrapper)
        
        # Show edit button on hover
        wrapper.enterEvent = lambda e: edit_btn.show()
        wrapper.leaveEvent = lambda e: edit_btn.hide()
    
    def create_pill(self, text, bg_color):
        pill = QLabel(text)
        pill.setStyleSheet(f"""
            QLabel {{
                background-color: {bg_color};
                color: #2f3a50;
                padding: 4px 10px;
                border-radius: 12px;
                font-size: 12px;
                border: 1px solid rgba(120, 133, 158, 0.15);
            }}
        """)
        return pill


class TasksPage(QWidget):
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
        layout.setSpacing(12)
        
        # Tasks header
        tasks_header = QLabel("Tasks")
        tasks_header.setStyleSheet("""
            QLabel {
                color: #2d394f;
                font-size: 23px;
                font-weight: 700;
                border: none;
                background: transparent;
            }
        """)
        layout.addWidget(tasks_header)
        
        # Tab navigation
        tab_nav = TabNavigation()
        layout.addWidget(tab_nav)
        
        # TO DO count
        todo_count = QLabel("RECENTLY ACTIVE")
        todo_count.setStyleSheet("""
            QLabel {
                color: #7e8799;
                font-size: 12px;
                font-weight: 500;
                border: none;
                background: transparent;
            }
        """)
        layout.addWidget(todo_count)
        
        # Task input
        task_input = TaskInput()
        layout.addWidget(task_input)
        
        # Task list
        task_list = QVBoxLayout()
        task_list.setSpacing(8)
        
        # Sample tasks
        tasks = [
            "Review pull request #142",
            "Fix authentication bug",
            "Update documentation",
            "Prepare for demo"
        ]
        
        for task in tasks:
            task_item = TaskItem(task)
            task_list.addWidget(task_item)
        
        layout.addLayout(task_list)
        layout.addStretch()
