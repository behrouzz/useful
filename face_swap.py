import cv2
import matplotlib.pyplot as plt
from datetime import datetime
from insightface.app import FaceAnalysis
from insightface.model_zoo import get_model

def show_face(face):
    bbox = face['bbox']
    bbox = [int(b) for b in bbox]
    plt.imshow(img[bbox[1]:bbox[3], bbox[0]:bbox[2], ::-1])
    plt.show()


app = FaceAnalysis(name='buffalo_l')
app.prepare(ctx_id=0, det_size=(640, 640))


swapper = get_model('../Models/inswapper_128.onnx',
                    download=False, download_zip=False)

# Original image
img = cv2.imread('data/0.jpg')
faces = app.get(img)
face = faces[0] # Manual: first face

# My image
me = cv2.imread('data/me.JPG')
me_face = app.get(me)[0]

# resulting image
res = img.copy()
res = swapper.get(res, face, me_face, paste_back=True)

# save result
t = datetime.now()
filename = t.isoformat().replace(':', '-').replace('T', ' ')[:19]
cv2.imwrite(f'data/{filename}.jpg', res)
