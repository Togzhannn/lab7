import pygame
import os

# Initialize pygame mixer
pygame.mixer.init()

# List of music files in your folder
music_files = [
    "Jahzzar - MainSquare.mp3",  # Existing track
    "Ketsa - Better-Days-Ahead.mp3",  # New track added
]
current_track_index = 0

# Play the current track
def play_music():
    pygame.mixer.music.load(music_files[current_track_index])
    pygame.mixer.music.play()

# Stop the current track
def stop_music():
    pygame.mixer.music.stop()

# Go to the next track
def next_track():
    global current_track_index
    current_track_index = (current_track_index + 1) % len(music_files)
    play_music()

# Go to the previous track
def previous_track():
    global current_track_index
    current_track_index = (current_track_index - 1) % len(music_files)
    play_music()

# Initialize Pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Simple Music Player")

# Play the first track
play_music()

# Start the main loop
running = True
while running:
    screen.fill((255, 255, 255))  # Optional: Clear screen with white
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:  # 'P' key to play
                if not pygame.mixer.music.get_busy():
                    play_music()
            elif event.key == pygame.K_s:  # 'S' key to stop
                stop_music()
            elif event.key == pygame.K_n:  # 'N' key to next track
                next_track()
            elif event.key == pygame.K_b:  # 'B' key to previous track
                previous_track()

# Quit the Pygame mixer and close the program
pygame.quit()
