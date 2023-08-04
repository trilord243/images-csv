import csv
import os
import requests


csv_file = './products.csv'


directory = r'C:\\Users\\Escal\Documents\\images-plaza'


if not os.path.exists(directory):
    os.makedirs(directory)


with open(csv_file, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        
        field = row[8]

       
        field = field.lstrip('0')

        
        url = f'https://www.elplazas.com/DB-IMG-PRODUCT/{field}/img.jpg'

        # Intenta descargar la imagen
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            # Define el nombre del archivo y la ruta completa
            filename = os.path.join(directory, f'{field}.jpg')

            # Abre el archivo en modo de escritura binaria y guarda los datos de la imagen
            with open(filename, 'wb') as img_file:
                for chunk in response.iter_content(chunk_size=128):
                    img_file.write(chunk)

            print(f'Imagen guardada en {filename}')
        else:
            print(f'Error al descargar la imagen de {url}, código de estado: {response.status_code}')
