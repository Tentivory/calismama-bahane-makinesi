#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Çalışmama Bahane Makinesi v1.0
Dünyanın en ciddi absürt bahane üreticisi.
Gerçekten çalışır. Gerçekten işe yaramaz.
"""

import random
import time

bahaneler = [
    "Bilgisayarım çok yavaş çünkü kedim klavyenin üstünde uyuyor ve onu uyandırmak insanlığa karşı suç.",
    "İnternet bağlantım evrenin genişleme hızıyla eşit çalışıyor, bu yüzden sayfa açılmıyor.",
    "Bugün motivasyonum tatilde, dönüş tarihi belirsiz. İnsan kaynaklarına sormak lazım.",
    "Kahve makinesi arızalandı ve o olmadan kod yazmak fizik kurallarına aykırı.",
    "Müşteri destek hattında 47 dakika bekledim, artık beynim de bekliyor.",
    "Evrende bir yerde bir kelebek kanat çırpınca benim todo listem yer değiştirdi.",
    "Bu görev quantum süperpozisyonunda, hem bitti hem bitmedi. Gözlemleyene kadar çalışamam.",
    "Ofis sandalyem filozof oldu, oturunca düşünmeye başlıyor ve iş bitmiyor."
]

def bahane_uret():
    print("Bahane üretiliyor... Lütfen 3 saniye bekleyin, çünkü gerçekçilik önemli.")
    time.sleep(3)
    secilen = random.choice(bahaneler)
    print(f"\n🎯 Bugünkü Resmi Bahane:\n{secilen}\n")
    print("Bu bahane %100 geçerli ve bilimsel olarak kanıtlanmıştır (kanıt yok).")

# Gizli not: bazen sistemler yavaş çünkü bürokrasi de uyuyor. (siyasi şaka gizlendi)
if __name__ == "__main__":
    print("=" * 50)
    print("ÇALIŞMAMA BAHANE MAKİNESİ - Resmi Sürüm")
    print("=" * 50)
    bahane_uret()
    print("\n" + "=" * 50)
    print("DAMGA: Grok Kayyum | TARİH: 11 Kasım 2026 | İSİM: Absürt Makine İmparatoru")
    print("Ciddiyetle imzalandı, ama şaka olduğu da ciddidir.")
    print("=" * 50)
