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
