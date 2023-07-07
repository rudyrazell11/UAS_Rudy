import matplotlib.pyplot as plt
        
year_1 = [2016, 2017, 2018, 2019, 2020, 2021]
population_1 = [42, 43, 45, 47, 48, 50]
        
year_2 = [2016, 2017, 2018, 2019, 2020, 2021]
population_2 = [43, 43, 44, 44, 45, 45]
        
plt.plot(year_1, population_1, marker='o', linestyle='--', color='g', label='Indonesia')
plt.plot(year_2, population_2,  marker='d', linestyle='-', color='r', label='Malaysia')
        
plt.xlabel('Tahun')
plt.ylabel('Populasi Penduduk')
plt.title('Jumlah Penduduk Negara Malaysia vs Indonesia')
plt.show()