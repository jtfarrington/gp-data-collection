"""
Location Popup - Field overlay for selecting event coordinates
"""

from PySide6.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QPushButton, QLabel
from PySide6.QtGui import QPixmap, QPainter, QPen, QBrush, QColor
from PySide6.QtCore import Qt, QPoint


class ClickableLabel(QLabel):
    """QLabel that captures mouse clicks"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.click_position = None
        self.parent_dialog = parent
    
    def mousePressEvent(self, event):
        """Capture mouse click position"""
        if event.button() == Qt.LeftButton:
            self.click_position = event.pos()
            if self.parent_dialog:
                self.parent_dialog.handle_field_click(self.click_position)


class LocationPopup(QDialog):
    """
    Popup dialog for selecting event location on field.
    
    Coordinate System:
    - (0, 0) = Bottom-left corner
    - (100, 100) = Top-right corner
    - X-axis: 0 (left) to 100 (right)
    - Y-axis: 0 (bottom) to 100 (top)
    """
    
    def __init__(self, field_image_path, current_x=None, current_y=None, 
                 left_team_name="Left Team", right_team_name="Right Team", parent=None):
        """
        Initialize the location popup.
        
        Args:
            field_image_path: Path to field image
            current_x: Current X coordinate (0-100), if set
            current_y: Current Y coordinate (0-100), if set
            left_team_name: Name of team on left side
            right_team_name: Name of team on right side
            parent: Parent widget
        """
        super().__init__(parent)
        
        self.field_image_path = field_image_path
        self.current_x = current_x
        self.current_y = current_y
        self.left_team_name = left_team_name
        self.right_team_name = right_team_name
        
        self.selected_x = current_x
        self.selected_y = current_y
        
        self.field_width = 800  # Display width
        self.field_height = 533  # Display height (maintains aspect ratio)
        
        self.setup_ui()
    
    def setup_ui(self):
        """Setup the UI elements"""
        self.setWindowTitle("Select Event Location")
        self.setModal(True)
        self.setFixedSize(850, 700)
        
        # Main layout
        layout = QVBoxLayout()
        
        # Team labels
        team_layout = QHBoxLayout()
        
        left_label = QLabel(f"← {self.left_team_name}")
        left_label.setStyleSheet("font-size: 16px; font-weight: bold; color: #333;")
        left_label.setAlignment(Qt.AlignLeft)
        
        right_label = QLabel(f"{self.right_team_name} →")
        right_label.setStyleSheet("font-size: 16px; font-weight: bold; color: #333;")
        right_label.setAlignment(Qt.AlignRight)
        
        team_layout.addWidget(left_label)
        team_layout.addStretch()
        team_layout.addWidget(right_label)
        
        layout.addLayout(team_layout)
        
        # Field image with clickable overlay
        self.field_label = ClickableLabel(self)
        self.load_and_display_field()
        layout.addWidget(self.field_label, alignment=Qt.AlignCenter)
        
        # Coordinate display
        self.coord_label = QLabel()
        self.coord_label.setStyleSheet("font-size: 14px; padding: 10px;")
        self.update_coordinate_display()
        layout.addWidget(self.coord_label, alignment=Qt.AlignCenter)
        
        # Buttons
        button_layout = QHBoxLayout()
        
        cancel_btn = QPushButton("Cancel")
        cancel_btn.setFixedSize(120, 40)
        cancel_btn.setStyleSheet("""
            QPushButton {
                background-color: #ffebee;
                border: 2px solid #dcdcdc;
                border-radius: 5px;
                font-size: 14px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #ffcdd2;
            }
        """)
        cancel_btn.clicked.connect(self.reject)
        
        confirm_btn = QPushButton("Confirm Location")
        confirm_btn.setFixedSize(160, 40)
        confirm_btn.setStyleSheet("""
            QPushButton {
                background-color: #c8e6c9;
                border: 2px solid #dcdcdc;
                border-radius: 5px;
                font-size: 14px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #a5d6a7;
            }
        """)
        confirm_btn.clicked.connect(self.accept)
        
        button_layout.addStretch()
        button_layout.addWidget(cancel_btn)
        button_layout.addWidget(confirm_btn)
        button_layout.addStretch()
        
        layout.addLayout(button_layout)
        
        self.setLayout(layout)
    
    def load_and_display_field(self):
        """Load field image and draw marker if location is set"""
        # Load original image
        pixmap = QPixmap(self.field_image_path)
        
        # Scale to display size
        pixmap = pixmap.scaled(self.field_width, self.field_height, 
                               Qt.KeepAspectRatio, Qt.SmoothTransformation)
        
        # Draw marker if location is set
        if self.selected_x is not None and self.selected_y is not None:
            pixmap = self.draw_marker_on_pixmap(pixmap, self.selected_x, self.selected_y)
        
        self.field_label.setPixmap(pixmap)
    
    def draw_marker_on_pixmap(self, pixmap, x, y):
        """
        Draw a red marker on the pixmap at the given coordinates.
        
        Args:
            pixmap: QPixmap to draw on
            x: X coordinate (0-100)
            y: Y coordinate (0-100)
        
        Returns:
            QPixmap with marker drawn
        """
        painter = QPainter(pixmap)
        painter.setRenderHint(QPainter.Antialiasing)
        
        # Convert coordinates to pixel position
        pixel_x, pixel_y = self.coords_to_pixels(x, y)
        
        # Draw red circle marker
        pen = QPen(QColor(255, 0, 0), 3)
        painter.setPen(pen)
        brush = QBrush(QColor(255, 0, 0, 180))
        painter.setBrush(brush)
        painter.drawEllipse(QPoint(pixel_x, pixel_y), 8, 8)
        
        # Draw white outline
        pen = QPen(QColor(255, 255, 255), 2)
        painter.setPen(pen)
        painter.setBrush(Qt.NoBrush)
        painter.drawEllipse(QPoint(pixel_x, pixel_y), 8, 8)
        
        painter.end()
        return pixmap
    
    def handle_field_click(self, pos):
        """
        Handle click on field image.
        
        Args:
            pos: QPoint with click position
        """
        # Convert pixel position to coordinates
        x, y = self.pixels_to_coords(pos.x(), pos.y())
        
        # Store selected coordinates
        self.selected_x = x
        self.selected_y = y
        
        # Redraw field with marker
        self.load_and_display_field()
        
        # Update coordinate display
        self.update_coordinate_display()
    
    def pixels_to_coords(self, pixel_x, pixel_y):
        """
        Convert pixel position to field coordinates (0-100).
        
        Args:
            pixel_x: X position in pixels
            pixel_y: Y position in pixels
        
        Returns:
            Tuple of (x, y) in 0-100 scale
        """
        # Convert to 0-100 scale
        x = (pixel_x / self.field_width) * 100
        y = ((self.field_height - pixel_y) / self.field_height) * 100  # Invert Y (bottom = 0)
        
        # Clamp to 0-100 range
        x = max(0, min(100, x))
        y = max(0, min(100, y))
        
        # Round to 1 decimal place
        x = round(x, 1)
        y = round(y, 1)
        
        return x, y
    
    def coords_to_pixels(self, x, y):
        """
        Convert field coordinates (0-100) to pixel position.
        
        Args:
            x: X coordinate (0-100)
            y: Y coordinate (0-100)
        
        Returns:
            Tuple of (pixel_x, pixel_y)
        """
        pixel_x = int((x / 100) * self.field_width)
        pixel_y = int(((100 - y) / 100) * self.field_height)  # Invert Y (bottom = 0)
        
        return pixel_x, pixel_y
    
    def update_coordinate_display(self):
        """Update the coordinate display label"""
        if self.selected_x is not None and self.selected_y is not None:
            self.coord_label.setText(f"Selected Location: X = {self.selected_x:.1f}, Y = {self.selected_y:.1f}")
        else:
            self.coord_label.setText("Click on the field to select a location")
    
    def get_coordinates(self):
        """
        Get the selected coordinates.
        
        Returns:
            Tuple of (x, y) or (None, None) if not set
        """
        return self.selected_x, self.selected_y