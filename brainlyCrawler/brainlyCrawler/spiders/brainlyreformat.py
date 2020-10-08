class BrainlyReformat:
    def transform_int(self, data):
        for item in data:
            if 'pertanyaan' in item:
                item = item.replace('pertanyaan ', '')
                if '.' in item:
                    item = item.replace('.', '')
                    item = item.replace(' rb', '')
                return int(item)
            elif 'teman' in item:
                item = item.replace('teman ', '')
                if '.' in item:
                    item = item.replace('.', '')
                    item = item.replace(' rb', '')
                return int(item)
            elif 'jawaban' in item:
                item = item.replace('jawaban ', '')
                if '.' in item:
                    item = item.replace('.', '')
                    item = item.replace(' rb', '')
                return int(item)
            else:
                item = item.replace('.', '')
                item = item.replace(' rb', '')
                return int(item)


    def subject_format(self, subjects_data):
        total_subjects_data = {
                'total_tercerdas_matematika': 0,
                'total_tercerdas_bindo': 0,
                'total_tercerdas_ppkn': 0,
                'total_tercerdas_ips': 0,
                'total_tercerdas_biologi': 0,
                'total_tercerdas_fisika': 0,
                'total_tercerdas_sejarah': 0,
                'total_tercerdas_binggris': 0,
                'total_tercerdas_seni': 0,
                'total_tercerdas_kimia': 0,
                'total_tercerdas_geografi': 0,
                'total_tercerdas_ti': 0,
                'total_tercerdas_ekonomi': 0,
                'total_tercerdas_barab': 0,
                'total_tercerdas_daerah': 0,
                'total_tercerdas_penjaskes': 0,
                'total_tercerdas_sosiologi': 0,
                'total_tercerdas_blain': 0,
                'total_tercerdas_wirausaha': 0,
                'total_tercerdas_akuntansi': 0,
                'total_tercerdas_bjepang': 0,
                'total_tercerdas_bmandarin': 0,
                'total_tercerdas_bperancis': 0,
                'total_jawaban_matematika': 0,
                'total_jawaban_bindo': 0,
                'total_jawaban_ppkn': 0,
                'total_jawaban_ips': 0,
                'total_jawaban_biologi': 0,
                'total_jawaban_fisika': 0,
                'total_jawaban_sejarah': 0,
                'total_jawaban_binggris': 0,
                'total_jawaban_seni': 0,
                'total_jawaban_kimia': 0,
                'total_jawaban_geografi': 0,
                'total_jawaban_ti': 0,
                'total_jawaban_ekonomi': 0,
                'total_jawaban_barab': 0,
                'total_jawaban_bdaerah': 0,
                'total_jawaban_penjaskes': 0,
                'total_jawaban_sosiologi': 0,
                'total_jawaban_blain': 0,
                'total_jawaban_wirausaha': 0,
                'total_jawaban_akuntansi': 0,
                'total_jawaban_bjepang': 0,
                'total_jawaban_bmandarin': 0,
                'total_jawaban_bperancis': 0,
        }

        subject_libraries = [
            'Matematika', 'B. Indonesia', 'PPKn', 'IPS', 'Biologi', 
            'Fisika', 'Sejarah', 'B. inggris', 'Seni', 'Kimia', 'Geografi', 
            'TI', 'Ekonomi', 'B. Arab', 'B. Daerah', 'Penjaskes', 'Sosiologi', 
            'Bahasa lain', 'Wirausaha', 'Akuntansi', 'B. jepang', 'B. mandarin', 'B. perancis'
            ]

        result_j = 'total_jawaban_'
        result_t = 'total_tercerdas_'
        
        for key in subjects_data.keys():
            if key in subject_libraries: 
                subjects = subjects_data[key]
                subjects = subjects.split(' (')
                key = key.lower()
                key = key.replace('. ', '')
                
                for subject in subjects:
                    if 'Jawaban' in subject:
                        data = subject.replace(' Jawaban', '')
                        sub_key = result_j + key
                        total_subjects_data[sub_key] = int(data)

                    elif 'Tercerdas' in subject:
                        data = subject.replace(' Tercerdas)', '')
                        sub_key = result_t + key
                        total_subjects_data[sub_key] = int(data)
            else:
                key = key.lower()
                key = key.replace('. ', '')
                sub_key_j = result_j + key
                sub_key_t = result_t + key
                total_subjects_data[sub_key_j] = 0
                total_subjects_data[sub_key_t] = 0

        return total_subjects_data



    def information_format(self, information_data):
        total_info_data = {
            'poin': 0,
            'tingkat': 0,
            'bergabung': 0,
        }

        info_libraries = ['Poin:', 'Tingkat:', 'Bergabung:']  


        for key in info_libraries:
            if  key in information_data.keys():
                if 'Poin' in key:
                    val = information_data[key]
                    key = key.lower()
                    key = key.replace(':', '')
                    val = val.replace('.', '')
                    total_info_data[key] = int(val)

                else:
                    val = information_data[key]
                    key = key.lower()
                    key = key.replace(':', '')
                    total_info_data[key] = val
                
            else:
                key = key.lower()
                key = key.replace(':', '')
                total_info_data[key] = 0
                total_info_data['tingkat'] = 'tidak diisi'
                total_info_data['bergabung'] = 'tidak diisi'
        
        return total_info_data
            