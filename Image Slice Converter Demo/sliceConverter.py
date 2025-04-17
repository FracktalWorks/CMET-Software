import os
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QPushButton, QLabel, QFileDialog, QLineEdit, QWidget, QMessageBox
)
from PIL import Image


class ImageSplitterApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Image Splitter")
        self.setGeometry(100, 100, 400, 200)

        # Main layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # File selection button
        self.file_label = QLabel("No file selected")
        self.layout.addWidget(self.file_label)

        self.select_file_button = QPushButton("Select Image File")
        self.select_file_button.clicked.connect(self.select_file)
        self.layout.addWidget(self.select_file_button)

        # Output folder name input
        self.output_name_label = QLabel("Output Folder Name (optional):")
        self.layout.addWidget(self.output_name_label)

        self.output_name_input = QLineEdit()
        self.layout.addWidget(self.output_name_input)

        # Start processing button
        self.process_button = QPushButton("Split Image")
        self.process_button.clicked.connect(self.split_image)
        self.layout.addWidget(self.process_button)

        self.selected_file = None

    def select_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Image File", "", "Bitmap Images (*.bmp)")
        if file_path:
            self.selected_file = file_path
            self.file_label.setText(f"Selected File: {os.path.basename(file_path)}")

    def split_image(self):
        if not self.selected_file:
            QMessageBox.warning(self, "Error", "Please select an image file first.")
            return

        # Get the output folder name
        base_name = os.path.splitext(os.path.basename(self.selected_file))[0]
        output_name = self.output_name_input.text().strip()
        output_folder = output_name if output_name else f"{base_name}_tiles"
        output_dir = os.path.join(os.path.dirname(self.selected_file), output_folder)

        # Perform the image splitting
        try:
            self.perform_split(self.selected_file, output_dir)
            QMessageBox.information(self, "Success", f"Image split successfully! Tiles saved in: {output_dir}")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred: {str(e)}")

    def perform_split(self, input_path, output_dir, tile_width=2560, tile_height=1600):
        # Open the input image
        with Image.open(input_path) as img:
            img = img.convert("RGB")  # Convert to RGB mode
            width, height = img.size

            # Ensure the output directory exists
            os.makedirs(output_dir, exist_ok=True)

            # Calculate the number of tiles
            x_tiles = (width + tile_width - 1) // tile_width
            y_tiles = (height + tile_height - 1) // tile_height

            # Split the image into tiles
            for x in range(x_tiles):
                for y in range(y_tiles):
                    left = x * tile_width
                    upper = y * tile_height
                    right = min(left + tile_width, width)
                    lower = min(upper + tile_height, height)

                    # Crop the image
                    cropped_img = img.crop((left, upper, right, lower))

                    # Create a black background image for the tile
                    tile = Image.new("RGB", (tile_width, tile_height), (0, 0, 0))
                    tile.paste(cropped_img, (0, 0))

                    # Save the tile as BMP
                    output_file = os.path.join(output_dir, f"tile_{x}_{y}.bmp")
                    tile.save(output_file)

# Main application
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = ImageSplitterApp()
    window.show()
    sys.exit(app.exec_())