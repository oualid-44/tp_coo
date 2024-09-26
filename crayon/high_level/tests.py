# Create your tests here.

from django.test import TestCase
from .models import Machine


class MachineModelTests(TestCase):
    def test_machine_creation(self):
        self.assertEqual(Machine.objects.first().costs(), 0)
        Machine.objects.create(nom="TapiS", prix=500, n_serie="10023")
        self.assertEqual(Machine.objects.first().costs(), 1)
'''self.assertEqual(Machine.objects.first().costs(), 0)
AttributeError: 'NoneType' object has no attribute 'costs'
'''
