import os
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QPushButton, QLabel, 
    QFileDialog, QLineEdit, QWidget, QMessageBox, QProgressBar
)
from PIL import Image


class ImageSplitterApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Image Splitter")
        self.setGeometry(100, 100, 400, 250)

        # Main layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # File/Folder selection button
        self.file_label = QLabel("No file/folder selected")
        self.layout.addWidget(self.file_label)

        self.select_file_button = QPushButton("Select Image File or Folder")
        self.select_file_button.clicked.connect(self.select_input)
        self.layout.addWidget(self.select_file_button)

        # Output folder name input
        self.output_name_label = QLabel("Output Folder Name (optional):")
        self.layout.addWidget(self.output_name_label)

        self.output_name_input = QLineEdit()
        self.layout.addWidget(self.output_name_input)

        # Progress bar
        self.progress_bar = QProgressBar()
        self.layout.addWidget(self.progress_bar)
        self.progress_bar.hide()

        # Start processing button
        self.process_button = QPushButton("Split Image(s)")
        self.process_button.clicked.connect(self.split_images)
        self.layout.addWidget(self.process_button)

        self.selected_path = None
        self.is_folder = False

    def select_input(self):
        options = QFileDialog.Options()
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.Directory)
        dialog.setOption(QFileDialog.ShowDirsOnly, False)
        path = dialog.getExistingDirectory(self, "Select Folder") or \
               dialog.getOpenFileName(self, "Select Image File", "", "Image Files (*.bmp *.png)")[0]
        
        if path:
            self.selected_path = path
            self.is_folder = os.path.isdir(path)
            display_name = os.path.basename(path) or path
            self.file_label.setText(f"Selected {'Folder' if self.is_folder else 'File'}: {display_name}")

    def get_all_image_files(self, folder_path):
        image_files = []
        for root, _, files in os.walk(folder_path):
            for file in files:
                if file.lower().endswith(('.bmp', '.png')):
                    image_files.append(os.path.join(root, file))
        return image_files

    def split_images(self):
        if not self.selected_path:
            QMessageBox.warning(self, "Error", "Please select an image file or folder first.")
            return

        try:
            if self.is_folder:
                image_files = self.get_all_image_files(self.selected_path)
                if not image_files:
                    QMessageBox.warning(self, "Error", "No BMP or PNG files found in the selected folder.")
                    return

                self.progress_bar.setMaximum(len(image_files))
                self.progress_bar.setValue(0)
                self.progress_bar.show()

                for i, file_path in enumerate(image_files):
                    base_name = os.path.splitext(os.path.basename(file_path))[0]
                    output_name = self.output_name_input.text().strip()
                    output_folder = output_name if output_name else base_name  # Removed "_tiles" suffix
                    output_dir = os.path.join(os.path.dirname(file_path), output_folder)
                    
                    self.perform_split(file_path, output_dir)
                    self.progress_bar.setValue(i + 1)
                
                self.progress_bar.hide()
                QMessageBox.information(self, "Success", "All images processed successfully!")
            else:
                base_name = os.path.splitext(os.path.basename(self.selected_path))[0]
                output_name = self.output_name_input.text().strip()
                output_folder = output_name if output_name else base_name  # Removed "_tiles" suffix
                output_dir = os.path.join(os.path.dirname(self.selected_path), output_folder)
                
                self.perform_split(self.selected_path, output_dir)
                QMessageBox.information(self, "Success", f"Image split successfully! Tiles saved in: {output_dir}")

        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred: {str(e)}")
            self.progress_bar.hide()

    def perform_split(self, input_path, output_dir, tile_width=2560, tile_height=1600):
        # Open the input image
        with Image.open(input_path) as img:
            img = img.convert("L")  # Convert to grayscale mode
            width, height = img.size

            # Ensure the output directory exists
            os.makedirs(output_dir, exist_ok=True)

            # Copy original image to output directory with "_original" suffix
            original_filename = os.path.basename(input_path)
            name, ext = os.path.splitext(original_filename)
            original_copy_path = os.path.join(output_dir, f"{name}_original{ext}")
            
            # Copy the original file to new location using grayscale conversion
            img.save(original_copy_path)
            
            # Delete the source image after successful copy
            try:
                os.remove(input_path)
            except Exception as e:
                QMessageBox.warning(self, "Warning", f"Could not delete source file: {str(e)}")

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
                    tile = Image.new("L", (tile_width, tile_height), 0)  # 0 is black in grayscale
                    tile.paste(cropped_img, (0, 0))

                    # Save the tile as BMP with optimized settings
                    output_file = os.path.join(output_dir, f"tile_{x}_{y}.bmp")
                    tile.save(output_file, compression=None)  # No compression for BMP, but using 8-bit depth


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = ImageSplitterApp()
    window.show()
    sys.exit(app.exec_())