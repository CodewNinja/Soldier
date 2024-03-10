import speech_recognition as sr
import time

class AskeriRobot:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.ates_durumu = False
        self.ileri_durumu = False
        self.geri_durumu = False
        self.sola_durumu = False
        self.saga_durumu = False
        self.ziplama_durumu = False
        self.ag_kesme_durumu = False
        self.teknoloji_etkisiz_durumu = False
        self.thermal_sensör = False
        self.hızlı_algılama = False

    def dinle_ve_anla(self):
        with sr.Microphone() as source:
            print("Sesli komut bekleniyor...")
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source)

            try:
                komut = self.recognizer.recognize_google(audio, language="tr-TR")
                print("Algılanan komut:", komut)
                self.anla_ve_uygula(komut)
            except sr.UnknownValueError:
                print("Üzgünüm, anlayamadım.")
            except sr.RequestError as e:
                print("Ses hizmeti başarısız; {0}".format(e))

    def anla_ve_uygula(self, komut):
        if "ateş et" in komut:
            self.ates_et()
        elif "ileri git" in komut:
            self.ileri_git()
        elif "geri gel" in komut:
            self.geri_git()
        elif "sola git" in komut:
            self.sola_git()
        elif "sağa git" in komut:
            self.saga_git()
        elif "zıpla" in komut:
            self.zipla()
        elif "ağları kes" in komut:
            self.aglari_kes()
        elif "teknolojik aletleri etkisiz hale getir" in komut:
            self.teknoloji_etkisiz_hale_getir()
        elif "termal sensörü etkinleştir" in komut:
            self.termal_sensör_aktifle()
        elif "hızlı algılama" in komut:
            self.hizli_algilama_aktifle()
        else:
            print("Anlaşılamayan komut.")

    def ates_et(self):
        if not self.ates_durumu:
            print("Ateş etme modu aktifleştiriliyor...")
            self.ates_durumu = True
            time.sleep(1)
            print("Ateş etme modu aktifleştirildi.")
        else:
            print("Ateş etme modu zaten aktif.")

    def ileri_git(self):
        if not self.ileri_durumu:
            print("İleri gitme modu aktifleştiriliyor...")
            self.ileri_durumu = True
            time.sleep(1)
            print("İleri gitme modu aktifleştirildi.")
        else:
            print("İleri gitme modu zaten aktif.")

    def geri_git(self):
        if not self.geri_durumu:
            print("Geri gitme modu aktifleştiriliyor...")
            self.geri_durumu = True
            time.sleep(1)
            print("Geri gitme modu aktifleştirildi.")
        else:
            print("Geri gitme modu zaten aktif.")

    def sola_git(self):
        if not self.sola_durumu:
            print("Sola gitme modu aktifleştiriliyor...")
            self.sola_durumu = True
            time.sleep(1)
            print("Sola gitme modu aktifleştirildi.")
        else:
            print("Sola gitme modu zaten aktif.")

    def saga_git(self):
        if not self.saga_durumu:
            print("Sağa gitme modu aktifleştiriliyor...")
            self.saga_durumu = True
            time.sleep(1)
            print("Sağa gitme modu aktifleştirildi.")
        else:
            print("Sağa gitme modu zaten aktif.")

    def zipla(self):
        if not self.ziplama_durumu:
            print("Zıplama modu aktifleştiriliyor...")
            self.ziplama_durumu = True
            time.sleep(1)
            print("Zıplama modu aktifleştirildi.")
        else:
            print("Zıplama modu zaten aktif.")

    def aglari_kes(self):
        if not self.ag_kesme_durumu:
            print("Ağları kesme modu aktifleştiriliyor...")
            self.ag_kesme_durumu = True
            time.sleep(1)
            print("Ağları kesme modu aktifleştirildi.")
        else:
            print("Ağları kesme modu zaten aktif.")

    def teknoloji_etkisiz_hale_getir(self):
        if not self.teknoloji_etkisiz_durumu:
            print("Teknolojik aletleri etkisiz hale getirme modu aktifleştiriliyor...")
            self.teknoloji_etkisiz_durumu = True
            time.sleep(1)
            print("Teknolojik aletleri etkisiz hale getirme modu aktifleştirildi.")
        else:
            print("Teknolojik aletleri etkisiz hale getirme modu zaten aktif.")

    def termal_sensör_aktifle(self):
        if not self.thermal_sensör:
            print("Termal sensör aktifleştiriliyor...")
            self.thermal_sensör = True
            time.sleep(1)
            print("Termal sensör aktifleştirildi.")
        else:
            print("Termal sensör zaten aktif.")

    def hizli_algilama_aktifle(self):
        if not self.hızlı_algılama:
            print("Hızlı algılama modu aktifleştiriliyor...")
            self.hızlı_algılama = True
            time.sleep(1)
            print("Hızlı algılama modu aktifleştirildi.")
        else:
            print("Hızlı algılama modu zaten aktif.")

if __name__ == "__main__":
    robot = AskeriRobot()
    while True:
        robot.dinle_ve_anla()