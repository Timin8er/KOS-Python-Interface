from time import sleep
import telnetlib
import json
import os

class kos_connection(telnetlib.Telnet):

    def __init__(self, *args, cpu=1, **kwargs):
        telnetlib.Telnet.__init__(self, *args, **kwargs)

        data = self.read_until(b'>')
        self.write(b'1\n')
        sleep(.2)
        self.write(b'1\n')
        sleep(.2)


    def ks_run(self, scr, *args, volume=1, timeout=1):
        com = f'{volume}:/{scr}.ks'
        com = [com] + list(args)
        com = '", "'.join(com)
        com = f'runpath("{com}").\n'
        self.write(com.encode())

        if timeout:
            sleep(timeout)
            self.ks_stop()

    def ks_stop(self):
        _ = self.read_very_eager()
        sleep(0.1)
        _ = self.write(telnetlib.IP)