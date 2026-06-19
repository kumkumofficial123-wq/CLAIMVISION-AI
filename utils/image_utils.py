import cv2

def estimate_damage(image_path):

    img = cv2.imread(image_path)

    gray = cv2.cvtColor(
        img,
        cv2.COLOR_BGR2GRAY
    )

    edges = cv2.Canny(
        gray,
        50,
        150
    )

    damage_pixels = edges.sum()/255

    if damage_pixels > 5000:

        severity = "high"

    elif damage_pixels > 2000:

        severity = "medium"

    else:

        severity = "low"

    return severity