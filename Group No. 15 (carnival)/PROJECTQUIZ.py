    import tkinter as tk
    from tkinter import messagebox, ttk
    import mysql.connector

    # Connect to MySQL database
    conn = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="anish123",
        database="quizapp"
    )
    cursor = conn.cursor()

    # -------------------- LOGIN PAGE --------------------
    def login_window():
        root = tk.Tk()
        root.title("Quiz App - Login")
        root.geometry("400x300")
        root.configure(bg="#f0f8ff")

        tk.Label(root, text="🎓 Quiz App Login", font=("Helvetica", 20, "bold"), bg="#f0f8ff", fg="#333").pack(pady=20)

        tk.Label(root, text="Username", font=("Arial", 12), bg="#f0f8ff").pack()
        username_entry = tk.Entry(root, width=30)
        username_entry.pack(pady=5)

        tk.Label(root, text="Password", font=("Arial", 12), bg="#f0f8ff").pack()
        password_entry = tk.Entry(root, width=30, show="*")
        password_entry.pack(pady=5)

        def login():
            username = username_entry.get()
            password = password_entry.get()

            cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
            user = cursor.fetchone()

            if user:
                root.destroy()
                start_quiz()
            else:
                messagebox.showerror("Error", "Invalid username or password")

        tk.Button(root, text="Login", font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", command=login).pack(pady=20)

        root.mainloop()

    # -------------------- QUIZ PAGE --------------------
    def start_quiz():
        cursor.execute("SELECT * FROM questions")
        questions = cursor.fetchall()

        q_index = [0]
        score = [0]

        quiz = tk.Tk()
        quiz.title("Quiz App")
        quiz.geometry("600x500")
        quiz.configure(bg="white")

        question_var = tk.StringVar()
        options_var = [tk.StringVar() for _ in range(4)]
        selected = tk.IntVar()

        question_label = tk.Label(quiz, textvariable=question_var, font=("Helvetica", 16, "bold"), wraplength=550, bg="white", fg="#333")
        question_label.pack(pady=30)

        question_count_label = tk.Label(quiz, text="", font=("Arial", 12), bg="white", fg="#777")
        question_count_label.pack()

        radio_buttons = []
        for i in range(4):
            rb = tk.Radiobutton(
                quiz, textvariable=options_var[i], variable=selected, value=i+1,
                font=("Arial", 12), bg="white", anchor="w", padx=20
            )
            rb.pack(fill='x', padx=60, pady=2)
            radio_buttons.append(rb)

        feedback_label = tk.Label(quiz, text="", font=("Arial", 12, "bold"), bg="white")
        feedback_label.pack(pady=10)

        progress = ttk.Progressbar(quiz, orient='horizontal', length=400, mode='determinate')
        progress.pack(pady=10)

        def load_question():
            if q_index[0] < len(questions):
                q = questions[q_index[0]]
                question_var.set(q[1])
                for i in range(4):
                    options_var[i].set(q[i + 2])
                question_count_label.config(text=f"Question {q_index[0] + 1} of {len(questions)}")
                selected.set(0)
                feedback_label.config(text="", fg="black")
                progress["value"] = (q_index[0] / len(questions)) * 100
            else:
                show_result()

        def move_to_next():
            q_index[0] += 1
            load_question()

        def next_question():
            if selected.get() == 0:
                messagebox.showwarning("Select an option", "Please choose an answer!")
                return

            correct_ans = questions[q_index[0]][6]
            if selected.get() == correct_ans:
                score[0] += 1
                feedback_label.config(text="✅ Correct!", fg="green")
            else:
                correct_option = questions[q_index[0]][1 + correct_ans]
                feedback_label.config(text=f"❌ Incorrect! Correct answer: {correct_option}", fg="red")

            quiz.after(1000, lambda: move_to_next())

        next_btn = tk.Button(quiz, text="Next", font=("Arial", 12, "bold"), bg="#2196F3", fg="white", command=next_question)
        next_btn.pack(pady=20)

        def show_result():
            for widget in quiz.winfo_children():
                widget.destroy()

            tk.Label(quiz, text="🎉 Quiz Completed!", font=("Helvetica", 22, "bold"), bg="white", fg="green").pack(pady=40)
            tk.Label(quiz, text=f"Your Score: {score[0]} / {len(questions)}", font=("Helvetica", 16), bg="white").pack(pady=20)

            tk.Button(quiz, text="Logout", font=("Arial", 12, "bold"), bg="red", fg="white", command=quiz.destroy).pack(pady=30)

        load_question()
        quiz.mainloop()

    # Start app
    login_window()
