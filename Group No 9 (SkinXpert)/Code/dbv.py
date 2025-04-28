

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import os
from PIL import Image, ImageTk
import subprocess
import sys
import pymysql

class SkinExpertDashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("SkinXpert - Your Personal Skin Care Assistant")
        self.root.state('zoomed')

        self.primary_color = "#4D614D"
        self.secondary_color = "#E1E6DD"
        self.bg_color = "#E1E6DD"
        self.text_color = "#32403A"
        self.accent_color = "#C8A95B"
        self.light_text = "#FFFFFF"

        self.background_image_path = "gcr1.jpg"
        self.current_frame = None

        self.main_frame = tk.Frame(self.root, bg=self.bg_color)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        self.create_header()
        self.content_area = tk.Frame(self.main_frame, bg=self.bg_color)
        self.content_area.pack(fill=tk.BOTH, expand=True)

        self.create_sidebar()
        self.show_page("home")

    def create_header(self):
        header = tk.Frame(self.main_frame, bg=self.primary_color, height=70)
        header.pack(fill=tk.X)

        logo_label = tk.Label(header, text="SkinXpert", font=("Times New Roman", 26, "bold"), 
                             bg=self.primary_color, fg=self.light_text)
        logo_label.pack(side=tk.LEFT, padx=20, pady=10)

        logout_btn = tk.Button(header, text="Logout", font=("Helvetica", 12),
                              bg=self.accent_color, fg=self.text_color, 
                              cursor="hand2", bd=0, padx=15, pady=5,
                              command=self.logout)
        logout_btn.pack(side=tk.RIGHT, padx=20, pady=15)

    def create_sidebar(self):
        sidebar = tk.Frame(self.content_area, bg=self.primary_color, width=250)
        sidebar.pack(side=tk.LEFT, fill=tk.Y)
        sidebar.pack_propagate(False)

        self.page_container = tk.Frame(self.content_area, bg=self.bg_color)
        self.page_container.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        sidebar_title = tk.Label(sidebar, text="Decode Your Skin", font=("Times New Roman", 18, "bold"),
                               bg=self.primary_color, fg=self.light_text)
        sidebar_title.pack(pady=(30, 20))

        separator = tk.Frame(sidebar, height=2, bg=self.accent_color)
        separator.pack(fill=tk.X, padx=20, pady=5)

        nav_items = [
            {"name": "home", "text": "Home", "icon": "🏠"},
            {"name": "remedies", "text": "Home Remedies", "icon": "🌿", "command": self.open_home_remedies},
            {"name": "routine", "text": "My Routine", "icon": "⏰","command": self.open_my_routine},
            {"name": "chatbot", "text": "Skin Advisor", "icon": "💬", "command": self.open_chatbot},
            {"name": "quiz", "text": "Quiz Results", "icon": "📋"},
            {"name": "cleanser", "text": "Cleansers", "icon": "🫧","command": self.open_cleanser},
            {"name": "sunscreen", "text": "Sunscreens", "icon": "☀️","command": self.open_sunscreen},
            {"name": "toner", "text": "Toners", "icon": "🪞","command": self.open_toner},
            {"name": "moisturizer", "text": "Moisturizer", "icon": "🧴","command": self.open_moisturizer}
        ]

        btn_container = tk.Frame(sidebar, bg=self.primary_color)
        btn_container.pack(fill=tk.X, padx=20, pady=10)

        for item in nav_items:
            btn = tk.Button(btn_container, 
                           text=f"{item['icon']} {item['text']}", 
                           font=("Helvetica", 12),
                           bg=self.primary_color, 
                           fg=self.light_text,
                           bd=0, cursor="hand2",
                           anchor="w", padx=10, pady=10,
                           width=20,
                           command=item.get("command", lambda i=item["name"]: self.show_page(i)))
            btn.pack(fill=tk.X, pady=2)

    def show_page(self, page_name):
        if self.current_frame:
            self.current_frame.destroy()

        self.current_frame = tk.Frame(self.page_container, bg=self.bg_color)
        self.current_frame.pack(fill=tk.BOTH, expand=True)

        if page_name == "home":
            self.set_background_image()

            title = tk.Label(self.current_frame, text=page_name.replace("_", " ").title(), 
                         font=("Times New Roman", 24, "bold"), bg=self.bg_color, fg=self.text_color)
            title.pack(pady=20)
        elif page_name=='quiz':
            connection = pymysql.connect(host='localhost', user='root', password='123456', database='skinxpert')
            cur = connection.cursor()

# Fetch Skin Type
            cur.execute("SELECT skintype FROM signup WHERE id = 1")
            fetch_result = cur.fetchone()  # Fetch one row

            if fetch_result:  
             stype = fetch_result[0]  # Extract skin type
            else:
                stype = "Unknown"  # Default if no result is found

                cur1=connection.cursor()
                cur1.execute("SELECT alevel FROM signup WHERE id = 1")
                connection.close()
            
# Create label inside the Tkinter window
            skintypelabel = tk.Label(self.content_area, text=f"Your Skin Type is {stype}", font=("Times New Roman", 32),bg='darkseagreen4', fg='wheat2')
            skintypelabel.place(x=400, y=100)
            

            if stype=='Dry Skin':
                a=tk.Label(self.content_area,text="You need ingredients that hydrate and strengthen the skin barrier while also addressing breakouts without causing irritation.",bg='darkseagreen4',font=("Times New Roman",18),fg='wheat2')
                a.place(x=30,y=250)
                label=tk.Label(self.content_area,text="•Hydrating & Barrier-Strengthening Ingredients:",font=("Times New Roman",17),bg='darkseagreen4',fg='wheat2')
                label.place(x=45,y=300)
                b=tk.Label(self.content_area,text="Hyaluronic Acid – Deeply hydrates the skin, preventing flakiness.",font=("Times New Roman",15),bg='darkseagreen4',fg='wheat2')
                b.place(x=400,y=330)
                b1=tk.Label(self.content_area,text="Glycerin – A humectant that attracts moisture and keeps skin supple.",font=("Times New Roman",15),bg='darkseagreen4',fg='wheat2')
                b1.place(x=400,y=3400)
                b2=tk.Label(self.content_area,text="Niacinamide (2-5%) – Reduces redness, strengthens the skin barrier, and controls oil production.",bg='darkseagreen4',font=("Times New Roman",15),fg='wheat2')
                b2.place(x=400,y=390)
                b3=tk.Label(self.content_area,text="Ceramides – Restore the skin barrier and prevent moisture loss.",font=("Times New Roman",15),bg='darkseagreen4',fg='wheat2')
                b3.place(x=400,y=420)
                c1=tk.Label(self.content_area,text="•Gentle Acne-Fighting Ingredients:",font=("Times New Roman",17),bg='darkseagreen4',fg='wheat2')
                c1.place(x=45,y=470)
                c=tk.Label(self.content_area,text="Lactic Acid – A mild exfoliant that removes dead skin while keeping skin hydrated.",font=("Times New Roman",15),bg='darkseagreen4',fg='wheat2')
                c.place(x=400,y=500)
                c2=tk.Label(self.content_area,text="Azelaic Acid (10%) – Reduces inflammation and fades acne marks.",font=("Times New Roman",15),bg='darkseagreen4',fg='wheat2')
                c2.place(x=400,y=530)
                c3=tk.Label(self.content_area,text="Mandelic Acid – A gentle AHA that fights acne and evens skin tone.",font=("Times New Roman",15),bg='darkseagreen4',fg='wheat2')
                c3.place(x=400,y=5400)
                c4=tk.Label(self.content_area,text="Zinc PCA – Helps control mild acne without drying out the skin.",font=("Times New Roman",15),bg='darkseagreen4',fg='wheat2')
                c4.place(x=400,y=590)
            
            elif stype=='Oily Skin':
                a=tk.Label(self.content_area,text="You need ingredients that control excess oil, unclog pores, and prevent breakouts while maintaining hydration.",bg='darkseagreen4',font=("Times New Roman",18),fg='wheat2')
                a.place(x=350,y=250)
                label=tk.Label(self.content_area,text="•Oil-Control & Hydration Ingredients:",font=("Times New Roman",17),bg='darkseagreen4',fg='wheat2')
                label.place(x=350,y=300)
                b=tk.Label(self.content_area,text="Niacinamide (5-10%) – Reduces oil production, minimizes pores, and soothes inflammation.",font=("Times New Roman",15),bg='darkseagreen4',fg='wheat2')
                b.place(x=400,y=330)
                b1=tk.Label(self.content_area,text="Zinc PCA – Regulates sebum production and helps fight acne-causing bacteria.",font=("Times New Roman",15),bg='darkseagreen4',fg='wheat2')
                b1.place(x=400,y=360)
                b2=tk.Label(self.content_area,text="Green Tea Extract – Antioxidant-rich, reduces inflammation and controls oil.",bg='darkseagreen4',font=("Times New Roman",15),fg='wheat2')
                b2.place(x=400,y=390)
                b3=tk.Label(self.content_area,text="Aloe Vera – Lightweight hydrator that soothes acne-prone skin.",font=("Times New Roman",15),bg='darkseagreen4',fg='wheat2')
                b3.place(x=400,y=420)
                c1=tk.Label(self.content_area,text="•Acne-Fighting & Exfoliating Ingredients:",font=("Times New Roman",17),bg='darkseagreen4',fg='wheat2')
                c1.place(x=350,y=470)
                c=tk.Label(self.content_area,text="Salicylic Acid (BHA, 1-2%) – Unclogs pores, reduces blackheads, and controls oil.",font=("Times New Roman",15),bg='darkseagreen4',fg='wheat2')
                c.place(x=400,y=500)
                c2=tk.Label(self.content_area,text="Azelaic Acid (10%) – Treats mild acne, reduces redness, and evens out skin tone.",font=("Times New Roman",15),bg='darkseagreen4',fg='wheat2')
                c2.place(x=400,y=530)
                c3=tk.Label(self.content_area,text=" Tea Tree Oil – Natural antibacterial that helps fight acne.",font=("Times New Roman",15),bg='darkseagreen4',fg='wheat2')
                c3.place(x=400,y=560)
                c4=tk.Label(self.content_area,text="Lactic Acid or Mandelic Acid (Gentle AHAs) – Exfoliate without over-drying.",font=("Times New Roman",15),bg='darkseagreen4',fg='wheat2')
                c4.place(x=400,y=590)
           
    def set_background_image(self):
        """Set background image on the home page."""
        try:
            if not os.path.exists(self.background_image_path):
                print(f"Error: Background image {self.background_image_path} not found.")
                return

            original = Image.open(self.background_image_path)
            container_width = self.page_container.winfo_width()
            container_height = self.page_container.winfo_height()

            if container_width <= 1:  # Ensures width is valid when first loaded
                container_width = self.root.winfo_screenwidth() - 250
                container_height = self.root.winfo_screenheight() - 70

            resized = original.resize((container_width, container_height), Image.LANCZOS)
            bg_image = ImageTk.PhotoImage(resized)

            bg_label = tk.Label(self.current_frame, image=bg_image)
            bg_label.image = bg_image  # Keep a reference
            bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        except Exception as e:
            print(f"Could not load background image: {e}")

    def open_chatbot(self):
        """Open chatbot.py when clicking Skin Advisor."""
        chatbot_path = "chatbot.py"

        if not os.path.exists(chatbot_path):
            messagebox.showerror("Error", "chatbot.py not found. Make sure it's in the same directory.")
            return

        try:
            subprocess.Popen([sys.executable, chatbot_path])
        except Exception as e:
            messagebox.showerror("Error", f"Could not open chatbot.py:\n{e}")



    def open_home_remedies(self):
        """Open hr2.py when clicking Home Remedies."""
        remedies_path = "hr2.py"

        if not os.path.exists(remedies_path):
            messagebox.showerror("Error", "hr2.py not found. Make sure it's in the same directory.")
            return

        try:
            subprocess.Popen([sys.executable, remedies_path])
        except Exception as e:
            messagebox.showerror("Error", f"Could not open hr2.py:\n{e}")


    def open_cleanser(self):
        """Open hr2.py when clicking Home Remedies."""
        cleanser_path = "dashboard.py"

        if not os.path.exists(cleanser_path):
            messagebox.showerror("Error", "dashboaard.py not found. Make sure it's in the same directory.")
            return

        try:
            self.ptype = "cleanser"
            subprocess.run(["python","dashboard.py",self.ptype])
        except Exception as e:
            messagebox.showerror("Error", f"Could not open dashboard.py:\n{e}")

    def open_sunscreen(self):
        """Open hr2.py when clicking Home Remedies."""
        cleanser_path = "dashboard.py"

        if not os.path.exists(cleanser_path):
            messagebox.showerror("Error", "dashboaard.py not found. Make sure it's in the same directory.")
            return

        try:
            self.ptype = "sunscreen"
            subprocess.run(["python","dashboard.py",self.ptype])
        except Exception as e:
            messagebox.showerror("Error", f"Could not open dashboard.py:\n{e}")

    def open_sunscreen(self):
        """Open hr2.py when clicking Home Remedies."""
        cleanser_path = "dashboard.py"

        if not os.path.exists(cleanser_path):
            messagebox.showerror("Error", "dashboaard.py not found. Make sure it's in the same directory.")
            return

        try:
            self.ptype = "sunscreen"
            subprocess.run(["python","dashboard.py",self.ptype])
        except Exception as e:
            messagebox.showerror("Error", f"Could not open dashboard.py:\n{e}")

    def open_toner(self):
        """Open hr2.py when clicking Home Remedies."""
        cleanser_path = "dashboard.py"

        if not os.path.exists(cleanser_path):
            messagebox.showerror("Error", "dashboaard.py not found. Make sure it's in the same directory.")
            return

        try:
            self.ptype = "toner"
            subprocess.run(["python","dashboard.py",self.ptype])
        except Exception as e:
            messagebox.showerror("Error", f"Could not open dashboard.py:\n{e}")


    def open_moisturizer(self):
        """Open hr2.py when clicking Home Remedies."""
        cleanser_path = "dashboard.py"

        if not os.path.exists(cleanser_path):
            messagebox.showerror("Error", "dashboaard.py not found. Make sure it's in the same directory.")
            return

        try:
            self.ptype = "moisturizer"
            subprocess.run(["python","dashboard.py",self.ptype])
        except Exception as e:
            messagebox.showerror("Error", f"Could not open dashboard.py:\n{e}")




            
    def open_my_routine(self):
        """Open mr.py when clicking Home Remedies."""
        remedies_path = "mr.py"

        if not os.path.exists(remedies_path):
            messagebox.showerror("Error", "mr.py not found. Make sure it's in the same directory.")
            return

        try:
            subprocess.Popen([sys.executable, remedies_path])
        except Exception as e:
            messagebox.showerror("Error", f"Could not open mr.py:\n{e}")



    def logout(self):
        if messagebox.askyesno("Logout", "Are you sure you want to logout?"):
            self.root.destroy()

# Main function to run the application
def main():
    root = tk.Tk()
    app = SkinExpertDashboard(root)
    root.mainloop()

if __name__ == "__main__":
    main()