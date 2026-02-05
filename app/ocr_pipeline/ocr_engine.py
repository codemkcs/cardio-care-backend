import easyocr

reader = easyocr.Reader(["en"], gpu=False)

def extract_text_with_boxes(image_path):
    results = reader.readtext(image_path)
    texts = []
    for bbox, text, conf in results:
        texts.append(text.lower())
    return texts
