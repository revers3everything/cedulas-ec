# Cédulas-EC

Este repositorio contiene un script en Python que genera todos los posibles números de cédula válidos de Ecuador, utilizando el algoritmo de validación de cédulas ecuatorianas. El script crea un archivo de aproximadamente **1.53 GB** que contiene todos los números de cédula válidos (150 millones de cédulas).

![alt text](image.png)

## Descripción

El **algoritmo de validación de cédulas ecuatorianas** se utiliza para validar la estructura de los números de cédula en Ecuador, garantizando que los dígitos cumplan con las reglas definidas por el Registro Civil. Este script genera sistemáticamente todas las combinaciones posibles de cédulas válidas y las guarda en un archivo.

## Estructura del Proyecto

- `generador_ids.py`: Script principal que genera todas las cédulas válidas.
- `cedulas_validas.txt`: Archivo generado que contiene todas las cédulas válidas (aproximadamente 1.53 GB).

## Uso

Para ejecutar el script y generar el archivo de cédulas válidas, sigue estos pasos:

1. Clona el repositorio:

    ```bash
    git clone https://github.com/tuusuario/cedulas-ec.git
    ```

2. Accede al directorio del repositorio y cambia el path de destino del archivo de salida en "generador_ids.py:

    ```bash
    cd cedulas-ec
    ```

3. Ejecuta el script con Python 3:

    ```bash
    python3 generador_ids.py
    ```

El script generará un archivo llamado `cedulas_validas.txt` en el mismo directorio.

## Requisitos

- **Python 3.x**

El script no requiere librerías externas adicionales, ya que utiliza funcionalidades estándar de Python.

## Algoritmo de Validación

El algoritmo de validación de cédulas ecuatorianas consiste en:

1. Verificar que los dos primeros dígitos correspondan a una provincia válida (entre 01 y 24, o el código especial 30).
2. Aplicar un cálculo con los dígitos impares y pares de la cédula.
3. El último dígito de la cédula es un verificador, calculado a partir de los otros 9 dígitos.

Este script genera todas las combinaciones posibles de cédulas que cumplen con estos criterios y las guarda en un archivo de texto.

## Tamaño del Archivo Generado

El archivo resultante (`cedulas_validas.txt`) tendrá un tamaño aproximado de **1.53 GB**, dado el volumen de combinaciones generadas de un total de 150 millones de cédulas.

## Advertencia

Este script y los datos generados son únicamente con fines educativos o de investigación. El uso indebido de los números de cédula está prohibido por la ley. El autor no se hace responsable del uso inapropiado de la información generada.
