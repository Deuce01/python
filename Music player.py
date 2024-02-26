import pygame

def play_music(file):
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()

def stop_music():
    pygame.mixer.music.stop()

def pause_music():
    pygame.mixer.music.pause()

def unpause_music():
    pygame.mixer.music.unpause()

# Example usage:
file_path = "example_song.mp3"  # Replace with your own file path
play_music(file_path)

# You can add more functionality as needed, such as a user interface for controlling the player.
