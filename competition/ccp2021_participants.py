def get_participants():
    raw = [
        'faridaarum|Farida Arum Parwati|IF-44-08|S1 Informatika',
        'zachariabachtiar|Zacharia Bachtiar|SE-44-02|S1 Rekayasa Perangkat Lunak',
        'tangguhlaksana0|Tangguh Laksana|SE-45-01|S1 Rekayasa Perangkat Lunak',
        'ghiyats02|Muhammad Ghiyaats Daffa|IF-44-11|S1 Informatika',
        'skootydack|Azarel Grahandito Adi|IF-45-08|S1 Informatika',
        'fitrahidayat1|Muhammad Ramdhan Fitra Hidayat|IF-45-10|S1 Informatika',
        'aryaashari100|Arya Dul Fitra Ashari|SE-45-02|S1 Rekayasa Perangkat Lunak',
        'naufalhawari|Muhammad Naufal Hawari|IF-45-01|S1 Informatika',
        'mufidu|Muhammad Mufid Utomo|IF-44-01|Informatika',
        'shidqifadhlu|Shidqi Fadhlurrahman Yusri|IF-44-10|S1 Informatika',
        'khalilullah_alf1|Khalilullah Al Faath|IF-44-08|S-1 Informatika',
        'me_billie|Muhammad Billie Elian|IF-45-12|Informatika',
        'fauzanrizqimuha1|Fauzan Rizqi Muhammad|IF-45-INT|S1 Informatika',
        'luthfinovra|Luthfi Novra|IF-45-12|Informatika',
        'rafliprnm|Rafli Purnama Putra|IT-44-01|S1 Teknologi Informasi',
        'Acierz|Rayhan Risq Arya Brinanta|IF-44-09|S1 Informatika',
        'amril_auvi|Muhammad Auvi Amril|SI-44-04|Sistem Informasi',
        'bonifasiustrg|Bonifasius Tarigan|IF-45-12|S1 Informatika',
        'mhyubr|Muhammad Ayyub Ramli|SI-44-01|S1 Sistem Informasi',
        'edwardbilly|Edward Billy Hadipuspito|IF-44-11|S1 Informatika',
        'r4ja_malam|Ridwan Maulana Tanjung|TF-45-01|Teknik Fisika',
        'drunkwhales|Hidayat Taufiqur Rahmah Achmad|IF-44-07|S1 Informatika',
        'galihakbar_ga91|Galih Akbar Nugraha|IF-45-07|S1 Informatika',
        'iwahyu809|Indra Wahyu|IF-45-05|Infotmatika',
        'johanesrn|Johanes Raphael Nandaputra|IF-44-01|Informatika',
        'aldimuhfar|Aldi Muhammad Farhan|IF-45-01|S1 Informatika',
        'RadDe|Radiana De Salma|IT-45-01|S1 Teknologi Informasi',
        'Raychans|Fasya Raihan Maulana|SE-45-02|S1 Rekayasa Perangkat Lunak',
        'suepppppppppp111|Surya Aulia|SE-45-02|S1 Rekayasa Perangkat Lunak',
        'glorianatasya|Gloria Natasya Irene Sidebang|IF-45-10|S1 Informatika',
        'darreljohan162|Darrel Johan|IT-4404|Teknologi Informasi',
        'ferdyfadriansyah|Ferdy Fadriansyah|IT 44 04|Teknologi Informasi',
        'muhammadrizqia|Muhammad Rizqi Anshari|SE-44-03|S1 Rekayasa Perangkat Lunak',
        'mulyaargyanto|Farhan Mulya Argyanto|SE-45-01|S1 Rekayasa Perangkat Lunak',
        'muhamad_rizqiab1|Muhamad Rizqi Abdillah|IT-44-04|S1 Teknologi Informasi',
        'brillianadhiyak1|Brillian Adhiyaksa Kuswandi|SI-44-INT|S1 Sistem Informasi',
        'auliarifki45|Aulia Riefqi Ardana|IF4403|Informatika',
        'prinsnnuzeren|Prins Naval Nuzeren|IF-45-05|S1 Informatika',
        'pelingprayoga|Ida Bagus Peling Prayoga|IT-44-01|S1 Teknologi Informasi',
        'gustavsayudha|Gustav Beka Sayudha|IF-45-INT|S1 Informatika',
        '4fortunezw|Agung Hadi Winoto|DS4503|Data Sains',
        'orvalavala|Orvala Azzurri Madhyastha|SE-44-02|Rekayasa Perangkat Lunak',
        'fadhlyalfarizi30|Fadhly Al-farizi|IF-44-11|S1 Informatika',
        'aryyabp|Aryya Bagus Padmanawijaya|IF-44-12|S1 Informatika',
        'herjanto|Herjanto Janawisuta|IF-44-08|S1 Informatika',
        'Ananthrax|Anandito Satria Asyraf|IF - 45 - 06|S1 Informatika',
        'aadhistii|Adhistianita Safira Husna|IF-45-09|S1 Informatika',
        'anisaadelya|Anisa Adelya Ayuputri|IF-44-08|Informatika',
        'miharu_tsuna|Miharu Idhan Fikriansyah|IT-44-01|Teknologi Informasi',
        'adinugraha|Adinugraha Dharmaputra|IF-44-12|Informatika',
        'raihanramadhan|Muhamad Raihan Ramadhan|IT-44-03|S1 Teknologi Informasi',
        'rofidragon71|Ahmad Sidik Rofiudin|SI-44-06|Sistem Informasi',
        'jasonn1|Jason Hasudungan Sitorus|IF-45-03|Informatika',
        'jayadiningrat|Aria Reyhan Jayadiningrat|IF-44-07|S1 Informatika',
        'vaniaamadea_va|Vania Amadea|IF-44-08|S1 Informatika',
        'exploiter_47|Rafidhia Haikal Pasya|SE-45-01|S1 Rekayasa Perangkat Lunak',
        'daryrama|Dary Ramadhan Abdussalam|SI-44-06|Sistem Informasi',
        'kelvynlukito|Kelvyn Lukito|IF-44-08|S1 Informatika',
        'muhfuad|Muhammad Fuad Abdullah|IF-45-01.1 PJJ|Informatika',
        'khalifardy|Khalifardy Miqdarsah|IF-45-02.1PJJ|Teknik Informatika',
        'abdul_adf|Abdul Daffa Fakhrudin|IF-44-11|S1 Informatika',
        'zadosaadip|Zadosaadi Brahmantio Purwanto|DS-45-02|S1 Data Sains',
        'afeefradithya|Afeef Radithya Rashid|DS-45-03|S1 Data Sains',
        'valternatean13|Valent Fauzan Al Rasyid|IF-45-08|S1 Informatika',
        'brolss|Brillyando Magathan Achmad|IF-44-06|S1 Informatika',
        'raflisusanto|Muhamad Rafli Susanto|IF-44-07|S1 Informatika',
        'Alvin Sibuea|Alvin Tolopan Armando Sibuea|IF-44-08|Informatika',
        'TupacSyukur|Rifqi Aulia Rahman|IF-44-INT|S1 Informatika Int',
        'rin4th|Rizal Nur|IF-45-07|S1 Informatika',
        'harviankhusnan|Harvian Khusnan Hafidz|IF-44-08|S1 Informatika',
        'syahkevinm|Kevin Muhammad Syah|IF-44-02|S1 Informatika',
        'trooulala|M. Sutlhon Sayid Abdurrohman|IF-44-09|S1 Informatika',
        'mrizkyfirdaus|Muhammad Rizky Firdaus|IF-44-04|S1 Informatika'
    ]
    return [
        {
            'hackerrank': p[0],
            'name': p[1],
            'class': p[2],
            'major': p[3],
        }
        for p in [r.split('|') for r in raw]
    ]