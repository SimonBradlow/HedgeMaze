# Hedge Maze ![Python](https://img.shields.io/badge/Python-3776AB.svg?style=flat&logo=Python&logoColor=white)

A simple raycasting-based game where the user navigates a hedge maze. <br>
Implemented in Python with Pygame, CRT shader implemented using ModernGL fragment shaders<br>

![](https://github.com/SimonBradlow/HedgeMaze/blob/main/resources/maze.gif)

### Project file structure:
- **main.py:** The main loop of the game
- **player.py:** Boiler-plate player class with functionality for WASD movement, mouse control for the camera, and wall collision
- **map.py:** Basic script file storing the map as a matrix of characters denoting walls
- **settings.py:** Basic script file containing global configuration variables for the game, player and raycasting engine
- **raycasting.py:** Uses the position of the main games player object to cast rays outward to collect distance data, and then renders the wall textures accordingly
- **object_renderer.py:** Allows for the inclusion of static sprite objects, as well as handles the background image. Contains functionality for loading in textures
- **fragment.glsl:** Fragment shaders used by the main program to implement the CRT-like fisheye shader

### Tutorials referenced:
**@blubberquark** (Tumblr) - [Using modernGL for post-processing shaders with PyGame](https://blubberquark.tumblr.com/post/185013752945/embed) <br>
**@Coder Space** (YouTube) - [Creating a DOOM (Wolfenstein) - style 3D Game in Python](https://www.youtube.com/watch?v=ECqUrT7IdqQ&t=469s)
