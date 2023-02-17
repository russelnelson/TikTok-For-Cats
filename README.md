# TikTok-For-Cats
Code that lets a cat control TikTok using facial recognition. This provides your cat with entertainment but more importantly, allows you to learn its likes and dislikes.

Requires:
- Computer with a web camera
- Cat
- TikTok account for cat

How it works:
- It uses OpenCV to detect the cat's proximity and open TikTok
- It scrolls through TikTok until the cat looks at the screen, then plays the current video
- If the cat looks away, it returns to scrolling
- Unlike human TikTok, it stops scrolling after a maximum number of TikToks (default = 10)

Note:
- The face detection may not be perfect and may need some tweaking depending on the lighting and other factors in the room, like 2+ cats

# Roadmap
+Planned improvements:

Adding error handling: The current implementation assumes that everything will work perfectly. However, in reality, there could be unexpected errors, such as the camera not working or the web page not loading properly. Adding error handling will make the code more robust and prevent it from crashing.

Making the code more modular: The current implementation is a single, monolithic script. This makes it difficult to understand and maintain. By breaking it up into smaller, more manageable functions, it will be easier to understand and modify.

Making the face detection more accurate: The current implementation uses a basic face detection algorithm, which may not work well in all lighting conditions or with all types of cats. Improving the accuracy of the face detection algorithm will make the code more reliable.

Adding user settings: The current implementation has hard-coded values for the screen coordinates and the number of Tiktoks to play. Adding a settings file or a user interface would make it easier for the user to customize these values.

Adding more interactivity: The current implementation only plays Tiktoks when the cat is looking at the screen. Adding more interactivity, such as allowing the cat to swipe to the next Tiktok by moving its paw, would make the experience more engaging for the cat.

Improving performance: The current implementation is not optimized for performance, and may be slow or resource-intensive. Improving performance will make the code more responsive and efficient. This could involve optimizing the face detection algorithm, using a more lightweight web browser, or running the code on a faster computer.




