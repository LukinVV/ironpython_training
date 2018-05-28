import clr
import sys
import os.path

project_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
sys.path.append(os.path.join(project_dir, "TestStack.White.0.13.3\\lib\\net40\\"))
sys.path.append(os.path.join(project_dir, "Castle.Core.3.3.0\\lib\\net40-client\\"))
clr.AddReferenceByName('TestStack.White')

from TestStack.White import Application
from TestStack.White.InputDevices import Keyboard
from TestStack.White.WindowsAPI import KeyboardInput
from TestStack.White.UIItems.Finders import *

clr.AddReferenceByName('UIAutomationTypes, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35')
from System.Windows.Automation import *
from fixture.group import GroupHelper


class ApplicationHelper:

    def __init__(self, app_path):
        self.group = GroupHelper(self)
        self.application = Application.Launch(app_path)
        self.main_window = self.application.GetWindow('Free Address Book')

    def close_app(self):
        self.main_window.Get(SearchCriteria.ByAutomationId("uxExitAddressButton")).Click()
