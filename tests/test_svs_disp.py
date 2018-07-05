import unittest
import subprocess

from base import SD_VM_Local_Test


class SD_SVS_DISP_Tests(SD_VM_Local_Test):
    def setUp(self):
        self.vm_name = "sd-svs-disp"
        super(SD_SVS_DISP_Tests, self).setUp()

    def test_grsec_kernel(self):
        cmd = ["uname", "-r"]
        p = subprocess.check_output(cmd)
        self.assertEqual(p, "4.14.53-grsec")

def load_tests(loader, tests, pattern):
    suite = unittest.TestLoader().loadTestsFromTestCase(SD_SVS_DISP_Tests)
    return suite
