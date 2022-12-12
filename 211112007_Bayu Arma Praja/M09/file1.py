class WrittenText:
    
    def __init__(self, text):
        self._text = text
        
    def render(self):
        return self._text
    
class UnderlineWrapper(WrittenText):
    
    def __init__(self, wrapped):
        self._wrapped = wrapped
        
    def render(self):
        return "<u>{}</u>".format(self._wrapped.render())
    
class BoldWrapper(WrittenText):
    
    def __init__(self, wrapped):
        self._wrapped = wrapped
        
    def render(self):
        return "<b>{}</b>".format(self._wrapped.render())
    
awal = WrittenText("Hai Apa Kabar?")
print(f"Awal = {awal.render()}")
akhir = UnderlineWrapper(awal)
print(f"Akhir = {akhir.render()}")
akhir1 = BoldWrapper((UnderlineWrapper)(awal))
print(f"Akhir = {akhir1.render()}")