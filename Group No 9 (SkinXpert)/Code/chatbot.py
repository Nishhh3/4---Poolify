# import tkinter as tk
# from tkinter import ttk, filedialog, scrolledtext
# import os
# from PIL import Image, ImageTk
# import re

# class SkincareChatbot:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Skincare Assistant")
#         self.root.geometry("1200x700")  # Full HP Victus screen size
        
#         # Sage green color scheme
#         self.colors = {
#             'bg': '#DAEBD5',  # Light sage green
#             'button': '#739E82',  # Medium sage green
#             'highlight': '#4F6F5A',  # Dark sage green
#             'text': '#2D3F33',  # Very dark sage green
#             'white': '#FFFFFF'  # White
#         }
        
#         self.root.configure(bg=self.colors['bg'])
        
#         # Create the skincare Q&A database
#         self.qa_database = {
#             "what products should i use for acne?": 
#                 "For acne, look for products with salicylic acid, benzoyl peroxide, or retinoids. A gentle cleanser, non-comedogenic moisturizer, and SPF are essential. Consider a spot treatment for breakouts.",
            
#             "how can i reduce redness on my face?": 
#                 "To reduce facial redness, try products with niacinamide, azelaic acid, or centella asiatica. Avoid hot water, harsh exfoliants, and triggers like alcohol or spicy foods. Always use SPF and consider a green-tinted primer.",
            
#             "what's the best way to deal with dry skin?": 
#                 "For dry skin, use a gentle, hydrating cleanser and apply moisturizer on damp skin. Look for ingredients like hyaluronic acid, glycerin, ceramides, and squalane. Consider using a humidifier and avoid hot showers.",
            
#             "how can i get rid of dark spots?": 
#                 "To fade dark spots, use ingredients like vitamin C, niacinamide, alpha arbutin, or tranexamic acid. Exfoliate regularly with AHAs, wear SPF daily, and be patient as results take time.",
            
#             "what's a good skincare routine for beginners?": 
#                 "A basic skincare routine includes: 1) Gentle cleanser 2) Moisturizer 3) Sunscreen (morning). Add a treatment product based on your skin concerns once you're consistent with the basics.",
            
#             "how often should i exfoliate?": 
#                 "Exfoliation frequency depends on your skin type and the product used. Generally, 1-3 times weekly for chemical exfoliants, 1-2 times weekly for physical scrubs. If your skin becomes irritated, reduce frequency.",
            
#             "do i really need to wear sunscreen every day?": 
#                 "Yes, daily sunscreen is essential even on cloudy days and indoors. UV rays cause premature aging and increase skin cancer risk. Use at least SPF 30 as the final step of your morning routine.",
            
#             "what causes cystic acne and how can i treat it?": 
#                 "Cystic acne is caused by hormones, genetics, and bacteria. Treatment options include retinoids, antibiotics, or hormonal treatments prescribed by a dermatologist. Don't squeeze cysts as this can worsen scarring.",
            
#             "how can i minimize pores?": 
#                 "Pores can't permanently shrink, but their appearance can be minimized with regular cleansing, chemical exfoliants (BHAs), niacinamide, retinoids, and clay masks. Keep skin hydrated and always wear sunscreen.",
            
#             "what ingredients should i avoid if i have sensitive skin?": 
#                 "Sensitive skin should avoid fragrance, alcohol, essential oils, harsh sulfates, chemical sunscreens, and high concentrations of active ingredients like retinol or glycolic acid. Patch test new products.",
            
#             "how do i know my skin type?": 
#                 "Cleanse face, wait 30 minutes without applying products. If skin feels tight, you likely have dry skin. If shiny all over, likely oily. If only T-zone is oily, you have combination skin. Redness/itching suggests sensitive skin.",
            
#             "what's the right order to apply skincare products?": 
#                 "General rule: thinnest to thickest texture. Morning: cleanser → toner → serum → eye cream → moisturizer → sunscreen. Evening: cleanser → toner → treatments/serums → eye cream → moisturizer/night cream.",
            
#             "can diet affect my skin?": 
#                 "Yes, diet can impact skin. High glycemic foods and dairy may trigger acne in some people. Foods rich in antioxidants, omega-3s, and vitamins A, C, and E can support skin health. Stay hydrated for optimal skin function.",
            
#             "how can i prevent wrinkles?": 
#                 "Prevent wrinkles by using daily sunscreen, incorporating retinoids, using antioxidants like vitamin C, staying hydrated, not smoking, getting adequate sleep, and maintaining a healthy diet rich in antioxidants.",
            
#             "what's the best treatment for under-eye dark circles?": 
#                 "For under-eye circles, try products with caffeine, vitamin K, retinol, or vitamin C. Use a hydrating eye cream, get adequate sleep, stay hydrated, and wear sunglasses. Concealer can help camouflage as you treat.",
            
#             "how should i treat skin during pregnancy?": 
#                 "During pregnancy, avoid retinoids, high-dose salicylic acid, hydroquinone, and certain essential oils. Safe ingredients include glycolic acid (in low percentages), vitamin C, hyaluronic acid, and niacinamide.",
            
#             "what can help with oily skin?": 
#                 "For oily skin, use a gentle foaming cleanser, oil-free moisturizer, and ingredients like niacinamide, salicylic acid, and clay masks. Don't skip moisturizer as dehydration can increase oil production.",
            
#             "how can i deal with hormonal acne?": 
#                 "Hormonal acne responds well to ingredients like salicylic acid and benzoyl peroxide. Consider supplements like zinc or spearmint tea. A dermatologist might prescribe spironolactone or hormonal birth control.",
            
#             "what should my skincare routine include in winter?": 
#                 "Winter skincare should include a gentle cleanser, heavier moisturizer, hydrating serum (with hyaluronic acid), facial oil, and lip balm. Exfoliate less frequently, use a humidifier, and continue using sunscreen.",
            
#             "is it normal for skincare products to sting?": 
#                 "Mild tingling can be normal with active ingredients like AHAs or vitamin C, but persistent stinging, burning, or redness indicates irritation. Discontinue use of products causing discomfort and simplify your routine."
#         }
        
#         # Create main frames
#         self.create_frames()
        
#         # Create header
#         self.create_header()
        
#         # Create chat area
#         self.create_chat_area()
        
#         # Create input area
#         self.create_input_area()
        
#         # Create image upload area
#         self.create_image_upload_area()
        
#         # Initialize chat with welcome message
#         self.update_chat("Skincare Assistant", "Hello! I'm your skincare assistant. How can I help you today? You can ask me questions about skincare or upload an image for analysis.")
    
#     def create_frames(self):
#         # Left frame for chat
#         self.left_frame = tk.Frame(self.root, bg=self.colors['bg'])
#         self.left_frame.place(relx=0, rely=0, relwidth=0.7, relheight=1)
        
#         # Right frame for image upload
#         self.right_frame = tk.Frame(self.root, bg=self.colors['bg'])
#         self.right_frame.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)
    
#     def create_header(self):
#         header_frame = tk.Frame(self.left_frame, bg=self.colors['highlight'])
#         header_frame.place(relx=0, rely=0, relwidth=1, relheight=0.1)
        
#         header_label = tk.Label(
#             header_frame, 
#             text="Skincare Assistant", 
#             bg=self.colors['highlight'],
#             fg=self.colors['white'],
#             font=("Helvetica", 24, "bold")
#         )
#         header_label.pack(pady=15)
    
#     def create_chat_area(self):
#         chat_frame = tk.Frame(self.left_frame, bg=self.colors['bg'])
#         chat_frame.place(relx=0.05, rely=0.12, relwidth=0.9, relheight=0.68)
        
#         self.chat_display = scrolledtext.ScrolledText(
#             chat_frame,
#             bg=self.colors['white'],
#             fg=self.colors['text'],
#             font=("Helvetica", 12),
#             wrap=tk.WORD,
#             state='disabled'
#         )
#         self.chat_display.pack(fill=tk.BOTH, expand=True)
    
#     def create_input_area(self):
#         input_frame = tk.Frame(self.left_frame, bg=self.colors['bg'])
#         input_frame.place(relx=0.05, rely=0.82, relwidth=0.9, relheight=0.15)
        
#         self.user_input = tk.Text(
#             input_frame,
#             bg=self.colors['white'],
#             fg=self.colors['text'],
#             font=("Helvetica", 12),
#             height=3,
#             wrap=tk.WORD
#         )
#         self.user_input.pack(fill=tk.BOTH, expand=True, pady=5)
        
#         button_frame = tk.Frame(input_frame, bg=self.colors['bg'])
#         button_frame.pack(fill=tk.X, pady=5)
        
#         send_button = tk.Button(
#             button_frame,
#             text="Send",
#             bg=self.colors['button'],
#             fg=self.colors['white'],
#             font=("Helvetica", 12, "bold"),
#             relief=tk.FLAT,
#             command=self.process_user_input
#         )
#         send_button.pack(side=tk.RIGHT, padx=10)
        
#         clear_button = tk.Button(
#             button_frame,
#             text="Clear",
#             bg=self.colors['button'],
#             fg=self.colors['white'],
#             font=("Helvetica", 12),
#             relief=tk.FLAT,
#             command=self.clear_input
#         )
#         clear_button.pack(side=tk.RIGHT, padx=10)
        
#         # Bind Enter key to send message
#         self.user_input.bind("<Return>", lambda event: self.process_user_input())
    
#     def create_image_upload_area(self):
#         # Title for the image section
#         image_title = tk.Label(
#             self.right_frame,
#             text="Skin Analysis",
#             bg=self.colors['highlight'],
#             fg=self.colors['white'],
#             font=("Helvetica", 18, "bold"),
#             pady=10
#         )
#         image_title.pack(fill=tk.X)
        
#         # Frame for the image
#         self.image_frame = tk.Frame(self.right_frame, bg=self.colors['bg'])
#         self.image_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
#         self.image_label = tk.Label(
#             self.image_frame,
#             text="Upload an image of your skin concern",
#             bg=self.colors['bg'],
#             fg=self.colors['text'],
#             font=("Helvetica", 12),
#             wraplength=250
#         )
#         self.image_label.pack(fill=tk.BOTH, expand=True)
        
#         # Upload button
#         upload_button = tk.Button(
#             self.right_frame,
#             text="Upload Image",
#             bg=self.colors['button'],
#             fg=self.colors['white'],
#             font=("Helvetica", 12, "bold"),
#             relief=tk.FLAT,
#             command=self.upload_image
#         )
#         upload_button.pack(pady=20)
        
#         # Analysis result section
#         self.analysis_frame = tk.Frame(self.right_frame, bg=self.colors['bg'])
#         self.analysis_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
#         self.analysis_label = tk.Label(
#             self.analysis_frame,
#             text="Skin analysis will appear here after upload",
#             bg=self.colors['bg'],
#             fg=self.colors['text'],
#             font=("Helvetica", 12),
#             wraplength=250,
#             justify=tk.LEFT
#         )
#         self.analysis_label.pack(fill=tk.BOTH, expand=True)
    
#     def upload_image(self):
#         file_path = filedialog.askopenfilename(
#             filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp")]
#         )
        
#         if file_path:
#             try:
#                 # Open and resize image
#                 image = Image.open(file_path)
#                 image = image.resize((250, 250), Image.LANCZOS)
#                 photo = ImageTk.PhotoImage(image)
                
#                 # Update image display
#                 self.image_label.config(image=photo, text="")
#                 self.image_label.image = photo  # Keep a reference
                
#                 # Get file name for reference
#                 file_name = os.path.basename(file_path)
                
#                 # Simulate analysis
#                 self.perform_skin_analysis(file_name)
                
#                 # Add to chat
#                 self.update_chat("You", f"I've uploaded an image for skin analysis: {file_name}")
#                 self.update_chat("Skincare Assistant", f"I've analyzed your skin image ({file_name}). You can see the results in the analysis panel.")
                
#             except Exception as e:
#                 self.update_chat("Skincare Assistant", f"Sorry, there was an error processing your image: {str(e)}")
    
#     def perform_skin_analysis(self, file_name):
#         # This is a simulated analysis - in a real app, you'd integrate with ML/AI
#         import random
        
#         skin_types = ["Normal", "Dry", "Oily", "Combination", "Sensitive"]
#         concerns = ["Acne", "Redness", "Dryness", "Hyperpigmentation", "Fine lines", "Enlarged pores"]
        
#         selected_type = random.choice(skin_types)
#         selected_concerns = random.sample(concerns, k=random.randint(1, 3))
        
#         analysis_text = f"Skin Analysis Results:\n\n" \
#                        f"Detected Skin Type: {selected_type}\n\n" \
#                        f"Detected Concerns:\n"
        
#         for concern in selected_concerns:
#             analysis_text += f"• {concern}\n"
        
#         analysis_text += "\nRecommended Ingredients:\n"
        
#         if "Acne" in selected_concerns:
#             analysis_text += "• Salicylic Acid\n• Benzoyl Peroxide\n"
#         if "Redness" in selected_concerns:
#             analysis_text += "• Niacinamide\n• Centella Asiatica\n"
#         if "Dryness" in selected_concerns:
#             analysis_text += "• Hyaluronic Acid\n• Ceramides\n"
#         if "Hyperpigmentation" in selected_concerns:
#             analysis_text += "• Vitamin C\n• Alpha Arbutin\n"
#         if "Fine lines" in selected_concerns:
#             analysis_text += "• Retinol\n• Peptides\n"
#         if "Enlarged pores" in selected_concerns:
#             analysis_text += "• BHA\n• Clay\n"
        
#         self.analysis_label.config(text=analysis_text)
    
#     def process_user_input(self):
#         user_message = self.user_input.get("1.0", tk.END).strip()
#         if user_message:
#             self.update_chat("You", user_message)
#             self.get_bot_response(user_message)
#             self.clear_input()
    
#     def get_bot_response(self, user_message):
#         # Convert to lowercase for matching
#         user_message_lower = user_message.lower()
        
#         # Check if we have a direct match in our database
#         if user_message_lower in self.qa_database:
#             response = self.qa_database[user_message_lower]
#             self.update_chat("Skincare Assistant", response)
#             return
        
#         # Check for keyword matches
#         best_match = None
#         highest_score = 0
        
#         for question, answer in self.qa_database.items():
#             # Simple keyword matching algorithm
#             words = set(re.findall(r'\b\w+\b', user_message_lower))
#             question_words = set(re.findall(r'\b\w+\b', question))
            
#             # Calculate match score based on word overlap
#             common_words = words.intersection(question_words)
#             if common_words:
#                 score = len(common_words) / len(question_words)
#                 if score > highest_score:
#                     highest_score = score
#                     best_match = answer
        
#         # If we found a reasonable match (threshold can be adjusted)
#         if highest_score > 0.3:
#             self.update_chat("Skincare Assistant", best_match)
#         else:
#             self.update_chat("Skincare Assistant", "I'm not sure about that. Could you rephrase your question? Common topics include acne, dry skin, skincare routines, specific ingredients, or skin types.")
    
#     def update_chat(self, sender, message):
#         self.chat_display.config(state='normal')
        
#         # Format based on sender
#         if sender == "You":
#             self.chat_display.insert(tk.END, f"\n{sender}: ", "user")
#             self.chat_display.tag_configure("user", foreground="#375F4C", font=("Helvetica", 12, "bold"))
#         else:
#             self.chat_display.insert(tk.END, f"\n{sender}: ", "bot")
#             self.chat_display.tag_configure("bot", foreground="#4F6F5A", font=("Helvetica", 12, "bold"))
        
#         # Insert the message
#         self.chat_display.insert(tk.END, f"{message}\n")
        
#         # Auto scroll to the bottom
#         self.chat_display.see(tk.END)
#         self.chat_display.config(state='disabled')
    
#     def clear_input(self):
#         self.user_input.delete("1.0", tk.END)

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = SkincareChatbot(root)
#     root.mainloop()

#---------------------------------------------------------new bot2 code------------------------------------------------------------#


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
        
        # Right panel (FAQ and Image Upload) - FIXED: removed width parameter
        self.right_panel = ttk.Frame(self.content_frame, padding=10, width=350)
        self.right_panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=False, padx=10)
        self.right_panel.pack_propagate(False)  # Prevent the frame from shrinking to fit its contents
        
        # FAQ section
        self.faq_label = ttk.Label(self.right_panel, 
                                  text="Common Questions", 
                                  font=("Arial", 16, "bold"))
        self.faq_label.pack(fill=tk.X, pady=10)
        
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
            faq_button = ttk.Button(self.right_panel, 
                                   text=question, 
                                   command=lambda q=question: self.select_faq(q))
            faq_button.pack(fill=tk.X, pady=3)
        
        # Image upload section
        self.upload_label = ttk.Label(self.right_panel, 
                                     text="Upload Skin Image", 
                                     font=("Arial", 16, "bold"))
        self.upload_label.pack(fill=tk.X, pady=(20, 10))
        
        self.upload_button = ttk.Button(self.right_panel, 
                                      text="Choose Image", 
                                      command=self.upload_image)
        self.upload_button.pack(fill=tk.X, pady=5)
        
        self.image_label = ttk.Label(self.right_panel, 
                                    text="No image selected", 
                                    background=self.sage_light)
        self.image_label.pack(pady=10)
        
        self.image_display = ttk.Label(self.right_panel, background=self.sage_light)
        self.image_display.pack(fill=tk.BOTH, expand=True, pady=10)
        
        # Initialize chat with welcome message
        self.display_bot_message("Hello! I'm your skincare assistant. How can I help you today? You can ask me questions or choose from common topics on the right.")
        
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
        
        # Merge the additional Q&A with the existing ones
        self.faq_answers.update(additional_qa)
        
        # Add additional FAQ buttons
        for question in additional_qa.keys():
            faq_button = ttk.Button(self.right_panel, 
                                   text=question, 
                                   command=lambda q=question: self.select_faq(q))
            faq_button.pack(fill=tk.X, pady=3)
    
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
            self.display_bot_message("You can upload an image of your skin by clicking the 'Choose Image' button on the right panel.")
        
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
                
                # Display the image preview
                image = Image.open(file_path)
                image = image.resize((300, 200), Image.LANCZOS)  # Resize for preview
                photo = ImageTk.PhotoImage(image)
                
                self.image_display.config(image=photo)
                self.image_display.image = photo  # Keep reference
                
                # Confirm to user
                self.display_bot_message(f"Image uploaded successfully. I can see your skin concern. What specific questions do you have about the condition shown in the image?")
                
            except Exception as e:
                messagebox.showerror("Error", f"Could not open image: {str(e)}")
    
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