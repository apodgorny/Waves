from display import Display
from Source import Source
from Waves import Waves
import Colors

display = Display(800, 600, 'Waves', Colors.BLACK)

waves = Waves()
source1 = Source(300, 300, 20)
source2 = Source(500, 400, 30)
source3 = Source(700, 500, 50)
source2.animate_to(501, 100, 1)

display.add(source1)
display.add(source2)
display.add(source3)
display.add(waves, -20)
display.surface.fill(Colors.GRAY122)
display.start()