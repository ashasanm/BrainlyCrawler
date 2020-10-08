# total_subjects_data = {
#         'total_tercerdas_matematika': 0,
#         'total_tercerdas_bindo': 0,
#         'total_tercerdas_ppkn': 0,
#         'total_tercerdas_ips': 0,
#         'total_tercerdas_biologi': 0,
#         'total_tercerdas_fisika': 0,
#         'total_tercerdas_sejarah': 0,
#         'total_tercerdas_binggris': 0,
#         'total_tercerdas_seni': 0,
#         'total_tercerdas_kimia': 0,
#         'total_tercerdas_geografi': 0,
#         'total_tercerdas_ti': 0,
#         'total_tercerdas_ekonomi': 0,
#         'total_tercerdas_barab': 0,
#         'total_tercerdas_daerah': 0,
#         'total_tercerdas_penjaskes': 0,
#         'total_tercerdas_sosiologi': 0,
#         'total_tercerdas_blain': 0,
#         'total_tercerdas_wirausaha': 0,
#         'total_tercerdas_akuntansi': 0,
#         'total_tercerdas_bjepang': 0,
#         'total_tercerdas_bmandarin': 0,
#         'total_tercerdas_bperancis': 0,
#         'total_jawaban_matematika': 0,
#         'total_jawaban_bindo': 0,
#         'total_jawaban_ppkn': 0,
#         'total_jawaban_ips': 0,
#         'total_jawaban_biologi': 0,
#         'total_jawaban_fisika': 0,
#         'total_jawaban_sejarah': 0,
#         'total_jawaban_binggris': 0,
#         'total_jawaban_seni': 0,
#         'total_jawaban_kimia': 0,
#         'total_jawaban_geografi': 0,
#         'total_jawaban_ti': 0,
#         'total_jawaban_ekonomi': 0,
#         'total_jawaban_barab': 0,
#         'total_jawaban_bdaerah': 0,
#         'total_jawaban_penjaskes': 0,
#         'total_jawaban_sosiologi': 0,
#         'total_jawaban_blain': 0,
#         'total_jawaban_wirausaha': 0,
#         'total_jawaban_akuntansi': 0,
#         'total_jawaban_bjepang': 0,
#         'total_jawaban_bmandarin': 0,
#         'total_jawaban_bperancis': 0,
# }

# subjects_data = {
#     'Penjaskes': '2 Jawaban', 
#     'Fisika': '1 Jawaban', 
#     'PPKn': '1 Jawaban', 
#     'IPS': '1 Jawaban'
#     }

# subject_libraries = [
#     'Matematika', 'B. Indonesia', 'PPKn', 'IPS', 'Biologi', 
#     'Fisika', 'Sejarah', 'B. inggris', 'Seni', 'Kimia', 'Geografi', 
#     'TI', 'Ekonomi', 'B. Arab', 'B. Daerah', 'Penjaskes', 'Sosiologi', 
#     'Bahasa lain', 'Wirausaha', 'Akuntansi', 'B. jepang', 'B. mandarin', 'B. perancis'
#     ]

# result_j = 'total_jawaban_'
# result_t = 'total_tercerdas_'

# for key in subjects_data.keys():
#     if key in subject_libraries: 
#         subjects = subjects_data[key]
#         subjects = subjects.split(' (')
#         key = key.lower()
#         key = key.replace('. ', '')
        
#         for subject in subjects:
#             print(subject)
#             if 'Jawaban' in subject:
#                 data = subject.replace(' Jawaban', '')
#                 sub_key = result_j + key
#                 total_subjects_data[sub_key] = data

#             elif 'Tercerdas' in subject:
#                 data = subject.replace(' Tercerdas)', '')
#                 sub_key = result_t + key
#                 total_subjects_data[sub_key] = data
#     else:
#         key = key.lower()
#         key = key.replace('. ', '')
#         sub_key_j = result_j + key
#         sub_key_t = result_t + key
#         total_subjects_data[sub_key_j] = 0
#         total_subjects_data[sub_key_t] = 0

# print(total_subjects_data)