from qtpyvcp.widgets.form_widgets.main_window import VCPMainWindow
### Supports the @Slot decorator to solve property type issues.
from qtpy.QtCore import Slot
from qtpy.QtWidgets import QAbstractButton

# Setup logging
from qtpyvcp.utilities import logger
LOG = logger.getLogger('qtpyvcp.' + __name__)

class MyMainWindow(VCPMainWindow):
    """Main window class for the VCP."""
    def __init__(self, *args, **kwargs):
        super(MyMainWindow, self).__init__(*args, **kwargs)
        self.vtk.enable_panning(True)
        self.vtk.setViewZ()
        
        # signal connections.
        self.btn_right_table_marker.clicked.connect(self.btn_right_table_marker_clicked)
        self.btn_saddle_front_marker.clicked.connect(self.btn_saddle_front_marker_clicked)

    # add any custom methods here
    @Slot(QAbstractButton)
    def on_patternGroup_buttonClicked(self, button):
        self.pattern.setValue(button.property('pattern'))
    
    def btn_right_table_marker_clicked(self):
        # calc distance of not positin from G54 0
        # put that distance into 'xtravel' double spin
        self.xtravel.setValue(abs(float(self.dro_G5x_table.text())))
    
    def btn_saddle_front_marker_clicked(self):
        self.ytravel.setValue(abs(float(self.dro_G5x_saddle.text())))