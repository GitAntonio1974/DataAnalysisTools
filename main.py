import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import pandas as pd
import threading
import time

class TelemetryLoader:
    def __init__(self, root):
        self.root = root
        self.root.title('Telemetry Data Loader')
        self.channels = ['Speed', 'Engine_RPM', 'Throttle', 'Brake', 'Steering_Angle']
        self.progress_var = tk.DoubleVar()
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.root, text='Load Telemetry Data')
        self.label.pack(pady=10)

        self.load_button = tk.Button(self.root, text='Load Data', command=self.load_data)
        self.load_button.pack(pady=10)

        self.export_button = tk.Button(self.root, text='Export to CSV', command=self.export_data)
        self.export_button.pack(pady=10)

        self.progress = tk.Progressbar(self.root, variable=self.progress_var, maximum=100)
        self.progress.pack(pady=10)

    def load_data(self):
        file_path = filedialog.askopenfilename(title='Select Telemetry File', filetypes=[('Text Files', '*.txt')])
        if file_path:
            self.load_thread = threading.Thread(target=self.read_data, args=(file_path,))
            self.load_thread.start()

    def read_data(self, file_path):
        self.progress_var.set(0)
        total_samples = 5000
        for i in range(total_samples):
            time.sleep(0.01)  # Simulating data loading from the file
            self.progress_var.set((i + 1) / total_samples * 100)
        messagebox.showinfo('Info', 'Data Loaded Successfully!')

    def export_data(self):
        save_path = filedialog.asksaveasfilename(title='Save CSV', defaultextension='.csv', filetypes=[('CSV Files', '*.csv')])
        if save_path:
            # Simulated data export, in a real implementation we would use loaded data
            dummy_data = {channel: [0] * 5000 for channel in self.channels}
            df = pd.DataFrame(dummy_data)
            df.to_csv(save_path, index=False)
            messagebox.showinfo('Info', 'Data Exported Successfully!')

if __name__ == '__main__':
    root = tk.Tk()
    app = TelemetryLoader(root)
    root.mainloop()