import cv2
import time
from send_email import send_email
import glob
import os
import shutil
from threading import Thread, Condition

condition = Condition()

imgdir = "images"


def cleanup(directory, condition):
    with condition:
        condition.wait()
    print("cleanup started")
    try:
        shutil.rmtree(directory)
        print(f'{directory} has been removed')
    except OSError as e:
        print(f'Error: {e.filename} - {e.strerror}')
    print("cleanup ended")


livefeed = cv2.VideoCapture(0)
time.sleep(0.5)

first_frame = None
status_list = []
while True:
    filename = time.strftime("%Y-%m-%d__%H-%M-%S")
    foreign_object_status = 0
    check, frame = livefeed.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_frame_gau = cv2.GaussianBlur(gray_frame, (21, 21), 0)
    # Intentionally blurring the frame data actually reduces the filesize of the frame, as does
    # making it grayscale.
# """The function takes three main arguments:
#
# gray_frame: The input grayscale frame to be blurred.
# (21, 21): The size of the Gaussian kernel. This specifies the width and height of the kernel used for blurring. A larger kernel size results in stronger blurring.
# 0: The standard deviation of the Gaussian kernel in the X and Y directions. Setting it to 0 lets OpenCV automatically calculate it based on the kernel size.
# """
#     cv2.imshow("My Video", gray_frame_gau)

    if first_frame is not None:
        pass
    else:
        first_frame = gray_frame_gau
        # As this will only run once, first_frame will be permanently frozen to whatever was on screen
        # when the webcam was first booted up.

    delta_frame = cv2.absdiff(first_frame, gray_frame_gau)
    # cv2.imshow("My Video", delta_frame)
    # ^^^ uncommment this and comment the earlier cv2.imshow to see what this delta frame looks like.

    thresh_frame = cv2.threshold(delta_frame, 45, 255, cv2.THRESH_BINARY)[1]
    # Any pixel with a value above 255 becomes pure white.
    # See figure[THRESH] in the notebook to see what this looks like as actual numbers
    dil_frame = cv2.dilate(thresh_frame, None, iterations=2)
    # This further de-noises the image.
    # cv2.imshow("My Video", dil_frame)

# Now we want to find contours around the white image:
    countours, check = cv2.findContours(dil_frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in countours:
        if cv2.contourArea(contour) < 5000:
            continue
        x, y, w, h = cv2.boundingRect(contour)
        greenrect = cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)  # give the dimensions of the bottom left and top right corner of your boundary rectangle
        # (0, 255, 0) is the color of the frame, 3 is the width of the frame...
        if greenrect.any():
            foreign_object_status = 1

            if not os.path.exists(imgdir):
                os.makedirs(imgdir)
                cv2.imwrite(f"{imgdir}/{filename}.jpg", frame)
            else:
                cv2.imwrite(f"{imgdir}/{filename}.jpg", frame)

    # ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()
    # any() returns True if at least one element in the iterable is truthy, while all() returns True only if all elements in the iterable are truthy. Otherwise, both functions return False.

    status_list.append(foreign_object_status)
    status_list = status_list[-2:] # This takes only the last two items from the status_list.
    if status_list[0] == 1 and status_list[1] == 0:
        all_images = glob.glob("images/*.jpg")
        index_to_email = int((len(all_images)) / 2)
        image_to_email = all_images[index_to_email]
        email_thread = Thread(target=send_email, args=(image_to_email, condition))
        email_thread.daemon = True
        email_thread.start()
        # We COULD solve the problem by putting clean_thread and all that outside the while loop, so it only runs
        # when the user quits the program with q.
        # but I think there's a better way using CONDITIONS:
        print("I'm between email thread and clean thread.")
        clean_thread = Thread(target=cleanup, args=(imgdir, condition))
        clean_thread.daemon = True
        clean_thread.start()

    cv2.imshow("Video", frame)
    key = cv2.waitKey(1)

    if key == ord("q"):
        break

print("blah blah blah")

livefeed.release()