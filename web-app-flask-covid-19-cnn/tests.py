import os
import cv2
import unittest
from app import app, hacer_predicciones

class FlaskTestCase(unittest.TestCase):

    # Comprobar si la página principal se carga correctamente
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # Comprobar si la función hacer_predicciones devuelve una salida válida
    def test_hacer_predicciones(self):
        img_dir = 'static/imagen_prueba.jpg'
        img_arr = cv2.imread(img_dir, cv2.IMREAD_GRAYSCALE)
        resized_arr = cv2.resize(img_arr, (150, 150))
        output = hacer_predicciones(resized_arr)
        self.assertIn(output, ['POSITIVO', 'NEGATIVO'])

if __name__ == '__main__':
    unittest.main()
