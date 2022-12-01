# For measuring the inference time.
import time
import os 

iframe_path="WebRTCCall\Capturedvideo"
filename ="video.mp4"

def iframes():
    if not os.path.exists(iframe_path):
        os.mkdir(iframe_path)
    command = 'ffprobe -v error -show_entries frame=pict_type -of default=noprint_wrappers=1'.split()
    out = subprocess.check_output(command + [filename]).decode()
    f_types = out.replace('pict_type=','').split()
    frame_types = zip(range(len(f_types)), f_types)
    i_frames = [x[0] for x in frame_types if x[1]=='I']
    if i_frames:
        cap = cv2.VideoCapture(filename)
        for frame_no in i_frames:
            cap.set(cv2.CAP_PROP_POS_FRAMES, frame_no)
            ret, frame = cap.read()
            outname = iframe_path+'i_frame_'+str(frame_no)+'.jpg'
            cv2.imwrite(outname, frame)
        cap.release()
        print("I-Frame selection Done!!")


if __name__ == '__main__':
    iframes()