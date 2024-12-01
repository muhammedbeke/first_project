import tkinter as tk
from tkinter import ttk
from veri_yonetimi import VeriYonetimi
from tkinter import messagebox

class FilmDiziYonetimi:
    def __init__(self,window):
        self.pencere=window
        self.pencere.geometry("600x400+600+200")
        self.pencere.title("FİLM-DİZİ YÖNETİM")
        self.veri_yonetimi = VeriYonetimi()

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

        self.text1 = tk.Text(self.pencere, width=25, height=8)
        self.text1.grid(row=4, column=1,pady=15)

        self.text2 = tk.Text(self.pencere, width=40, height=10)
        self.text2.grid(row=1, column=2, rowspan=4, padx=10,sticky="n")

        self.text3 = tk.Text(self.pencere, width=30, height=5)
        self.text3.grid(row=4, column=2,sticky="s",pady=50)

        self.box1 = ttk.Combobox(self.pencere, values=["film", "dizi"])
        self.box1.grid(row=1, column=1)

        self.box2 = ttk.Combobox(self.pencere, values=["izlendi", "izlenecek", "bekleniyor"])
        self.box2.grid(row=2, column=1)

        self.box3 = ttk.Combobox(self.pencere, values=["1", "2", "3", "4", "5"])
        self.box3.grid(row=3, column=1)

        self.listeyi_guncelle()

        self.button1 = tk.Button(self.pencere, text="EKLE", command=self.ekle)
        self.button1.grid(row=5, column=1,padx=3,sticky="w")

        self.button2 = tk.Button(self.pencere, text="SİL", command=self.sil)
        self.button2.grid(row=5, column=1,padx=(60,0),sticky="w")

        self.button3 = tk.Button(self.pencere, text="ARA", command=self.arama)
        self.button3.grid(row=5, column=1,padx=(40,0))

        self.button4 = tk.Button(self.pencere, text="Düzenle", command=self.duzenle)
        self.button4.grid(row=5,column=1,sticky="e")

        self.button5= tk.Button(self.pencere,text="Not Göster",command=self.goster)
        self.button5.grid(row=5,column=2)

    def listeyi_guncelle(self):
        self.text2.delete(1.0, tk.END)
        for i, veri in enumerate(self.veri_yonetimi.veriler):
            self.text2.insert(tk.END, f"{i + 1}. {veri['ad']} ({veri['durum']},{veri['tur']},{veri['yildiz']} yıldız)\n")

    def ekle(self):
        ad = self.entry1.get()
        tur = self.box1.get()
        durum = self.box2.get()
        yildiz = self.box3.get()
        notlar = self.text1.get("1.0", tk.END).strip()
        if not ad or not tur or not durum or not yildiz:
            messagebox.showwarning("Uyarı", "Tüm alanları doldurun!")
            return
        yeni_icerik = {
            "ad": ad,
            "tur": tur,
            "durum": durum,
            "yildiz": int(yildiz),
            "not": notlar,
        }
        messagebox.showinfo("Başarılı", "Film/Dizi başarıyla eklendi!")
        self.veri_yonetimi.ekle(yeni_icerik)
        self.listeyi_guncelle()
        self.entry1.delete(0, tk.END)
        self.box1.set('')
        self.box2.set('')
        self.box3.set('')
        self.text1.delete("1.0", tk.END)

    def sil(self):

        secili_satir = self.text2.get(tk.SEL_FIRST, tk.SEL_LAST)
        if not secili_satir:
            messagebox.showwarning("Uyarı", "Silmek için bir öğe seçin!")
            return
        if secili_satir:
            for i, veri in enumerate(self.veri_yonetimi.veriler):
                if f"{i + 1}. {veri['ad']} ({veri['durum']},{veri["tur"]},{veri['yildiz']} yıldız)" == secili_satir.strip():
                    self.veri_yonetimi.sil(i)
                    break
            self.listeyi_guncelle()
        messagebox.showinfo("Başarılı", "Film/Dizi başarıyla silindi!")

    def arama(self):
        arama_terimi = self.text2.tag_ranges(tk.SEL)
        if not arama_terimi:
            messagebox.showwarning("Uyarı", "Lütfen arama terimi seçin.")
            return
        arama_terimi =self.text2.get(tk.SEL_FIRST, tk.SEL_LAST).strip().lower()
        metin = self.text2.get("1.0", tk.END).lower()
        secili_baslangic = self.text2.index(tk.SEL_FIRST)
        satir_numarasi = secili_baslangic.split(')')[0]
        satir_numarasi=int(eval(satir_numarasi))
        if arama_terimi in metin:
            messagebox.showinfo("Sonuç:", "{}.indexde bulundu".format(satir_numarasi))
        else:
            messagebox.showwarning("Sonuç:", "Aranan terim bulunamadı.")

    def duzenle(self):
        secili_satir = self.text2.tag_ranges(tk.SEL)
        if not secili_satir:
            messagebox.showwarning("Uyarı", "Lütfen bir satır seçin.")
            return
        secili_satir = self.text2.get(tk.SEL_FIRST, tk.SEL_LAST).strip()

        if secili_satir:
            secili_veri = None
            for i, veri in enumerate(self.veri_yonetimi.veriler):
                if f"{i + 1}. {veri['ad']} ({veri['durum']},{veri["tur"]},{veri['yildiz']} yıldız)" == secili_satir:
                    secili_veri = veri
                    break
            if secili_veri:
                ad = self.entry1.get()
                tur = self.box1.get()
                durum = self.box2.get()
                yildiz = self.box3.get()
                notlar = self.text1.get("1.0", tk.END).strip()
                if not ad or not tur or not durum or not yildiz:
                    messagebox.showwarning("Uyarı", "Tüm alanları doldurun!")
                    return
                secili_veri["ad"] = ad
                secili_veri["tur"] = tur
                secili_veri["durum"] = durum
                secili_veri["yildiz"] = int(yildiz)
                secili_veri["not"] = notlar
                self.listeyi_guncelle()
                self.entry1.delete(0, tk.END)
                self.box1.set('')
                self.box2.set('')
                self.box3.set('')
                self.text1.delete("1.0", tk.END)


    def goster(self):

         secili_satir = self.text2.get(tk.SEL_FIRST, tk.SEL_LAST).strip()
         if not secili_satir:
             messagebox.showwarning("Uyarı", "Lütfen bir öğe seçin.")
             return
         secili_veri = None
         for i, veri in enumerate(self.veri_yonetimi.veriler):
             veri_str = f"{i + 1}. {veri['ad']} ({veri['durum']},{veri["tur"]},{veri['yildiz']} yıldız)"
             if veri_str.lower() == secili_satir.lower():
                 secili_veri = veri
                 break
         if secili_veri:
             self.text3.delete("1.0", tk.END)
             self.text3.insert(tk.END, f"Notlar: {secili_veri['not']}\n")


