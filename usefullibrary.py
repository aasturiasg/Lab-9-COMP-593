from requests import get
import ctypes

def download_image(image_url, local_path):

    """
    Obtains an image from the URL provided and saves it to a specified local path.

    :param image_url: URL of the image to be downloaded
    :param local_path: path where the image must be saved, including the image's name and extension
    :returns: None
    """

    print('Downloading pokemon image from URL...', end=' ')

    #obtain a response from the image url
    response_message = get(image_url)

    #if get was successful save the binary string to a file
    if response_message.status_code == 200:
        with open(local_path, 'wb') as image_file:
            image_file.write(response_message.content)
        print('done!')

    #for any other scenario, display the response code and stop the script
    else:
        print('unexpected error encountered. Response code: ' + str(response_message.status_code))
        exit('Stopping script...')

def set_background_image(image_path):

    """
    Sets the current desktop background to a specified image, using its path.

    :param image_path: path of the image wanted for background
    :returns: None
    """

    print('Setting background image...', end=' ')

    #set the desktop background to be the specified image
    ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 0)

    print('done!')