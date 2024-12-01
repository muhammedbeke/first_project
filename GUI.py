import tkinter as tk
from tkinter import ttk
from veri_yonetimi import VeriYonetimi
from tkinter import messagebox


class FilmDiziYonetimi:
    def __init__(self,root):
        self.pencere=root
        self.pencere.geometry("600x400+600+200")
        self.pencere.title("FİLM-DİZİ YÖNETİM")

        self.veri_yonetimi = VeriYonetimi()

        # Widgetları oluştur
        self.etiket1 = tk.Label(self.pencere, text="AD:")
        self.etiket1.grid(row=0, column=0, pady=10)

        self.etiket2 = tk.Label(self.pencere, text="TÜR:")
        self.etiket2.grid(row=1, column=0, pady=10)

        self.etiket3 = tk.Label(self.pencere, text="DURUM:")
        self.etiket3.grid(row=2, column=0, pady=10)

        self.etiket4 = tk.Label(self.pencere, text="YILDIZ:")
        self.etiket4.grid(row=3, column=0, pady=10)

        self.etiket5 = tk.Label(self.pencere, text="NOTLAR:")
        self.etiket5.grid(row=4, column=0, pady=10)

        self.etiket6 = tk.Label(self.pencere, text="Filmler/Diziler:")
        self.etiket6.grid(row=0, column=2)

        self.entry1 = tk.Entry(self.pencere, width=30)
        self.entry1.grid(row=0, column=1)

        self.text1 = tk.Text(self.pencere, width=25, height=10)
        self.text1.grid(row=4, column=1)

        self.text2 = tk.Text(self.pencere, width=35, height=20)
        self.text2.grid(row=1, column=2, rowspan=4, padx=10)

        self.box1 = ttk.Combobox(self.pencere, values=["film", "dizi"])
        self.box1.grid(row=1, column=1)

        self.box2 = ttk.Combobox(self.pencere, values=["izlendi", "izlenecek", "bekleniyor"])
        self.box2.grid(row=2, column=1)

        self.box3 = ttk.Combobox(self.pencere, values=["1", "2", "3", "4", "5"])
        self.box3.grid(row=3, column=1)

        self.listeyi_guncelle()

        self.button1 = tk.Button(self.pencere, text="EKLE", command=self.ekle)
        self.button1.grid(row=5, column=1, padx=10, sticky="w")

        self.button2 = tk.Button(self.pencere, text="SİL", command=self.sil)
        self.button2.grid(row=5, column=1, padx=5)
        self.button3 = tk.Button(self.pencere, text="ARA", command=self.arama)
        self.button3.grid(row=5, column=1, padx=10,sticky="e")

    def listeyi_guncelle(self):
        self.text2.delete(1.0, tk.END)
        for i, veri in enumerate(self.veri_yonetimi.veriler):
            self.text2.insert(tk.END, f"{i + 1}. {veri['ad']} ({veri['durum']}, {veri['yildiz']} yıldız)\n")

    def ekle(self):
        ad = self.entry1.get()
        tur = self.box1.get()
        durum = self.box2.get()
        yildiz = self.box3.get()
        notlar = self.text1.get("1.0", tk.END).strip()

        yeni_icerik = {
            "ad": ad,
            "tur": tur,
            "durum": durum,
            "yildiz": int(yildiz),
            "not": notlar,
        }

        self.veri_yonetimi.ekle(yeni_icerik)
        self.listeyi_guncelle()

        # Alanları temizle
        self.entry1.delete(0, tk.END)
        self.box1.set('')
        self.box2.set('')
        self.box3.set('')
        self.text1.delete("1.0", tk.END)

    def sil(self):
        try:
            secili_satir = self.text2.get(tk.SEL_FIRST, tk.SEL_LAST)
            if secili_satir:
                for i, veri in enumerate(self.veri_yonetimi.veriler):
                    if f"{i + 1}. {veri['ad']} ({veri['durum']}, {veri['yildiz']} yıldız)" == secili_satir.strip():
                        self.veri_yonetimi.sil(i)
                        break
                self.listeyi_guncelle()
        except tk.TclError:
            print("Seçili bir satır yok.")
    def arama(self):
        arama_terimi = secili_satir = self.text2.get(tk.SEL_FIRST, tk.SEL_LAST).strip().lower()
        metin = self.text2.get("1.0", tk.END).lower()

        if arama_terimi in metin:
            messagebox.showinfo("Sonuç", "Aranan terim bulundu!")
        else:
            messagebox.showwarning("Sonuç", "Aranan terim bulunamadı.")

