from flask import Flask, render_template, Response, jsonify
import cv2
import random
from flask_cors import CORS 

app = Flask(__name__)
CORS(app)

def gen_frames():
    """Generator function that yields camera frames in byte format."""
    camera = cv2.VideoCapture(0)

    if not camera.isOpened():
        raise RuntimeError("Could not start camera.")

    try:
        while True:
            success, frame = camera.read()
            if not success:
                break
            else:
                # Optional: Resize the frame for faster processing
                # frame = cv2.resize(frame, (640, 480))

                # Encode the frame in JPEG format
                ret, buffer = cv2.imencode('.jpg', frame)
                frame = buffer.tobytes()

                # Yield the output frame in byte format
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
    finally:
        camera.release()

@app.route('/')
def index():
    """Render the main page with initial random numbers."""
    # Generate two initial random numbers
    random_number1 = random.randint(1, 100)
    random_number2 = random.randint(1, 100)
    
    return render_template('index.html', number1=random_number1, number2=random_number2)

@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/get_random_numbers')
def get_random_numbers():
    """API endpoint to get new random numbers."""
    random_number1 = random.randint(1, 100)
    random_number2 = random.randint(1, 100)
    return jsonify({'number1': random_number1, 'number2': random_number2})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
