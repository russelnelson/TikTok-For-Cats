import cv2
import pyautogui
import webbrowser

# Open TikTok website
webbrowser.open('https://www.tiktok.com/')

# Set up the camera
cap = cv2.VideoCapture(0)

# Set up initial variables
cat_present = False
cat_looks_at_screen = False
current_tiktok = 0

# Loop through frames from the camera
while True:
    # Read a frame from the camera
    ret, frame = cap.read()

    # Convert the frame to grayscale and apply a blur
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)

    # Detect faces in the frame
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalcatface_extended.xml')
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # If a cat is present, set cat_present to True and check if it's looking at the screen
    if len(faces) > 0:
        cat_present = True

        # Check if the cat is looking at the screen
        for (x, y, w, h) in faces:
            if x < 200 and y < 200:
                cat_looks_at_screen = True
                break
            else:
                cat_looks_at_screen = False

    # If a cat is not present, set cat_present to False and reset cat_looks_at_screen
    else:
        cat_present = False
        cat_looks_at_screen = False

    # If the cat is present and looking at the screen, play the current Tiktok
    if cat_present and cat_looks_at_screen:
        if current_tiktok == 0:
            # Click the play button to start the first Tiktok
            pyautogui.click(700, 600)
        else:
            # Swipe to the next Tiktok
            pyautogui.drag(0, -200, duration=0.5)
        current_tiktok += 1

    # If the cat is not looking at the screen, swipe to the next Tiktok
    if not cat_looks_at_screen:
        pyautogui.drag(0, -200, duration=0.5)
        current_tiktok += 1

    # Exit the loop if the cat has watched enough Tiktoks
    if current_tiktok == 10:
        break

# Release the camera and close the browser
cap.release()
webbrowser.close()
