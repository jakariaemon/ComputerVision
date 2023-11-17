import cv2
import os
import random
import hand_tracking_module as htm  # Ensure this module is properly installed or referenced

# Folder containing your move images
moves_folder = "moves_folder"  # Replace with your actual folder path

# Path to the hand image
image_path = "test.jpg"  # Replace with your actual file path
img = cv2.imread(image_path)

# Check if image is loaded
if img is None:
    print("Can't read the image file.")
    exit()

# Initialize the hand detector
detector = htm.handDetector(detectionCon=0.75)

tipIds = [4, 8, 12, 16, 20]  # Finger tip identifiers

# Process the loaded image
img = detector.findHands(img, draw=False)
lmList = detector.findPosition(img, draw=False)

if len(lmList) != 0:
    fingers = []

    # Thumb detection is based on x-axis position
    if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
        fingers.append(1)
    else:
        fingers.append(0)

    # Fingers detection based on y-axis position
    for id in range(1, 5):
        if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
            fingers.append(1)
        else:
            fingers.append(0)

    totalFingers = fingers.count(1)

    # Map the number of fingers to the corresponding game move
    game_moves = {0: 'rock', 5: 'paper', 2: 'scissors'}
    player_move = game_moves.get(totalFingers)

    if player_move:
        # The computer randomly selects a move
        computer_move = random.choice(['rock', 'paper', 'scissors'])

        # Load the image corresponding to the computer's move
        move_image_path = os.path.join(moves_folder, f"{computer_move}.png")
        move_img = cv2.imread(move_image_path)

        if move_img is None:
            print(f"Error loading the image for {computer_move}!")
            exit()

        # Resize for consistency
        img_height, img_width, _ = img.shape
        move_img = cv2.resize(move_img, (img_width, img_height))

        # Combine images
        combined_img = cv2.hconcat([img, move_img])

        # Determine the winner
        if player_move == computer_move:
            message = "It's a tie!"
        elif (player_move == 'rock' and computer_move == 'scissors') or \
             (player_move == 'scissors' and computer_move == 'paper') or \
             (player_move == 'paper' and computer_move == 'rock'):
            message = "You win!"
        else:
            message = "You lose!"

        # Display the game result message
        cv2.putText(combined_img, f"Computer's move: {computer_move}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
        cv2.putText(combined_img, message, (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

        # Show the combined image
        cv2.imwrite('combined.jpg', combined_img)

else:
    print("No hand detected in the image.")
