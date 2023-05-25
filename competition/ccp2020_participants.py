def get_participants():
    raw = [
        'rahusiens|Rahusien Salim|class|major',
        'haikalvidya|Vidya Haikal Imad Fadly|class|major',
        'putuuu|Putu Teguh Widjaya|class|major',
        'rizkyfransisca|Kadek Rizky Fransisca Putra|class|major',
        'BEBEX|Albertus Ivan Martino|class|major',
        'karrazaan|Imam Rafiif Arrazaan|class|major',
        'MartabakKeju|Rayhan Zanzabila|class|major',
        'nuhmms23|Nuh Mahardhika Matien Siam|class|major',
        'alfianmf|Alfian Maulana Fardhani|class|major',
        'Kurorin|Putri Nabila|class|major',
        'rizalwidyananda|Rizal Widyananda|class|major',
        'helmy6941|Muhammad Helmy Faishal|class|major',
        'bagushariyadi467|Bagus Hariyadi|class|major',
        'faiz_rofi|Faiz Rofi Hencya|class|major',
        'hernandaeka3|Hernanda Eka Prasetyo|class|major',
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