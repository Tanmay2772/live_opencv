import cv2
import pyaudio
import wave

# Initialize video capture
cap = cv2.VideoCapture(0)

# Define the codec for video saving
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

# Initialize audio recording
audio = pyaudio.PyAudio()
stream = audio.open(format=pyaudio.paInt16, channels=2, rate=44100, input=True, frames_per_buffer=1024)
frames = []

print("Recording video and audio... Press 'q' to stop")

# Start capturing video and audio
while True:
    ret, frame = cap.read()
    if ret:
        # Get frame dimensions (optional, for debugging)
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        # Show the video frame in a window
        cv2.imshow('Frame', frame)

        # Write the video frame to the file
        out.write(frame)

        # Capture audio data
        data = stream.read(1024)
        frames.append(data)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release the video capture and writer
cap.release()
out.release()

# Stop and close the audio stream
stream.stop_stream()
stream.close()
audio.terminate()

# Save the audio data to a WAV file
wave_file = wave.open("output_audio.wav", 'wb')
wave_file.setnchannels(2)
wave_file.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
wave_file.setframerate(44100)
wave_file.writeframes(b''.join(frames))
wave_file.close()

# Destroy all OpenCV windows
cv2.destroyAllWindows()

print("Video and audio recording completed.")
