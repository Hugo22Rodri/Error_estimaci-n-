from django.test import TestCase
from .views import calcular_errores

class CalculoErroresTests(TestCase):
    def test_calculo_valores_positivos(self):
        error_abs, error_rel, error_porc = calcular_errores(100, 99.5)
        self.assertAlmostEqual(error_abs, 0.5)
        self.assertAlmostEqual(error_rel, 0.005)
        self.assertAlmostEqual(error_porc, 0.5)
        
    def test_valor_real_cero(self):
        error_abs, error_rel, error_porc = calcular_errores(0, 0.1)
        self.assertEqual(error_abs, 0.1)
        self.assertEqual(error_rel, float('inf'))
        self.assertEqual(error_porc, float('inf'))
        
    def test_ambos_cero(self):
        error_abs, error_rel, error_porc = calcular_errores(0, 0)
        self.assertEqual(error_abs, 0)
        self.assertEqual(error_rel, 0)
        self.assertEqual(error_porc, 0)
        
    def test_valores_negativos(self):
        error_abs, error_rel, error_porc = calcular_errores(-100, -99)
        self.assertAlmostEqual(error_abs, 1.0)
        self.assertAlmostEqual(error_rel, 0.01)
        self.assertAlmostEqual(error_porc, 1.0)
        
    def test_aprox_mayor_que_real(self):
        error_abs, error_rel, error_porc = calcular_errores(50, 52)
        self.assertAlmostEqual(error_abs, 2.0)
        self.assertAlmostEqual(error_rel, 0.04)
        self.assertAlmostEqual(error_porc, 4.0)