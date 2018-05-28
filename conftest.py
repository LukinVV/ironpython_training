import pytest
import os.path
import json
from fixture.application import ApplicationHelper
import clr

clr.AddReferenceByName(
    'Microsoft.Office.Interop.Excel, Version=15.0.0.0, Culture=neutral, PublicKeyToken=71e9bce111e9429c')
from Microsoft.Office.Interop import Excel

fixture = None
target = None

@pytest.fixture()
def app(request):
    global fixture
    web_config = load_config(request.config.getoption("--target"))
    if fixture is None:
        fixture = ApplicationHelper(web_config["app_path"])
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.close_app()

    request.addfinalizer(fin)
    return fixture



def load_from_xlsx(f):
    file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/%s.xlsx" % f)
    excel = Excel.ApplicationClass()
    workbook = excel.Workbooks.Open(file)
    sheet = workbook.ActiveSheet
    data = []
    rows_with_test_data = sheet.UsedRange.Rows.Count
    for i in range(rows_with_test_data):
        data.append(str(sheet.Range["A%s" % (i + 1)].Value2))
    workbook.Close(SaveChanges=False)
    excel.Quit()
    return data


def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("xlsx_"):
            testdata = load_from_xlsx(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])


def load_config(conf):
    global target
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), conf)
        with open(config_file) as f:
            target = json.load(f)
    return target

def pytest_addoption(parser):
    parser.addoption("--target", action="store", default="target.json")