#
# makefile v0.1.1 for qrdecoder v0.1.2
# Template written by Martin Plicka
# <http://mplicka.cz/en/blog/compiling-ui-and-resource-files-with-pyqt>
#
# Description:
# ------------
#    Compile all .ui & .qrc files into .py files
#
# Dependencies:
# -------------
#   - GNU make for GNU/linux <http://www.gnu.org/software/make/>
#   - or GnuWin for Windows <http://gnuwin32.sourceforge.net/packages/make.htm>
#
# Directions:
# -----------
#   - Install Gnu make or GnuWin
#   - If in Windows, add C:\Program Files\GnuWin\bin to path
#   - Run the following command in the source dir:
#       make
# 
# Changelog:
# ----------
#  Version 0.1.1 (12-16-2011)
#   - Removed ".bat" from "PYUIC = pyuic4.bat"
#
#  Version 0.1 ()
#   - Initial Release
#
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

###### EDIT ##################### 
#Directory with ui and resource files
RESOURCE_DIR = src/resources
 
#Directory for compiled resources
COMPILED_DIR = src/ui
 
#UI files to compile
UI_FILES = mainwindow.ui aboutwindow.ui

#Qt resource files to compile
RESOURCES = images.qrc
 
#pyuic4 and pyrcc4 binaries
PYUIC = pyuic4
PYRCC = pyrcc4
 
#################################
# DO NOT EDIT FOLLOWING
 
COMPILED_UI = $(UI_FILES:%.ui=$(COMPILED_DIR)/ui_%.py)
COMPILED_RESOURCES = $(RESOURCES:%.qrc=$(COMPILED_DIR)/%_rc.py)
 
all : resources ui 

resources : $(COMPILED_RESOURCES) 
 
ui : $(COMPILED_UI)
 
$(COMPILED_DIR)/ui_%.py : $(RESOURCE_DIR)/%.ui
	$(PYUIC) $< -o $@
 
$(COMPILED_DIR)/%_rc.py : $(RESOURCE_DIR)/%.qrc
	$(PYRCC) $< -o $@
 
clean : 
	$(RM) $(COMPILED_UI) $(COMPILED_RESOURCES) $(COMPILED_UI:.py=.pyc) $(COMPILED_RESOURCES:.py=.pyc) 
