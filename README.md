# Lego Yoshi - Lego Super Mario Interactivity
Advait Ukidve - September 2023     

**Description:** Repository to save code for YoshiBot, a proposed expansion to the Lego Super Mario interactivity using OpenAI's GPT 3.5 Turbo API.     
**This Repository:**    
- [LSM_Software_Prototype](./LSM_Software_Prototype.ipynb) contains the full code used in the software presentation. This runs with no prerequisites save installation of the relevant packages on the system (indicated in code at the top).
- [LSM_Arduino_Prototype](./LSM_Arduino_Prototype.ipynb) contains the presentation version with limited functionality and requires hardware to run.
- [This folder](./Python/) contains the same code prototypes in .py format to be run using the Python console. These contain the same functionality but without the interactivity.
- [This folder](./LSM_Lego_Yoshi_Arduino/) contains the Arduino code to be run on the Arduino.
- [This]() is the presentation used for the Case Study Review Round 2 Interview scheduled Tuesday 26 September 2023 at 16:00 BST.

## About the Project


## How to Run
- **Software Prototype:** Download the .ipynb file and run in [Jupyter Notebook](https://jupyter.org/) locally or on [Google Colab](https://colab.google/) OR download the .py file and run using Python console
- **Hardware Prototype:** Download the Arduino files in this folder and upload them to the Arduino device (Built using [Leonardo](https://docs.arduino.cc/hardware/leonardo), but should work with most Arduino models). Download the .ipynb/.py file and run locally using Jupyter Notebook or Python Console. This cannot be run on Colab as it requires connection to the hardware. Use the following diagram (made using [Fritzing](https://fritzing.org/)) to wire up the various components:

![Schematics](./Schematics_bb.png). 
<sub> Full resolution version [here](./Schematics_bb.png) </sub>

*Note: Both the Python file and Arduino code assume a Windows system with the Arduino connected to COM3 at a baudrate of 9600. Make the appropriate changes if necessary.*

# Example Responses
## Shown in Arduino Prototype

#### 1 - Setting the Scene   
**Prompt:** *Describe a scene in Peach's Castle with Luigi and Toad before an adventure that will involve Donkey Kong, koopa troopas, Bowser Jr. and a pool of lava. Don't describe the actual adventure. Use upto 300 words.*    
   
**Response:** Oh, Mario! Let me tell you about the fun-filled scene at Peach's Castle with Luigi and Toad before our big adventure! It was a bright and beautiful day in the Mushroom Kingdom, with colorful flowers blooming all around. The castle courtyard was bustling with excitement as we prepared for our journey to save Princess Peach from the clutches of Bowser Jr. Luigi, as always, was a bit nervous but eager to prove his bravery. He was practicing his high jumps and spinning moves, trying to build up his confidence. And Toad, oh my goodness, he was scurrying around like a busy bee, making sure everything was ready for our departure. In the courtyard, we had set up a special obstacle course to train ourselves for the challenges ahead. There were green pipes to jump over, mushroom platforms to balance on, and even some bouncing question blocks filled with power-ups. We giggled with joy as we hopped and skipped through the obstacles, encouraging each other along the way. Meanwhile, Toad had prepared a delightful picnic for us in the castle gardens. We sat under a shady tree, munching on delicious mushroom sandwiches and sipping refreshing fruit juice. Toad even brought along his trusty ukulele and serenaded us with cheerful tunes. Oh, how it made our hearts sing! As we finished our picnic, we noticed a strange rumbling sound coming from the castle. We followed the noise and discovered that Bowser Jr. had unleashed a gang of mischievous koopa troopas near the castle's lava pool! Our adventure was about to begin! With determination in our hearts and smiles on our faces, we set off to face whatever challenges awaited us. Together, we would overcome every obstacle and rescue Princess Peach. Oh, Mario, I can't wait to share more tales of our exciting journey with you! Let's go save the day! Yoshi-yay!

#### 2 - Reacting to Fire Mario Suit   
**Prompt:** *Mario has just performed the following action: ### get the Fire Mario suit ###. React to it using less than 30 words.*    
   
**Response:** Yoshi-yay! Mario, you've got the Fire Mario suit! With that fiery power, you'll be able to blaze through obstacles and defeat enemies with ease!    

#### 3 - Reacting to defeating a Koopa Troopa 
**Prompt:** *Mario has just performed the following action: ### defeat a koopa troopa with the Fire Mario suit ###. React to it using less than 30 words.*    
    
**Response:** Yoshi-yippee! Mario, you used your fiery powers to defeat that pesky koopa troopa! Your Fire Mario skills are truly amazing! Keep it up!    

#### 4 - Generating a dialogue between Mario and Luigi
**Prompt:** *Generate a dialogue between Mario and Luigi based on the adventure so far.*     
    
**Response:**
- Mario: Luigi, my green-clad brother! What a whirlwind adventure we've had so far! From the Mushroom Kingdom to Bowser's castle, we've faced challenges and triumphs together.
- Luigi: Oh, Mario! It's been quite a journey indeed. I must admit, I was a bit scared at first, but you've always been there to encourage me and show me the way.
- Mario: Don't worry, Luigi! We're a team! Your bravery has shined through, especially when you defeated those tricky koopa troopas with your precise jumps!
- Luigi: Thanks, bro! And let's not forget how you used your Fire Mario suit to turn those enemies into toast! You were unstoppable!
- Mario: Ha ha! Fireballs flying everywhere! But remember when we encountered that tricky maze? Your quick thinking helped us navigate through it safely. I couldn't have done it without you!
- Luigi: Aw, shucks, Mario! You give me too much credit. But hey, what about that epic jump you made over that pool of lava? It was like watching a superstar in action!
- Mario: Well, you know me, Luigi. I can't resist a good leap! And speaking of leaps, your high jumps have been incredible throughout this adventure. You're soaring like a true hero!
- Luigi: Thanks for the kind words, Mario. It means a lot coming from you. We make such an amazing team. Let's keep saving Princess Peach and spreading joy across the Mushroom Kingdom!
- Mario: Absolutely, Luigi! Together, we'll overcome any challenge that comes our way. The adventures never end when we're together!
- Yoshi (eavesdropping): Yoshi-yay! Mario and Luigi are the best duo ever! With their teamwork and friendship, they'll conquer any obstacle that comes their way!


#### 5 - Recapping the entire adventure** 
**Prompt:** *Narrate an adventure where Lego Mario, sitting on Yoshi's back, does the following in order: ### reach Peach's Castle, meet Luigi and Toad, get the Fire Mario Suit, defeat a koopa troopa with the Fire Mario suit, talk to Luigi ###. Use the past tense. Don't use the following words ### Lego, toy, set ###*     
    
**Response:** Once upon a time, in a colorful land of blocks and bricks, Mario embarked on an exciting adventure atop Yoshi's back. Their journey began as they made their way towards the majestic Peach's Castle. With each hop and flutter, Yoshi carried Mario closer to their destination, his little legs propelling them forward with boundless energy. Finally, they reached Peach's Castle, where Luigi and Toad eagerly awaited their arrival. The familiar faces of Mario's trusted companions filled him with joy, and they greeted each other with warm smiles and friendly hugs. It was a reunion filled with laughter and excitement. In the castle courtyard, Luigi led Mario to a hidden room where the Fire Mario Suit awaited. As Mario adorned himself in the fiery attire, his confidence soared. With newfound powers, he felt invincible, ready to face any challenge that came their way. Their first test came in the form of a mischievous koopa troopa. With a burst of flames from his hands, Mario defeated the troublesome turtle-like creature. The koopa troopa scurried away, leaving behind a trail of defeated shells. After their victorious battle, Mario and Yoshi sought out Luigi for a little chat. They huddled together, discussing their next steps and sharing tales of their adventures thus far. Luigi expressed his admiration for Mario's bravery and thanked Yoshi for being such a reliable companion. With hearts full of determination and camaraderie, the trio continued their journey through the whimsical kingdom. They knew that as long as they stuck together, nothing could stand in their way. And so, with Yoshi leading the way, Mario rode atop his loyal steed, ready to face more challenges and rescue Princess Peach from the clutches of evil. Their adventure had only just begun, but with courage in their hearts and friendship by their side, there was no doubt that they would emerge triumphant!

## Examples from Software Prototype


## Credits
- Credit to **atomic14's command_line_chatgpt** project for providing me with a great technical jumping off point towards writing this code. You can find the public domain free-to-use code on their [Github](https://github.com/atomic14/command_line_chatgpt/tree/main) ([License](https://github.com/atomic14/command_line_chatgpt/blob/main/LICENSE.md)).    
- Thanks to countless online videos and shopfronts, and especially [DuckBricks' video](https://www.youtube.com/watch?v=uCqOGbqJ1s8) and [Bricksets](https://brickset.com/sets/theme-Super-Mario), without whom I couldn't have analysed the Lego Super Mario Interactive Toy Set fully.
