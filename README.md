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
Planned improvements:

- Error handling: The current implementation assumes that the cat will not walk on the keyboard.

- Face detection accuracy: The current implementation uses a basic cat face detection algorithm, but does not attempt to detect cat emotions.

- User interface: The current implementation does not save a history of watched videos. Some owners may want to set the scroll on infinite while they're at work then rewatch favorite TikToks with their cat as a way of asking, so how was your day?

- Additional interactivity: The current implementation only plays Tiktoks when the cat is looking at the screen. Adding more interactivity, such as allowing the cat to swipe to the next Tiktok by moving its paw, would make the experience more engaging for the cat.




