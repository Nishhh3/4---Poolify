import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import os
import sys
from PIL import Image, ImageTk
import subprocess

class SkincareChatbot:
    def __init__(self, root):
        self.root = root
        self.root.title("Skincare Assistant")
        self.root.geometry("1920x1080")  # Full HP Victus screen resolution
        
        # Set sage green color scheme
        self.sage_green = "#8A9A5B"
        self.sage_light = "#C4D7B2"
        self.sage_dark = "#5F7161"
        self.text_color = "#333333"
        
        # Configure the style
        self.style = ttk.Style()
        self.style.configure("TFrame", background=self.sage_light)
        self.style.configure("TButton", 
                             background=self.sage_green, 
                             foreground=self.text_color, 
                             font=("Arial", 12, "bold"),
                             padding=8)
        self.style.map("TButton", 
                      background=[("active", self.sage_dark), ("pressed", self.sage_dark)])
        self.style.configure("TLabel", 
                            background=self.sage_light, 
                            foreground=self.text_color, 
                            font=("Arial", 12))
        
        # Main frame
        self.main_frame = ttk.Frame(root)
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Header
        self.header_frame = ttk.Frame(self.main_frame)
        self.header_frame.pack(fill=tk.X, padx=20, pady=10)
        
        self.title_label = ttk.Label(self.header_frame, 
                                     text="Skincare Assistant", 
                                     font=("Arial", 24, "bold"),
                                     background=self.sage_light)
        self.title_label.pack(side=tk.LEFT, padx=10)
        
        # Back button
        self.back_button = ttk.Button(self.header_frame, 
                                      text="Back", 
                                      command=self.go_back)
        self.back_button.pack(side=tk.RIGHT, padx=10)
        
        # Content area
        self.content_frame = ttk.Frame(self.main_frame)
        self.content_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        # Left panel (Chat)
        self.chat_frame = ttk.Frame(self.content_frame, padding=10)
        self.chat_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Chat display area
        self.chat_display = tk.Text(self.chat_frame, 
                                   wrap=tk.WORD, 
                                   bg=self.sage_light, 
                                   fg=self.text_color,
                                   font=("Arial", 12),
                                   padx=10, pady=10,
                                   state='disabled',
                                   highlightthickness=0,
                                   relief=tk.FLAT)
        self.chat_display.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Chat scrollbar
        self.chat_scrollbar = ttk.Scrollbar(self.chat_display, command=self.chat_display.yview)
        self.chat_display['yscrollcommand'] = self.chat_scrollbar.set
        self.chat_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # User input area
        self.user_input_frame = ttk.Frame(self.chat_frame)
        self.user_input_frame.pack(fill=tk.X, pady=10)
        
        self.user_input = ttk.Entry(self.user_input_frame, font=("Arial", 12))
        self.user_input.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        self.user_input.bind("<Return>", self.send_message)
        
        self.send_button = ttk.Button(self.user_input_frame, 
                                    text="Send", 
                                    command=self.send_message)
        self.send_button.pack(side=tk.RIGHT, padx=5)
        
        # Right panel (FAQ and Image Upload)
        self.right_panel = ttk.Frame(self.content_frame, padding=10, width=350)
        self.right_panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=False, padx=10)
        self.right_panel.pack_propagate(False)  # Prevent the frame from shrinking to fit its contents
        
        # FAQ section
        self.faq_label = ttk.Label(self.right_panel, 
                                  text="Common Questions", 
                                  font=("Arial", 16, "bold"))
        self.faq_label.pack(fill=tk.X, pady=10)
        
        # Create a canvas with scrollbar for the FAQ section
        self.faq_canvas = tk.Canvas(self.right_panel, bg=self.sage_light, highlightthickness=0)
        self.faq_scrollbar = ttk.Scrollbar(self.right_panel, orient="vertical", command=self.faq_canvas.yview)
        self.faq_frame = ttk.Frame(self.faq_canvas, style="TFrame")
        
        self.faq_canvas.configure(yscrollcommand=self.faq_scrollbar.set)
        self.faq_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.faq_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.faq_canvas.create_window((0, 0), window=self.faq_frame, anchor="nw")
        self.faq_frame.bind("<Configure>", lambda e: self.faq_canvas.configure(scrollregion=self.faq_canvas.bbox("all")))
        
        # FAQ buttons
        self.faq_questions = [
            "How to build a skincare routine?",
            "How to treat acne?",
            "What products for dry skin?",
            "How to reduce wrinkles?",
            "What is SPF?",
            "How often to exfoliate?",
            "What are retinoids?",
            "Help with skin redness",
            "How to layer products?",
            "Best ingredients for oily skin?"
        ]
        
        for question in self.faq_questions:
            faq_button = ttk.Button(self.faq_frame, 
                                   text=question, 
                                   command=lambda q=question: self.select_faq(q))
            faq_button.pack(fill=tk.X, pady=3)
        
        # Image upload section
        self.upload_frame = ttk.Frame(self.main_frame, padding=10)
        self.upload_frame.pack(fill=tk.X, padx=20, pady=10)
        
        self.upload_label = ttk.Label(self.upload_frame, 
                                     text="Upload Skin Image", 
                                     font=("Arial", 16, "bold"))
        self.upload_label.pack(side=tk.LEFT, padx=5)
        
        self.upload_button = ttk.Button(self.upload_frame, 
                                      text="Choose Image", 
                                      command=self.upload_image)
        self.upload_button.pack(side=tk.LEFT, padx=10)
        
        self.image_label = ttk.Label(self.upload_frame, 
                                    text="No image selected", 
                                    background=self.sage_light)
        self.image_label.pack(side=tk.LEFT, padx=10)
        
        # Add a large image display area that will appear when an image is uploaded
        self.main_image_frame = ttk.Frame(self.main_frame, padding=10)
        self.main_image_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        self.main_image_display = ttk.Label(self.main_image_frame, 
                                           background=self.sage_light, 
                                           text="Upload an image to analyze your skin")
        self.main_image_display.pack(fill=tk.BOTH, expand=True)
        
        # Add 10 more Q&A pairs to reach 20 total
        additional_qa = {
            "What's the difference between AHA and BHA?": 
                "AHAs (Alpha Hydroxy Acids) like glycolic acid work on the skin surface, improving texture and brightness. BHAs (Beta Hydroxy Acids) like salicylic acid are oil-soluble and penetrate pores to clear buildup. AHAs work better for dry skin, while BHAs are ideal for oily, acne-prone skin.",
            
            "How to treat dark spots?": 
                "For dark spots, use: 1) Vitamin C serum 2) Alpha arbutin 3) Kojic acid 4) Niacinamide 5) Sunscreen daily (prevents darkening). Results take 8-12 weeks. For stubborn spots, consult a dermatologist for professional treatments.",
            
            "Is double cleansing necessary?": 
                "Double cleansing (oil-based cleanser followed by water-based cleanser) is beneficial if you wear sunscreen, makeup, or have oily skin. It ensures thorough removal of oil-based impurities. If you have dry or sensitive skin, you might prefer single cleansing with a gentle formula.",
            
            "How to deal with under-eye circles?": 
                "For under-eye circles: 1) Caffeine serums (reduce puffiness) 2) Vitamin C (brightens) 3) Retinol (thickens skin) 4) Peptides (strengthen area) 5) Sufficient sleep and hydration. Genetic dark circles may need concealer or dermatological treatments.",
            
            "What is skin purging?": 
                "Purging is a temporary breakout when starting active ingredients like retinoids or AHAs/BHAs. It happens as turnover accelerates, bringing hidden congestion to the surface. Unlike a reaction, purging occurs where you normally break out and resolves within 4-6 weeks.",
            
            "How to care for sensitive skin?": 
                "For sensitive skin: 1) Patch test new products 2) Use fragrance-free formulas 3) Minimal ingredients lists 4) Gentle cleansers with pH 4.5-5.5 5) Physical sunscreens (zinc oxide/titanium dioxide) 6) Introduce new products one at a time, with 2 weeks between.",
            
            "When to see a dermatologist?": 
                "See a dermatologist if you have: persistent acne unresponsive to OTC treatments, unexpected skin changes, painful or rapidly changing moles, severe redness/inflammation, scarring, or any skin condition causing physical discomfort or emotional distress.",
            
            "Can diet affect skin?": 
                "Yes, diet can affect skin. High-glycemic foods and dairy may trigger acne in some people. Foods rich in antioxidants, omega-3s, and vitamins A, C, and E support skin health. Hydration is also essential. Individual responses vary, so observe how your skin reacts to diet changes.",
            
            "How to treat combination skin?": 
                "For combination skin, use gentle cleansers, hydrating but light moisturizers, and consider multi-masking (applying different masks to different areas). Focus oil-controlling products on the T-zone only. Gel-cream textures often work well for balanced hydration.",
            
            "What are ceramides?": 
                "Ceramides are lipids (fats) naturally found in skin that maintain the moisture barrier and protect against environmental damage. They make up about 50% of the skin barrier. As we age, ceramide levels decrease, so using ceramide-containing products helps restore moisture and protection."
        }
        
        # Add additional FAQ buttons
        for question in additional_qa.keys():
            faq_button = ttk.Button(self.faq_frame, 
                                   text=question, 
                                   command=lambda q=question: self.select_faq(q))
            faq_button.pack(fill=tk.X, pady=3)
        
        # Initialize chat with welcome message
        self.display_bot_message("Hello! I'm your skincare assistant. How can I help you today? You can ask me questions or choose from common topics on the right. Upload an image of your skin for personalized advice.")
        
        # Define FAQ answers
        self.faq_answers = {
            "How to build a skincare routine?": 
                "Basic skincare routine: 1) Cleanser 2) Toner (optional) 3) Treatment products 4) Moisturizer 5) Sunscreen (AM only). Start simple and add products gradually. Listen to your skin's response!",
            
            "How to treat acne?": 
                "For acne, try products with salicylic acid, benzoyl peroxide, or retinoids. Keep skin clean, don't pick at pimples, and consider seeing a dermatologist for severe cases. Diet and stress can also affect acne.",
            
            "What products for dry skin?": 
                "For dry skin, look for: 1) Gentle, non-foaming cleansers 2) Hydrating toners 3) Hyaluronic acid serums 4) Rich moisturizers with ceramides 5) Facial oils like squalane or jojoba. Avoid harsh alcohols and fragrance.",
            
            "How to reduce wrinkles?": 
                "For wrinkles, focus on: 1) Retinoids (gold standard for anti-aging) 2) Sunscreen daily 3) Vitamin C serum 4) Peptides 5) Moisturizers with hyaluronic acid. Consistency is key for results.",
            
            "What is SPF?": 
                "SPF (Sun Protection Factor) measures how well sunscreen protects against UVB rays. SPF 30 blocks about 97% of UVB rays. For daily use, choose broad-spectrum SPF 30+ and reapply every 2 hours when outside.",
            
            "How often to exfoliate?": 
                "Exfoliation frequency depends on your skin type. Dry/sensitive: 1-2 times weekly. Normal: 2-3 times weekly. Oily: 3-4 times weekly. Chemical exfoliants (AHAs/BHAs) are generally gentler than physical scrubs.",
            
            "What are retinoids?": 
                "Retinoids are vitamin A derivatives that promote cell turnover, boost collagen, and help with acne and signs of aging. Start with low concentrations (0.25-0.5%) 1-2 times weekly, then gradually increase. Always use sunscreen when using retinoids.",
            
            "Help with skin redness": 
                "For skin redness: 1) Identify triggers (spicy foods, alcohol, temperature changes) 2) Use gentle, fragrance-free products 3) Try ingredients like centella asiatica, green tea, licorice root, or azelaic acid 4) See a dermatologist if severe.",
            
            "How to layer products?": 
                "Layer skincare from thinnest to thickest: 1) Cleanser 2) Toner 3) Essence 4) Serums 5) Ampoules 6) Moisturizer 7) Facial oil 8) Sunscreen (AM) or sleeping mask (PM). Wait 30-60 seconds between layers for better absorption.",
            
            "Best ingredients for oily skin?": 
                "For oily skin, look for: 1) Salicylic acid (BHA) - unclogs pores 2) Niacinamide - regulates sebum 3) Hyaluronic acid - lightweight hydration 4) Clay masks - absorbs excess oil 5) Non-comedogenic, oil-free moisturizers."
        }
        
        # Merge the additional Q&A with the existing ones
        self.faq_answers.update(additional_qa)
    
    def display_bot_message(self, message):
        self.chat_display.config(state='normal')
        self.chat_display.insert(tk.END, "Assistant: " + message + "\n\n")
        self.chat_display.config(state='disabled')
        self.chat_display.see(tk.END)
    
    def display_user_message(self, message):
        self.chat_display.config(state='normal')
        self.chat_display.insert(tk.END, "You: " + message + "\n\n")
        self.chat_display.config(state='disabled')
        self.chat_display.see(tk.END)
    
    def send_message(self, event=None):
        message = self.user_input.get().strip()
        if message:
            self.display_user_message(message)
            self.user_input.delete(0, tk.END)
            
            # Process message and determine response
            self.process_message(message)
    
    def process_message(self, message):
        # Convert message to lowercase for easier matching
        message_lower = message.lower()
        
        # Check if message matches any FAQ keywords
        for question, answer in self.faq_answers.items():
            # Create keywords from the question
            keywords = question.lower().split()
            
            # Check if any keyword is in the user's message
            if any(keyword in message_lower for keyword in keywords if len(keyword) > 3):
                self.display_bot_message(answer)
                return
        
        # Check for specific keywords in the message
        if "upload" in message_lower or "image" in message_lower or "picture" in message_lower:
            self.display_bot_message("You can upload an image of your skin by clicking the 'Choose Image' button at the top of the screen.")
        
        elif "routine" in message_lower or "regimen" in message_lower:
            self.display_bot_message(self.faq_answers["How to build a skincare routine?"])
        
        elif "acne" in message_lower or "pimple" in message_lower or "breakout" in message_lower:
            self.display_bot_message(self.faq_answers["How to treat acne?"])
        
        elif "dry" in message_lower or "flaky" in message_lower:
            self.display_bot_message(self.faq_answers["What products for dry skin?"])
        
        elif "oily" in message_lower or "greasy" in message_lower:
            self.display_bot_message(self.faq_answers["Best ingredients for oily skin?"])
        
        elif "wrinkle" in message_lower or "anti-aging" in message_lower or "fine line" in message_lower:
            self.display_bot_message(self.faq_answers["How to reduce wrinkles?"])
        
        elif "spf" in message_lower or "sunscreen" in message_lower or "sun" in message_lower:
            self.display_bot_message(self.faq_answers["What is SPF?"])
        
        else:
            # Default response for unrecognized queries
            self.display_bot_message("I'm not sure I understand your question. Could you try rephrasing it or select one of the common questions from the right panel?")
    
    def select_faq(self, question):
        self.display_user_message(question)
        self.display_bot_message(self.faq_answers[question])
    
    def upload_image(self):
        file_path = filedialog.askopenfilename(
            title="Select Skin Image",
            filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp")]
        )
        
        if file_path:
            try:
                # Save file path for reference
                self.current_image_path = file_path
                
                # Display file name
                file_name = os.path.basename(file_path)
                self.image_label.config(text=f"Selected: {file_name}")
                
                # Display the image in the main image area
                image = Image.open(file_path)
                
                # Get the window dimensions
                window_width = self.main_image_frame.winfo_width()
                window_height = self.main_image_frame.winfo_height()
                
                # Calculate the max size while maintaining aspect ratio
                max_width = window_width - 40
                max_height = window_height - 40
                
                # Get original dimensions
                original_width, original_height = image.size
                
                # Calculate scaling factors
                width_ratio = max_width / original_width
                height_ratio = max_height / original_height
                
                # Use the smaller ratio to ensure image fits
                scaling_factor = min(width_ratio, height_ratio)
                
                # Calculate new dimensions
                new_width = int(original_width * scaling_factor)
                new_height = int(original_height * scaling_factor)
                
                # Resize the image while maintaining aspect ratio
                resized_image = image.resize((new_width, new_height), Image.LANCZOS)
                
                # Convert to PhotoImage
                photo = ImageTk.PhotoImage(resized_image)
                
                # Update the main image display
                self.main_image_display.config(image=photo)
                self.main_image_display.image = photo  # Keep reference
                
                # Confirm to user
                self.display_bot_message(f"Image '{file_name}' uploaded successfully. I can see your skin concern. What specific questions do you have about the condition shown in the image?")
                
            except Exception as e:
                messagebox.showerror("Error", f"Could not open image: {str(e)}")
                print(f"Error: {str(e)}")
    
    def go_back(self):
        try:
            # Run the dbv.py file
            subprocess.Popen([sys.executable, "dbv.py"])
            # Close current window
            self.root.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"Could not open dbv.py: {str(e)}")
            print(f"Error: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = SkincareChatbot(root)
    root.mainloop()