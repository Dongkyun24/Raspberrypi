#picamera_test.py
import picamera
import time

path = "/home/pi/src6/06_multimedia"

camera = picamera.PiCamera()

try:
    camera.resolution = (640, 480) #사진크기
    camera.start_preview()
    time.sleep(3) #카메라 촬영 준비시간 필요
    camera.rotation = 180
    #camera.capture("%s/photo.jpg" % path) #사진촬영

    camera.start_recording("%s/video.h264" % path) # 동영상 촬영
    #time.sleep(10)
    input("press enter to stop")
    camera.stop_recording()

finally:
    camera.stop_preview
ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
#pygame_play.py
import pygame

pygame.init()

pygame.mixer.music.load('sample1.mp3')
while True:
    cmd = input('play:p, pause:pp, unpause:up, stop:s, quit:q >')
    if cmd == 'p':
        pygame.mixer.music.play()
    elif cmd == 'pp':
        pygame.mixer.music.pause()
    elif cmd == 'up':
        pygame.mixer.music.unpause()
    elif cmd == 's':
        pygame.mixer.music.stop()
    elif cmd == 'q':
        break
    else:
        print("incorrect command")
#pyaudio_recording.py
# PyAudio로 Recording하기

import pyaudio
import wave

SAMPLE_RATE = 44100  # 음성데이터 샘플링 레이트 : 44100hz
FORMAT = pyaudio.paInt16
CHANNELS = 1
CHUNK = 1024
RECORD_SECONDS = 5

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=SAMPLE_RATE,
                input=True,
                frames_per_buffer=CHUNK)

print('start recording')

frames = []

for i in range(0, int(SAMPLE_RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

print('stop recording')

stream.stop_stream()
stream.close()
p.terminate()

wf = wave.open('output.wav', 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(SAMPLE_RATE)
wf.writeframes(b''.join(frames))
wf.close()
ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
#pyaudio_play.py
# PyAudio로 wav파일 재생하기

import pyaudio
import wave

# 음성데이터를 불러올때 한번에 몇개씩 가져올지
CHUNK = 1024

wf = wave.open('sample.wav', 'rb')
p = pyaudio.PyAudio()

# 음성데이터 스트림 열기
stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True)

data = wf.readframes(CHUNK)

# 음성데이터를 입력받아 출력
while data:
    stream.write(data)
    data = wf.readframes(CHUNK)

stream.stop_stream()
stream.close()
p.terminate()
wf.close()