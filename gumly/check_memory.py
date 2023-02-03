import os, psutil


class Memory:
    """
    Class to catpure and show information about the memory used by the 
    current program.
    It can log the infomation using a logging object or print it.
    It has three options of memory measurement unity: KB, MB and GB.
    If the argument 'debug' is False, the 'log' method will do nothing.
    """

    def __init__(self, logging=None, unity='GB', debug=True):
        self.baseline = psutil.Process(os.getpid()).memory_info().rss
        self.total = psutil.virtual_memory()[0]
        self.logging = logging
        self.conv = {
            'MB': lambda x: x/1024 ** 2,
            'KB': lambda x: x/1024,
            'GB': lambda x: x/1024 ** 3
        }
        self.unity = unity if unity in self.conv.keys() else 'MB'
        self.debug = debug if type(debug) is bool else True

    def get(self):
        return psutil.Process(os.getpid()).memory_info().rss - self.baseline

    def text(self, x, unity=None):

        unity = unity if unity in self.conv.keys() else self.unity
        msg = f"{self.conv[unity](x):.2f} {unity}s"
        return msg

    def log(self, text, header='MEMO', unity=None):
        
        if self.debug:
            unity = unity if unity in self.conv.keys() else self.unity
            total = self.text(self.total, unity)
            mem = self.get()
            ptotal = self.text(mem + self.baseline, unity)
            frac = (mem + self.baseline)/self.total * 100
            m = self.text(self.get(), unity)
            msg = f"{header}: {text}: {m} | {frac:.2f}% ({ptotal} / {total})"
            
            if self.logging is not None:
                self.logging.info(msg)
            else:
                print(msg)

    

if __name__ == '__main__':
    
    import logging
    import numpy as np

    logging.basicConfig(level=logging.INFO)
    m = Memory(logging, 'MB')

    m.log('begin', 'MEMO INIT')
    l = list()
    for i in range(100):
        x = np.random.rand(100,100)
        l.append(i + len(x))
        
        if i == 0 or i == 50 or i == 99:
            m.log(f'i = {i}')