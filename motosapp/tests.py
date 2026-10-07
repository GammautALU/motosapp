from django.test import TestCase
from django.urls import reverse

from .models import Moto


class CrearMotoViewTests(TestCase):
    def test_crear_moto_muestra_el_formulario(self):
        response = self.client.get(reverse('crear_moto'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<h2>Ingresar Nueva Moto</h2>')
        self.assertContains(response, 'name="nombre"')
        self.assertContains(response, 'name="marca"')

    def test_crear_moto_guarda_y_vuelve_a_la_lista(self):
        response = self.client.post(
            reverse('crear_moto'),
            {
                'nombre': 'Moto de prueba',
                'marca': 'Marca de prueba',
                'anio': 2024,
                'cilindrada': 250,
                'precio': 3000,
            },
        )

        self.assertRedirects(response, reverse('lista_motos'))
        self.assertTrue(Moto.objects.filter(nombre='Moto de prueba').exists())


class EliminarMotoViewTests(TestCase):
    def setUp(self):
        self.moto = Moto.objects.create(
            nombre='Moto de prueba',
            marca='Marca de prueba',
            anio=2024,
            cilindrada=250,
            precio=3000,
        )

    def test_eliminar_moto_muestra_confirmacion(self):
        response = self.client.get(
            reverse('eliminar_moto', args=[self.moto.pk])
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Confirmar Eliminación')
        self.assertContains(response, 'Moto de prueba')

    def test_eliminar_moto_elimina_y_vuelve_a_la_lista(self):
        response = self.client.post(
            reverse('eliminar_moto', args=[self.moto.pk])
        )

        self.assertRedirects(response, reverse('lista_motos'))
        self.assertFalse(Moto.objects.filter(pk=self.moto.pk).exists())
