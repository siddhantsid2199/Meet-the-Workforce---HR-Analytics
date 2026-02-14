import fitz  # PyMuPDF
import io
from PIL import Image

def extract_images(pdf_path):
    doc = fitz.open(pdf_path)
    for i in range(len(doc)):
        for img in doc.get_page_images(i):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            image_ext = base_image["ext"]
            image = Image.open(io.BytesIO(image_bytes))
            image.save(f"image_{pdf_path.replace(' ', '_')}_{i}_{xref}.{image_ext}")
    doc.close()

extract_images("Meet the Workforce- HR Analytics Report.pdf")
extract_images("Meet the Workforce- HR Analytics.pdf")
