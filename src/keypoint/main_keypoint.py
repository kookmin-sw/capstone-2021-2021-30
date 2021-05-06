import cv2, os, sys
import src.keypoint.get_keypoint as gk
from pytube import YouTube
from PIL import Image

class mainKeypoint:
    def __init__(self):
        self.select = 0
        self.download_path = "../data/"
        self.video_name = "No Name"

    def excute(self):
        # data 폴더에 필요한 폴더 있는지 확인 후 없으면 생성
        self.makeDirectories()

        # 종료 전까지 실행
        while True:
            # 번호 입력 예외 처리
            self.getSelectNumber()

            # 번호 처리
            # 작업할 비디오 이름 저장
            if self.select == 0:
                print("\n\tStart 0. Save the Video File Name...")
                self.getVideoName()

            # url을 입력 받아 동영상과 오디오 다운로드
            elif self.select == 1:
                print("\n\tStart 1. Download Youtube Video and Audio...")
                self.getVideoAndAudio()

            # 동영상을 프레임 이미지들로 변환
            elif self.select == 2:
                print("\n\tStart 2. Video -> Frame Images...")
                self.videoToFrameImages()

            # 프레임 이미지들을 크롭된 이미지로 변환
            elif self.select == 3:
                print("\n\tStart 3. Frame Images -> Cropped Images...")
                self.imagesToCroppedImages()

            # 크롭된 이미지를 토대로 키포인트 생성
            elif self.select == 4:
                print("\n\tStart 4. Get Keypoint from Images...")
                getk = gk.getKeypoint
                getk.getKeypointFromImages(getk, self.download_path, self.video_name)

            # 그 외의 숫자는 종료
            else:
                print("\n! Exit (Number out of range)")
                sys.exit()

    # data 폴더에 필요한 폴더 있는지 확인 후 없으면 생성
    def makeDirectories(self):
        try:
            if not os.path.exists(self.download_path + "video/"):
                os.makedirs(self.download_path + "video/")
            if not os.path.exists(self.download_path + "audio/"):
                os.makedirs(self.download_path + "audio/")
            if not os.path.exists(self.download_path + "image_frame/"):
                os.makedirs(self.download_path + "image_frame/")
            if not os.path.exists(self.download_path + "image_cropped/"):
                os.makedirs(self.download_path + "image_cropped/")
            if not os.path.exists(self.download_path + "image_keypoint/"):
                os.makedirs(self.download_path + "image_keypoint/")
            if not os.path.exists(self.download_path + "keypoint/"):
                os.makedirs(self.download_path + "keypoint/")

        except OSError:
            print("\n! Error: Failed to create the directory")
            sys.exit()

    # 번호 입력 예외 처리
    def getSelectNumber(self):
        print("\n0. Save the Video File Name")
        print("1. Download Youtube Video and Audio")
        print("2. Video -> Frame Images")
        print("3. Frame Images -> Cropped Images")
        print("4. Get Keypoint from Images")
        print("?. Exit")

        try:
            self.select = int(input("\nSelect the number: "))
        except:
            print("\n! Exit (Not Number)")
            sys.exit()

    # 작업할 비디오 이름 저장
    def getVideoName(self):
        file_list = os.listdir(self.download_path + "video/")

        print("")
        for i, file in enumerate(file_list):
            print(i, '. ', file)

        try:
            file_num = int(input("\nSelect video file: "))
            self.video_name = file_list[file_num].replace(".mp4", "")
        except:
            print("\n! Error: Wrong select number")

    # url을 입력 받아 동영상과 오디오 다운로드
    def getVideoAndAudio(self):
        # 예) 날씨 영상 (84초) : https://www.youtube.com/watch?v=mlE_AfipkNs&list=PL0Hzp0A3iLSxHccWBo2n_Ps8bPwDO-Mb_&index=4&ab_channel=KBSNews
        try:
            yt = YouTube(input("\nEnter the Youtube url: "))
            self.video_name = yt.streams[0].title.replace(".", "")

            # 유튜브 동영상 다운로드
            videos = yt.streams.filter(only_video=True, file_extension='mp4')
            print("")
            for i in range(len(videos)):
                print(i, '. ', videos[i])
            print("? .  Pass")

            try:
                video_num = int(input("\nSelect video resolution: "))
                videos[video_num].download(self.download_path + "video/")
                print("\nVideo download completed...")
            except:
                print("\nVideo download passed...")

            # 유튜브 오디오 다운로드
            audios = yt.streams.filter(only_audio=True)
            print("")
            for i in range(len(audios)):
                print(i, '. ', audios[i])
            print("? .  Pass")

            try:
                audio_num = int(input("\nSelect audio resolution: "))
                audios[audio_num].download(self.download_path + "audio/")
                print("\nAudio download completed...")
            except:
                print("\nAudio download passed...")

        except:
            print("\n! Error: Wrong Youtube url")

    # 동영상을 프레임 이미지들로 변환
    def videoToFrameImages(self):
        # 해당 비디오 파일이 있는지 확인
        if os.path.isfile(self.download_path + "video/" + self.video_name + ".mp4"):
            # 필요한 fps값 입력 후 실수인지 확인
            try:
                fps = float(input("\nEnter the fps: "))
                print("")
            except:
                print("\n! Error: Fps value is not float")

            # 해당 비디오 파일의 이름으로 빈 디렉토리를 생성
            capture_path = self.download_path + "image_frame/" + self.video_name + "/"
            try:
                if not os.path.exists(capture_path):
                    os.makedirs(capture_path)
                for file in os.scandir(capture_path):
                    os.remove(file.path)
            except:
                print("\n! Error: Failed to create empty directory")

            count = 0
            cap = cv2.VideoCapture(self.download_path + "video/" + self.video_name + ".mp4")

            # 프레임 이미지 캡쳐 과정
            def getFrame(sec):
                cap.set(cv2.CAP_PROP_POS_MSEC, sec * 1000)
                hasFrames, image = cap.read()
                if hasFrames:
                    imwrite2(capture_path + "%d.jpg" % count, image)
                return hasFrames

            # imwrite가 한글 경로를 인식하지 못해 대신 imencode 사용
            def imwrite2(filename, image, params=None):
                try:
                    ext = os.path.splitext(filename)[1]
                    result, n = cv2.imencode(ext, image, params)
                    if result:
                        with open(filename, mode='w+b') as f:
                            n.tofile(f)
                        return True
                    else:
                        return False
                except Exception as e:
                    print(e)
                    return False

            sec = 0
            success = getFrame(sec)
            while success:
                sec += 1. / fps
                sec = round(sec, 2)
                success = getFrame(sec)
                print(capture_path + "%d.jpg done..." % count)
                count += 1

            cap.release()

            print("\nSaving Frame images completed...")

        else:
            print("\n! Error: There's no video name called '" + self.download_path + "video/" + self.video_name + ".mp4'")

    # 프레임 이미지들을 크롭된 이미지로 변환
    def imagesToCroppedImages(self):
        # 작업 비디오 파일 이름의 폴더가 없을 경우 예외 처리
        try:
            file_list = os.listdir(self.download_path + "image_frame/" + self.video_name + "/")
        except:
            print("\n! Error: There's no directory called '" + self.download_path + "video/" + self.video_name + "/")

        # 자를 영역값 입력 예외 처리
        # 예) (1620, 735, 1872, 980)
        try:
            print("\nEnter the cropping location values like this (start-x, start-y, end-x, endy)")
            start_x = int(input("Enter the cropping start-x: "))
            start_y = int(input("Enter the cropping start-y: "))
            end_x = int(input("Enter the cropping end-x: "))
            end_y = int(input("Enter the cropping end-y: "))
            crop_area = (start_x, start_y, end_x, end_y)
        except:
            print("\n! Error: Cropping values is not int")

        # '/image_cropped/'에 해당 빈 폴더 생성
        crop_path = self.download_path + "image_cropped/" + self.video_name + "/"
        try:
            if not os.path.exists(crop_path):
                os.makedirs(crop_path)
            for file in os.scandir(crop_path):
                os.remove(file.path)
        except:
            print("\n! Error: Failed to create empty directory")

        for file in file_list:
            img = Image.open(self.download_path + "image_frame/" + self.video_name + "/" + file)
            crop_img = img.crop(crop_area)
            crop_img.save(crop_path + "%s" % file)
            print(crop_path + "%s done..." % file)

        print("\nCropping images completed...")