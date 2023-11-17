from turtle import delay
import cv2
import random
import os
import hand_tracking_module as htm
import time
moves_folder = "moves_folder"
detector = htm.handDetector(detectionCon=0.75)
cap = cv2.VideoCapture(0)
game_state = "start"  

tipIds = [4, 8, 12, 16, 20]


move_images = {move: cv2.imread(os.path.join(moves_folder, f"{move}.jpg")) for move in ['rock', 'paper', 'scissors']}

while cap.isOpened():
    success, img = cap.read()
    if not success:
        print("Failed to grab frame")
        break

    img = detector.findHands(img, draw=True)
    lmList = detector.findPosition(img, draw=False)

    # Instructions overlay based on the game state
    instructions = ""
    if game_state == "start":
        instructions = "Press 'r' to make a move"
    elif game_state == "move_made":
        instructions = "Press 'r' to play again"
    
    cv2.putText(img, instructions, (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
    
    cv2.imshow('Rock Paper Scissors', img)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    if key == ord('r') and game_state in ["start", "move_made"]:
        game_state = "ready"

    if game_state == "ready" and lmList:
        fingers = []

        if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
            fingers.append(1)
        else:
            fingers.append(0)

        for id in range(1, 5):
            if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                fingers.append(1)
            else:
                fingers.append(0)

        totalFingers = fingers.count(1)

        if totalFingers == 0:
            player_move = 'rock'
        elif totalFingers == 5:
            player_move = 'paper'
        elif totalFingers == 2 and fingers[1] == 1 and fingers[2] == 1:
            player_move = 'scissors'
        else:
            player_move = None  

        if player_move:
            computer_move = random.choice(['rock', 'paper', 'scissors'])
            move_img = move_images.get(computer_move)

            if move_img is None:
                print(f"Error loading the image for {computer_move}!")
                continue

            if player_move == computer_move:
                message = "It's a tie!"
            elif (player_move == 'rock' and computer_move == 'scissors') or \
                 (player_move == 'scissors' and computer_move == 'paper') or \
                 (player_move == 'paper' and computer_move == 'rock'):
                message = "You win!"
            else:
                message = "You lose!"

            combined_img = cv2.hconcat([img, cv2.resize(move_img, img.shape[1::-1])])
            cv2.putText(combined_img, f"Computer's move: {computer_move}", (img.shape[1] + 10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
            cv2.putText(combined_img, message, (50, img.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            cv2.imshow('Rock Paper Scissors', combined_img)
            if cv2.waitKey(5000) & 0xFF == ord('q'):
                break
            
            game_state = "move_made"  


cap.release()
cv2.destroyAllWindows()
