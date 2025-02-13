import tkinter as tk
from tkinter import messagebox
from quizApp import questions

class QuizApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Online Quiz System")
        self.master.geometry("600x600")  # Set the window size
        self.master.configure(bg='#336c99')

        self.welcome_label = tk.Label(master, text="ⓄⓃⓁⒾⓃⒺ       ⓆⓊⒾⓏ     ⒶⓅⓅⓁⒾⒸⒶⓉⒾⓄⓃ", font=("Arial", 6, "bold"), bg="#ffcc3b", fg="black", width=55, height=3)
        self.welcome_label.pack(pady=(0))
        
        self.bottom_frame = tk.Frame(master, bg='#ffcc3b')
        self.bottom_frame.pack(side=tk.BOTTOM, fill=tk.X)

        self.bottom_label = tk.Label(master, text="", font=("Arial", 6, "bold"), bg="#ffcc3b", fg="black", width=55, height=3)
        self.bottom_label.pack(side=tk.BOTTOM, fill=tk.X)
       
        self.welcome_frame = tk.Frame(master, bg='#ffcc3b')
        self.welcome_frame.place(relx=0.5, rely=0.5, anchor='center')
        
        self.welcome_message = tk.Label(self.welcome_frame, text="Start to Continue", font=("Times New Roman", 10), bg="#ffcc3b", fg="black", height=2, width=20)
        self.welcome_message.pack(pady=0)

        self.start_button = tk.Button(self.welcome_frame, text="Start", command=self.enter_name, font=("Times New Roman", 6), bg="green", fg="white")
        self.start_button.pack(pady=35)

        self.bottom_frame = tk.Frame(master, bg='#ffcc3b')
        self.bottom_frame.pack(side=tk.BOTTOM, fill=tk.X)

    def enter_name(self):
        self.welcome_frame.place_forget()

        self.name_frame = tk.Frame(self.master, bg='#ffcc3b')
        self.name_frame.place(relx=0.5, rely=0.5, anchor='center')

        self.name_label = tk.Label(self.name_frame, text="Enter your name", font=("Times New Roman", 10), bg='#ffcc3b', fg="black", width=20, height=1)
        self.name_label.pack(pady=5)

        self.name_entry = tk.Entry(self.name_frame, font=("Arial", 7),width=18)
        self.name_entry.pack(pady=5)

        self.continue_button = tk.Button(self.name_frame, text="Continue", command=self.start_quiz, font=("Times New Roman", 5), bg="green", fg="white", width=4)
        self.continue_button.pack(pady=20)

    def start_quiz(self):
        self.user_name = self.name_entry.get()  # Get the user's name
        if not self.user_name:
            messagebox.showwarning ("Input Error","Enter your name. ")
            return

        self.name_frame.place_forget()

        self.level_frame = tk.Frame(self.master, bg='#ffcc3b')
        self.level_frame.place(relx=0.5, rely=0.5, anchor='center')

        self.level_label = tk.Label(self.level_frame, text="Select Your Level:", font=("Times New Roman", 10), bg='#ffcc3b', fg="black", height=2, width=20)
        self.level_label.pack(pady=10)

        self.easy_button = tk.Button(self.level_frame, text="Easy", command=lambda: self.start_quiz_level("easy"), font=("Times New Roman", 7), bg='green', fg="white", width=5)
        self.easy_button.pack(pady=10)

        self.medium_button = tk.Button(self.level_frame, text="Medium", command=lambda: self.start_quiz_level("medium"), font=("Times New Roman", 7), bg='green', fg="white", width=5)
        self.medium_button.pack(pady=10)

        self.hard_button = tk.Button(self.level_frame, text="Hard", command=lambda: self.start_quiz_level("hard"), font=("Times New Roman", 7), bg='green', fg="white", width=5)
        self.hard_button.pack(pady=15)

        self.expert_button = tk.Button(self.level_frame, text="Expert", command=lambda: self.start_quiz_level("expert"), font=("Times New Roman", 7), bg='green', fg="white", width=5)
        self.expert_button.pack(pady=15)

    def start_quiz_level(self, level):
        self.level_frame.place_forget()
        self.score = 0
        self.question_index = 0
        self.questions = questions[level]
        self.is_quiz_active = True
        self.show_question()

    def show_question(self):
        if hasattr(self, 'question_frame'):
            self.question_frame.destroy()

        self.question_frame = tk.Frame(self.master)
        self.question_frame.place(relx=0.5, rely=0.5, anchor='center')

        self.question_label = tk.Label(self.question_frame, text="", wraplength=400, font=("Times New Roman", 7), fg="green", width=30)
        self.question_label.pack(pady=20)

        self.var = tk.StringVar()
        self.options_frame = tk.Frame(self.question_frame)
        self.options_frame.pack(pady=10)

        self.option_buttons = []
        for i in range(4):
            btn = tk.Radiobutton(self.options_frame, text="", variable=self.var, value="", font=("Times New Roman", 5), fg="black")
            btn.pack(anchor='w')
            self.option_buttons.append(btn)

        self.back_button = tk.Button(self.question_frame, text="⇦ Back", command=self.previous_question, font=("Times New Roman", 5), bg='red', fg='white', width=4)
        self.back_button.pack(side=tk.LEFT, padx=40, pady=15)

        self.next_button = tk.Button(self.question_frame, text="Next ⇨", command=self.next_question, font=("Times New Roman", 5), bg='green', fg='white', width=4)
        self.next_button.pack(side=tk.RIGHT, padx=40, pady=15)

        self.timer_label = tk.Label(self.question_frame, text="", font=("Times New Roman", 4), fg="red")
        self.timer_label.pack(pady=5)

        self.update_question()
        self.start_timer(15)

    def start_timer(self, duration):
        self.remaining_time = duration
        self.update_timer()

    def update_timer(self):
        if self.is_quiz_active and self.remaining_time > 0:
            self.timer_label.config(text=f"Time left: {self.remaining_time} seconds")
            self.remaining_time -= 1
            self.master.after(2000, self.update_timer)  # Update every 1 second
        elif self.remaining_time == 0:
            self.next_question()

    def update_question(self):
        question = self.questions[self.question_index]
        self.question_label.config(text=question["question"])
        self.var.set(None)

        for i, option in enumerate(question["options"]):
            self.option_buttons[i].config(text=option, value=option)

    def next_question(self):
        if self.var.get() == self.questions[self.question_index]["answer"]:
            self.score += 1

        self.question_index += 1
        if self.question_index < len(self.questions):
            self.update_question()
            self.start_timer(15)
        else:
            self.show_result()

    def previous_question(self):
        if self.question_index > 0:
            self.question_index -= 1
            self.update_question()
            self.start_timer(15)
        else:
            self.show_level_selection()  

    def show_result(self):
        self.is_quiz_active = False
        self.question_frame.destroy()
        result_frame = tk.Frame(self.master, bg='#336c99')
        result_frame.place(relx=0.5, rely=0.5, anchor='center')
        
        # Show the user's score
        score_label = tk.Label(result_frame, text=f"{self.user_name}'s score: {self.score}/{len(self.questions)}", font=("Times New Roman", 10), bg='#336c99', fg="#ffcc3b")
        score_label.pack(pady=2)

        # Display the appropriate message based on the score
        if self.score == len(self.questions):  
            result_label = tk.Label(result_frame, text="Congratulations perfect score!" , font=("Times New Roman", 5), bg='#336c99', fg="white")
        elif self.score == 0: 
            result_label = tk.Label(result_frame, text="Try again?", font=("Times New Roman", 6), bg='#336c99', fg="white")
        else:  
            result_label = tk.Label(result_frame, text="Thank you for trying!", font=("Times New Roman", 5), bg='#336c99', fg="white")
        result_label.pack(pady=2)

        # Restart and Exit buttons
        button_frame = tk.Frame(result_frame, bg='#336c99')
        button_frame.pack(pady=10)

        restart_button = tk.Button(button_frame, text="⇦ Restart", command=self.restart_quiz, font=("Times New Roman", 4), bg="green", fg="white", width=5)
        restart_button.pack(side=tk.LEFT, padx=5)

        exit_button = tk.Button(button_frame, text="Exit ⇨", command=self.confirm_exit, font=("Times New Roman", 4), bg="red", fg="white", width=5)
        exit_button.pack(side=tk.LEFT, padx=5)

    def confirm_exit(self):
        if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
            self.master.quit()

    def exit_app(self):
        self.master.quit()  # Exit the application

    def restart_quiz(self):
        self.enter_name()  # Go back to the name entry screen

    def show_level_selection(self):
        if hasattr(self, 'level_frame'):
            self.level_frame.destroy()

        self.level_frame = tk.Frame(self.master, bg='#ffcc3b')
        self.level_frame.place(relx=0.5, rely=0.5, anchor='center')

        self.level_label = tk.Label(self.level_frame, text="Select Your Level:", font=("Times New Roman", 10), bg='#ffcc3b', fg="black", height=2, width=25)
        self.level_label.pack(pady=10)

        self.easy_button = tk.Button(self.level_frame, text="Easy", command=lambda: self.start_quiz_level("easy"), font=("Times New Roman", 7), bg='green', fg="white", width=5)
        self.easy_button.pack(pady=10)

        self.medium_button = tk.Button(self.level_frame, text="Medium", command=lambda: self.start_quiz_level("medium"), font=("Times New Roman", 7), bg='green', fg="white", width=5)
        self.medium_button.pack(pady=10)

        self.hard_button = tk.Button(self.level_frame, text="Hard", command=lambda: self.start_quiz_level("hard"), font=("Times New Roman", 7), bg='green', fg="white", width=5)
        self.hard_button.pack(pady=10)

        self.expert_button = tk.Button(self.level_frame, text="Expert", command=lambda: self.start_quiz_level("expert"), font=("Times New Roman", 7), bg='green', fg='white', width=5)
        self.expert_button.pack(pady=15)

if __name__ == "__main__":
    root = tk.Tk()
    root.attributes('-fullscreen', True)  # Set the window to full screen
    quiz_app = QuizApp(root)
    root.mainloop()