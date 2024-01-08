import tkinter as tk
from tkinter import filedialog
from moviepy.video.io.VideoFileClip import VideoFileClip

class VideoEditorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Video Editor")

        # Variables for video processing
        self.video_path = None
        self.video_duration = None

        # File upload button
        tk.Button(root, text="Upload Video", command=self.upload_video).pack(pady=20)

        # Duration input field
        tk.Label(root, text="Enter cut duration (in seconds):").pack()
        self.duration_entry = tk.Entry(root)
        self.duration_entry.pack(pady=10)

        # Cut button
        tk.Button(root, text="Cut Video", command=self.cut_video).pack(pady=20)

    def upload_video(self):
        """
        Open a file dialog to upload a video file.
        """
        self.video_path = filedialog.askopenfilename(title="Select a Video File", filetypes=[("Video Files", "*.mp4;*.avi;*.mov")])

        if self.video_path:
            video_clip = VideoFileClip(self.video_path)
            self.video_duration = video_clip.duration
            video_clip.close()
            tk.messagebox.showinfo("Video Information", f"Video Duration: {self.video_duration:.2f} seconds")

    def cut_video(self):
        """
        Cut the video according to the user's specified duration and save the cut episodes.
        """
        if not self.video_path:
            tk.messagebox.showerror("Error", "Please upload a video first.")
            return

        try:
            cut_duration = float(self.duration_entry.get())
        except ValueError:
            tk.messagebox.showerror("Error", "Invalid duration. Please enter a valid number.")
            return

        if cut_duration <= 0 or cut_duration > self.video_duration:
            tk.messagebox.showerror("Error", f"Invalid duration. Enter a value between 0 and {self.video_duration} seconds.")
            return

        video_clip = VideoFileClip(self.video_path)
        num_cuts = int(self.video_duration // cut_duration)

        for i in range(num_cuts):
            start_time = i * cut_duration
            end_time = min((i + 1) * cut_duration, self.video_duration)

            cut_clip = video_clip.subclip(start_time, end_time)
            cut_clip.write_videofile(f"cut_episode_{i + 1}.mp4")
            cut_clip.close()

        video_clip.close()
        tk.messagebox.showinfo("Success", "Video cutting complete. Check the saved episodes in the folder.")

if __name__ == "__main__":
    root = tk.Tk()
    app = VideoEditorApp(root)
    root.mainloop()
