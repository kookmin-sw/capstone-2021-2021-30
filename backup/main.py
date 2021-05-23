import cv2, os, sys, time
from pytube import YouTube
from PIL import Image
import file_name_changer as fc
import motion_data as md
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.check_box = []
        self.list = []
        self.selected_list = []
        self.setupUI()

    # UI 생성
    def setupUI(self):
        self.setWindowTitle("Motion Capturer")
        self.resize(750, 750)

        # 전체 레이아웃(vertical)
        self.hbox_layout = QHBoxLayout()

        # 좌측 리스트(스크롤>그룹박스>폼레이아웃>체크박스)
        self.form_layout = QFormLayout()
        self.group_box = QGroupBox(self)
        # 리스트에 넣기
        self.setList()
        self.group_box.setLayout(self.form_layout)
        # 스크롤바에 리스트 넣기
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidget(self.group_box)
        self.scroll_area.setStyleSheet("background-color: white;")
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll_area.setWidgetResizable(True)
        self.hbox_layout.addWidget(self.scroll_area)

        # 우측 버튼 레이아웃(horizontal)
        self.vbox_layout = QVBoxLayout()
        # 폴더열기 버튼
        self.file_btn = QPushButton("파일열기", self)
        self.file_btn.clicked.connect(self.fileBtnClicked)
        self.vbox_layout.addWidget(self.file_btn)
        # 실행 버튼
        self.execute_btn = QPushButton("실행", self)
        self.execute_btn.clicked.connect(self.executeBtnClicked)
        self.vbox_layout.addWidget(self.execute_btn)

        # 레이아웃 정리
        self.hbox_layout.addLayout(self.vbox_layout)
        self.setLayout(self.hbox_layout)

    # 리스트 생성
    def setList(self):
        # 체크박스, 폼 레이아웃 초기화
        self.check_box.clear()
        for x in reversed(range(self.form_layout.count())):
            self.form_layout.itemAt(x).widget().setParent(None)

        # 리스트에 따른 체크박스 생성
        for i in range(len(self.list)):
            self.check_box.append(QCheckBox(self.list[i]))
            self.form_layout.addWidget(self.check_box[i])

    # 파일열기 버튼 클릭
    def fileBtnClicked(self):
        # 파일 탐색기
        self.fileDialog = QFileDialog(self)
        self.fileDialog.setFileMode(QFileDialog.ExistingFiles)
        self.fileDialog.setNameFilter(
            self.tr("Videos (*.avi *.mp4 *.wmv *.mpg *.flv *.mov);; All Files(*.*)"))  # 파일 탐색기 확장자 설정
        self.fileDialog.setViewMode(QFileDialog.Detail)
        self.list.clear()
        if self.fileDialog.exec_():
            self.list = self.fileDialog.selectedFiles()
        self.setList()

    # 실행 버튼 클릭
    def executeBtnClicked(self):
        # 체크된 리스트 구함
        self.selected_list.clear()
        for i in range(len(self.list)):
            if self.check_box[i].checkState():
                print(self.list[i])
                self.selected_list.append(self.list[i])

        motion = md.MotionData()
        # 체크된 리스트 내용으로 변환 시작
        for j in range(len(self.selected_list)):
            #self.dialog = QDialog()
            #self.dialog.setWindowTitle("Sign Language Video")
            #self.dialog.show()

            motion.getHolisticData3(self.selected_list[j])

class VideoEditer:
    def getVideoAndAudio(self, download_path):
        yt = YouTube(input("url path: "))

        videos = yt.streams.filter(file_extension='mp4')
        for i in range(len(videos)):
            print(i, '. ', videos[i])
        video_num = int(input("select video resolution: "))
        videos[video_num].download(download_path + "videos/")

        audios = yt.streams.filter(only_audio=True)
        for i in range(len(audios)):
            print(i, '. ', audios[i])
        audio_num = int(input("select audio resolution: "))
        audios[audio_num].download(download_path + "audios/")

        print("video download completed...")

    def videoToFrameImages(self, download_path, fps):
        count = 0
        cap = cv2.VideoCapture(download_path + "videos/[출근길 날씨] 맑고 큰 일교차…수도권·충청 황사 영향  KBS 20210317.mp4")

        def getFrame(sec):
            cap.set(cv2.CAP_PROP_POS_MSEC, sec * 1000)
            hasFrames, image = cap.read()
            if hasFrames:
                cv2.imwrite(download_path + "images/%d.jpg" % count, image)
            return hasFrames

        sec = 0
        success = getFrame(sec)
        while success:
            sec += 1./fps
            sec = round(sec, 2)
            success = getFrame(sec)
            print("%d.jpg done" % count)
            count += 1

        cap.release()

        print("frame image save completed...")

    def cropVideo(self, download_path, crop_area):
        file_list = os.listdir(download_path + "images/")

        for file in file_list:
            img = Image.open(download_path + "images/" + file)
            crop_img = img.crop(crop_area)
            crop_img.save("D:/youtube/crop_images/%s" % file)
            print("%s done" % file)

        print("image cropped completed...")

def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    # AIHub 수화 영상 이름 변경 (필요시 사용)
    '''
    reader = fc.FileNameChanger()
    reader.readCsvFile('./reference/data_anotation.csv', 'D:/sign_language_video', 420)
    print("read csv and video name changed")
    '''

    # UI 실행
    #main()

    # 영상 편집 클래스
    # 날씨 주소 : https://www.youtube.com/watch?v=mlE_AfipkNs&list=PL0Hzp0A3iLSxHccWBo2n_Ps8bPwDO-Mb_&index=4&ab_channel=KBSNews
    # 총 84초
    download_path = "D:/youtube/"
    ve = VideoEditer

    #ve.getVideoAndAudio(ve, download_path)  # 유튜브 동영상 저장 및 오디오 추출
    #ve.videoToFrameImages(ve, download_path, 5)  # 유튜브 영상 -> 프레임 이미지
    #crop_area = (1080, 490, 1248, 653)
    #crop_area = (1620, 735, 1872, 980)
    #ve.cropVideo(ve, download_path, crop_area)  # 프레임 이미지 -> 수화 부분만 저장

    # 수화 부분만 저장된 이미지의 키포인트 구하기
    mdata = md.MotionData
    mdata.getDataFromImages(mdata, download_path)

    sys.exit()

