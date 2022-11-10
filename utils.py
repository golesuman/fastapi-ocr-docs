import cv2
from easyocr import Reader

def cleanup_text(text):
  return "".join([c if ord(c) < 128 else "" for c in text]).strip()

def predict(image, langs, gpu):
    reader = Reader(langs, gpu)
    results = reader.readtext(image)

    for (bbox, text, prob) in results:
        print(f"[INFO] {prob:.4f}: {text}")
        (tl, tr, br, bl) = bbox # bounding box
        tl = (int(tl[0]), int(tl[1]))
        tr = (int(tr[0]), int(tr[1]))
        br = (int(br[0]), int(br[1]))
        bl = (int(bl[0]), int(bl[1]))
        # cleanup the text and draw the box surrouding the text along
        # with ocr'd text itself
        text = cleanup_text(text)
        cv2.rectangle(image, tl, br, (0, 255, 0), 2)
        cv2.putText(image, text, (tl[0], tl[1] -10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
        return image