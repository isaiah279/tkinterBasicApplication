from tkinter import *
import pygame

root = Tk()
root.title("Okech@ChiorMusicPlayer")
# root.iconbitmap(" ")
# intializing pygame mixer
pygame.mixer.init()
#add somng
def add_song():
    pass


# create playlist Box
song_box_list = Listbox(root, bg="black", fg="green",width=100 )
song_box_list.pack()
# create player control buttons
back_btn = PhotoImage(file='icons8-back-64.png')
fowrd_btn = PhotoImage(file='icons8-forward-64.png')
play_btn = PhotoImage(file='icons8-play-64.png')
pause_bt = PhotoImage(file='icons8-pause-50.png')
stop_btn = PhotoImage(file='icons8-stop-64.png')


# create claear control frames
controls_frame = Frame(root)
controls_frame.pack()
# create player controls
back_button = Button(controls_frame, image=back_btn, borderwidth=0)
forward_button = Button(controls_frame, image=fowrd_btn, borderwidth=0)
play_button = Button(controls_frame, image=play_btn, borderwidth=0)
pause_button = Button(controls_frame, image=pause_bt, borderwidth=0)
stop_button = Button(controls_frame, image=stop_btn, borderwidth=0)

back_button.grid(row=0, column=0,padx=10)
forward_button.grid(row=0, column=1,padx=10)
play_button.grid(row=0, column=2,padx=10)
pause_button.grid(row=0, column=3,padx=10)
stop_button.grid(row=0, column=4,padx=10)

#creating meue
my_menu=Menu(root)
#adding song menue
add_song_menu=Menu(my_menu)
my_menu.add_cascade(label="Add songs",menu=add_song_menu)
add_song_menu.add_command(label="Add One song To play list",command=add_song)
root.mainloop()
