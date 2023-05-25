def get_participants():
    raw = [
        'blinfoldking|Ganesha Danu Enastika|Kelas|Prodi',
        'altair72|Muhammad Abdurrohman Al Fatih|Kelas|Prodi',
        'ryuaka|Anas Rasyid|Kelas|Prodi',
        'AhsanAtha|Ahsan Athallah|Kelas|Prodi',
        'mdmahardhika|Dwiantara Mahardhika|Kelas|Prodi',
        'jordiyapz|Jordi Yaputra|Kelas|Prodi',
        'amseels|Nuril Kaunaini Rofiatunnajah|Kelas|Prodi',
        'zasiem|Erza Putra|Kelas|Prodi',
        'muftialies|Mufti Alie Satriawan|Kelas|Prodi',
        'putra16_mp|Muhammad Mukhtar|Kelas|Prodi',
        'trijakapamungkas|Tri Jaka Pamungkas|Kelas|Prodi',
        'nuzulaz10|Nuzula Zamzami|Kelas|Prodi',
        'bbeyonce|1301174100|Kelas|Prodi',
        'syitilv|Syiti Liviani|Kelas|Prodi',
        'adzkar|Adzkar Fauzie|Kelas|Prodi',
        'fadhiil_nugroho|Fadhiil Nugroho|Kelas|Prodi',
        'OMA80|Nabil Anwar Fauzi|Kelas|Prodi',
        'novitaguok|Novita Guok|Kelas|Prodi',
        'rzkyrr|Rizki Ramadhan|Kelas|Prodi',
        'zetaraehan|M Raehan Akbar|Kelas|Prodi',
        'zarszzntunx|Ganjar Gingin Tahyudin|Kelas|Prodi',
        'firdausai|Firdaus Indradhirmaya|Kelas|Prodi',
        'rakhmat_rifaldy1|Rakhmat Rifaldy|Kelas|Prodi',
        'gregoriusvito|Gregorius Vito|Kelas|Prodi',
        'djooo|Setyo Adji|Kelas|Prodi',
        'galmayda|Gabriel Almayda|Kelas|Prodi',
        'tiwaramdhani|Tiwa Ramdhani|Kelas|Prodi',
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