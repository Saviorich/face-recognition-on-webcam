import cv2


def get_image_from_webcam():
    cam = cv2.VideoCapture(0)
    while True:
        ret_val, img = cam.read()
        cv2.imshow('"Space" to search for faces', img)
        key = cv2.waitKey(1)
        if key == 32:  # space
            cv2.destroyAllWindows()
            return img


def view_image(image, name_of_window):
    cv2.namedWindow(name_of_window, cv2.WINDOW_AUTOSIZE)
    cv2.imshow(name_of_window, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def get_faces_from_image(image):
    face_cascade = cv2.CascadeClassifier('venv/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5
    )
    return faces


def draw_rectangle_on_faces(image, faces):
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 255, 0), 1)


def main():
    image = get_image_from_webcam()
    faces = get_faces_from_image(image)
    faces_amount = f"Faces found: {len(faces)}"
    draw_rectangle_on_faces(image, faces)
    view_image(image, faces_amount)


if __name__ == '__main__':
    main()
