import tkinter as tk
from tkinter import filedialog
import mysql.connector

def upload_image():
    filename = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    if filename:
        try:
            with open(filename, "rb") as img_file:
                img_data = img_file.read()

            # Connect to your MySQL database
            mydb = mysql.connector.connect(
                host='127.0.0.1',
                user='root',
                password='anish123',
                database='carnival'
            )

            mycursor = mydb.cursor()
            # Insert the image data into the table
            sql = "INSERT INTO images (image_data) VALUES (%s)"
            mycursor.execute(sql, (img_data,))
            mydb.commit()  # Commit the changes

            mycursor.close()
            mydb.close()
            print("Image uploaded successfully!")
        except Exception as e:
            print(f"Error uploading image: {e}")
    else:
        print("No file selected. Please choose an image.")

if __name__ == "__main__":
    window = tk.Tk()
    window.title("Image Uploader")

    button_upload = tk.Button(window, text="Upload Image", command=upload_image)
    button_upload.pack()

    window.mainloop()
