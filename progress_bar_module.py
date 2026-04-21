import tkinter as tk

class ProgressBar:
    def __init__(self, root):
        self.root = root
        self.root.title('Progress Bar')
        self.progress = tk.IntVar()

        # Create a progress bar
        self.progress_bar = tk.Progressbar(self.root, variable=self.progress, maximum=100)
        self.progress_bar.pack(pady=20)

        # Create a label to show percentage
        self.label = tk.Label(self.root, text='0%')
        self.label.pack(pady=10)

    def update_progress(self, value):
        self.progress.set(value)
        self.label.config(text=f'{value}%')
        self.root.update_idletasks()  # Update the UI to reflect changes

    def start_loading(self):
        for i in range(0, 101, 10):  # Increments of 10%
            self.update_progress(i)
            self.root.after(500)  # Simulate some work being done

# Example of using the ProgressBar class
if __name__ == '__main__':
    root = tk.Tk()
    progress_bar = ProgressBar(root)
    progress_bar.start_loading()  # Start loading simulation
    root.mainloop()