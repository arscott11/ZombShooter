Shoot Za Zombies

Overview(setting)
The setting is a few months after the apocalypse started. You found some gear and a gun. But the Zombies are only increasing and you just found yourself. In quite the predicament. Zombies are attacking you. The only objective you have is to survive. And to take as many zombies down as possible. 
You have 20 health. Zombies hit you for 5 health
There’s a timer counting up. The goal is to survive as long as possible.
After a certain amount of time more zombies appear that follow the player.
Mouse input. 
The characters in the middle of the screen and aims where the cursor is on the screen
Shoot by clicking the mouse button. 
Zombies spawn off the screen and move towards the player
Change how fast you turn with a scroller on the menu (maybe)

Game States
Intro/MainMenu -> Text -> Gameplay -> EndGame -> Pause -> Gameplay -> Quit

Intro
Show Title Screen 
Give Instructions
Scroller to change sensitivity
Everything Else Hidden

Text
*Tell a bit of a story that you can proceed by pressing a button*
Gameplay elements are still hidden
Intro is hidden.
Text shown
BtnContinue shown

Gameplay
All Sprites Shown
Intro still hidden.
Text hidden
Timer and score reset

Quit
Game Ends

Restart
Btn quit hide
Btn restart hide
Sprites Reset

Sprites:

Player
Top down character with gun
User controlled
 Moves with WASD 
Character rotates with mouse cursor
Shoots gun with mouse click
If makes contact with zombie health minus 5
If health <= 0 End Screen

Zombie
Computer controlled
Walks towards player at all time
Spawns randomly outside the map
Walks slowly
If hit by bullet Zombie reset and there’s a kill sound
After a certain amount of time elapses more zombies will be added to the list and will spawn

UI Elements

Background
Outdoor open field 
Easy to see zombie and player and other UI elements

Title
Game Instructions multilabel
The name of game
Button
When button quit Title hide and text show

Text
MultiLabel of story
When clicked game starts

Timer
Starts when gameplay starts
Time counts up
After certain time more zombies appear

Health
Player health starts at 50
When hit by a zombie it goes down by 5
When health reaches zero pause screen
Gameplay hide
BtnReset
appears in pause state
When clicked, goes back to gameplay state
Hide buttons
Show all sprites
reset score and timer
BtnQuit
appears in pause state
when clicked, exits entire game

Sound Effects

Groans
This zombie noise will play randomly throughout the game

Splat
This sound will be play when a zombie gets hit by a bullet

Scream
This will play when your character dies




This was my beginning goal which changed throughout the project. I attempted a wave-based zombie game instead. My goals where to have waves of zombies that the character could shoot by aiming with their mouse which I thought would be fun. 

The instructions a player might need is that they can move around with wasd, aim their gun with the mouse, and shoot with a mouse click. 
My process was to try to get the base gameplay first and then touch up everything. I didn’t end up having as much time as I thought I would as I got stuck on how to make waves of zombies for like a week. Due to this, I was unable to touch the game up as much as I wanted even after an all-nighter. 
My game does have music playing throughout along with side effects that play when a character dies or when a gun shoots. I also have a splat sound for shooting the zombies. 
I learned a lot through this though. A lot with iterations and collisions between groups. I struggled with collisions for a while which the problem was due to iteration and other weird stuff like that so figuring that out was a big learning curve. I want to improve a lot of stuff.
I tried to make it so there was a countdown between each wave, and I couldn’t figure it out through much trial and error. I also wanted boss fights and to fix the collisions so that they were more realistic, but I couldn’t figure that out either. Throughout getting stuck on everything for so long I wasn’t able to get powerups either. I’m pretty disappointed honestly with how it turned out because I had pretty high hopes for it but I overestimated how quickly these ideas would get done since they seemed easy in my head. These are all areas I’d like to improve on and how I strayed from the game design document.

I was able to stay on track by sticking to my core gameplay elements even if the rest got changed a bit.






