# 🎵 Hypixel SkyBlock Harp Bot 🎵

## 🇬🇧 English Version

### 📝 Description
This bot helps you achieve 100% completion on the Harp minigame in Hypixel SkyBlock. It automatically plays various songs by simulating mouse movements and key presses.

### 🛠️ Installation

1. Make sure you have Python installed on your computer
2. Install the required dependencies using pip:
```bash
pip install pyautogui
pip install keyboard
```

### 🎮 How to Use

1. Run the script:
```bash
python3 harp.py
```

2. Select a song from the menu by entering its number (1-11)
3. Switch to your Minecraft window
4. Start the song in Minecraft
5. Wait for the first block to hit the border (the line where you need to click)
6. Press 'S' exactly when the first block hits the border
7. Press 'Q' at any time to stop the bot

### ⚙️ Configuration

#### Mouse Coordinates
The bot uses specific mouse coordinates for each note. If the coordinates don't match your screen ( default: 1920x1080 ):
- Use a tool like MPos-v.0.5.0 to get your mouse coordinates
- Edit the `mapping` dictionary in the code with your coordinates

#### Song Timing
If a song doesn't play correctly, you may need to adjust its delay:
- Open the script
- Find the `songs` dictionary
- Modify the `delay` value for the specific song
- Common delay values are between 0.0484 and 0.1484 seconds

### 🎼 Available Songs
1. Hymn To The Joy
2. Frere Jacques
3. Amazing Grace
4. Brahms Lullaby
5. Happy Birthday To You
6. Greensleeves
7. Geometry
8. Minuet
9. Joy To The World
10. Godly Imagination
11. La Vie En Rose

### ⚠️ Important Notes
- Make sure your Minecraft window is in focus when starting the song
- The bot uses the 'W' key to play notes
- Keep the game window visible and don't move it while the bot is running
- You may need to adjust the delay values based on your computer's performance
- Timing is crucial - press 'S' exactly when the first block hits the border

---

## 🇫🇷 Version Française

### 📝 Description
Ce bot vous aide à obtenir 100% de réussite dans le minijeu de la Harpe sur Hypixel SkyBlock. Il joue automatiquement différentes chansons en simulant les mouvements de la souris et les appuis de touches.

### 🛠️ Installation

1. Assurez-vous d'avoir Python installé sur votre ordinateur
2. Installez les dépendances requises avec pip :
```bash
pip install pyautogui
pip install keyboard
```

### 🎮 Comment Utiliser

1. Exécutez le script :
```bash
python3 harp.py
```

2. Sélectionnez une chanson dans le menu en entrant son numéro (1-11)
3. Basculez vers votre fenêtre Minecraft
4. Démarrez la chanson dans Minecraft
5. Attendez que le premier bloc atteigne la bordure (la ligne où vous devez cliquer)
6. Appuyez sur 'S' exactement quand le premier bloc atteint la bordure
7. Appuyez sur 'Q' à tout moment pour arrêter le bot

### ⚙️ Configuration

#### Coordonnées de la Souris
Le bot utilise des coordonnées spécifiques pour chaque note. Si les coordonnées ne correspondent pas à votre écran (default: 1920x1080) :
- Utilisez un outil comme MPos-v.0.5.0 pour obtenir vos coordonnées de souris
- Modifiez le dictionnaire `mapping` dans le code avec vos coordonnées

#### Timing des Chansons
Si une chanson ne joue pas correctement, vous devrez peut-être ajuster son délai :
- Ouvrez le script
- Trouvez le dictionnaire `songs`
- Modifiez la valeur `delay` pour la chanson spécifique
- Les valeurs de délai courantes sont entre 0.0484 et 0.1484 secondes

### 🎼 Chansons Disponibles
1. Hymne à la Joie
2. Frère Jacques
3. Amazing Grace
4. Berceuse de Brahms
5. Joyeux Anniversaire
6. Greensleeves
7. Geometry
8. Menuet
9. Joy to the World
10. Godly Imagination
11. La Vie en Rose

### ⚠️ Notes Importantes
- Assurez-vous que votre fenêtre Minecraft est active lorsque vous démarrez la chanson
- Le bot utilise la touche 'W' pour jouer les notes
- Gardez la fenêtre du jeu visible et ne la déplacez pas pendant que le bot fonctionne
- Vous devrez peut-être ajuster les valeurs de délai en fonction des performances de votre ordinateur
- Le timing est crucial - appuyez sur 'S' exactement quand le premier bloc atteint la bordure
