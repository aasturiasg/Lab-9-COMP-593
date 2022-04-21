""" 
COMP 593 - Lab 9

Description: 
  Displays a graphical user interface to select pokemons from a combobox, see their images, and set them as desktop background.

Usage:
  python Pokemon_Image_Viewer.py

Parameters:
  None.

History:
  Date        Author      Description
  2022-04-21  A.Asturias  Initial creation
"""

from tkinter import *
from tkinter import ttk
from pokeinfo import retrieve_pokemon_list, get_image_url
from usefullibrary import download_image, set_background_image
import os
import sys
import ctypes

def main():

    #determine the path of the directory where the script is
    script_directory = sys.path[0]

    #verifies if an images directory already exists, if not, creates it 
    images_directory = os.path.join(script_directory, 'images')
    if not os.path.isdir(images_directory):
        os.mkdir(images_directory)

    #initialize the window with a title
    window = Tk()
    window.title('Image Viewer for Pokemon')

    #set an icon and icon for the taskbar
    script_id = 'Image.Viewer.for.Pokemon'
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(script_id)
    window.iconbitmap(os.path.join(script_directory, 'blue_pokeball.ico'))

    #allow resizing on the window
    window.rowconfigure(0, weight=1)
    window.columnconfigure(0, weight=1)

    #dimensions for the minimum size of the window
    window.minsize(500, 600)

    #instantiate the frame to contain all the elements of the program
    frame = ttk.Frame(window)
    frame.grid(row=0, column=0, sticky=(N,S,E,W))

    #set resizing for the frame
    frame.rowconfigure(0, weight=1)
    frame.columnconfigure(0, weight=1)
    
    #import a default image to the script and display it in a label inside the frame
    pokemon_image = PhotoImage(file=os.path.join(script_directory, 'pokeball.png'))
    image_label = ttk.Label(frame, image=pokemon_image)
    image_label.grid(row=0, column=0, padx=30, pady=(30,10))

    #get a list with all pokemon names
    pokemon_list = retrieve_pokemon_list()
    pokemon_list.sort()

    #instantiate a combobox that lives inside the frame and displays all pokemon names
    pokemon_combobox = ttk.Combobox(frame, values=pokemon_list, state='readonly')
    pokemon_combobox.set('Choose a Pokemon')
    pokemon_combobox.grid(row=1, column=0, padx=30, pady=10)

    #function to call when an item is selected in the combobox
    def handle_combobox(event):

        """
        Downloads and displays a specified pokemon's image in the PhotoImage object.

        :param event: event information
        :returns: None
        """

        #gets pokemon name and url
        pokemon_name = pokemon_combobox.get()
        pokemon_image_url = get_image_url(pokemon_name.lower())

        #builds the path to save the pokemon image
        pokemon_image_path = os.path.join(images_directory, pokemon_name + '.png')

        #downloads the pokemon image to the local drive and displays it in the PhotoImage object
        download_image(pokemon_image_url, pokemon_image_path)
        pokemon_image['file'] = pokemon_image_path

        #enable the button
        set_background_button.state(['!disabled'])

    #tell the combobox to listen for selected items and call the handle_combobox function
    pokemon_combobox.bind('<<ComboboxSelected>>', handle_combobox)

    #function to call when the button is clicked
    def handle_button():

        """
        Sets the desktop background to the pokemon's image.

        :returns: None
        """

        #get the pokemon's name
        pokemon_name = pokemon_combobox.get()

        #build the path to where the image is expected to be stored
        pokemon_image_path = os.path.join(images_directory, pokemon_name + '.png')

        #set the desktop background to the image specified by the path
        set_background_image(pokemon_image_path)

    #instantiate the button and the funtion to call when it is clicked
    set_background_button = ttk.Button(frame, text='Set as Desktop Background', command=handle_button)

    #disable the button and position it in the frame
    set_background_button.state(['disabled'])
    set_background_button.grid(row=2, column=0, padx=30, pady=(10,30))

    #infinite loop to display the window and look for events
    window.mainloop()


main()
