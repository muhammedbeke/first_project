import json
import os

class VeriYonetimi:
    DATA_FILE = "filmler_ve_diziler.json"

    def __init__(self):
        self.veriler = []
        self.veri_yukle()

    def veri_yukle(self):
        """JSON dosyasından verileri yükler."""
        if os.path.exists(self.DATA_FILE):
            with open(self.DATA_FILE, "r") as dosya:
                self.veriler = json.load(dosya)
        else:
            self.veriler = []

    def veri_kaydet(self):
        """Verileri JSON dosyasına kaydeder."""
        with open(self.DATA_FILE, "w") as dosya:
            json.dump(self.veriler, dosya, indent=4)

    def ekle(self, yeni_icerik):
        """Yeni bir film veya dizi ekler."""
        self.veriler.append(yeni_icerik)
        self.veri_kaydet()

    def sil(self, index):
        """Belirtilen indeksteki içeriği siler."""
        if 0 <= index < len(self.veriler):
            del self.veriler[index]
            self.veri_kaydet()
