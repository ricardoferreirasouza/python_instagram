import os
import win32com.client as client

excel = client.Dispatch("excel.application")

for file in os.listdir(os.getcwd() + "/old version/"):
    filename, fileextension = os.path.splitext(file)
    wb = excel.Workbooks.Open(os.getcwd() + "/old version/" + file)
    output_path = os.getcwd() + "/new version/" + filename
    wb.SaveAs(output_path, 51)
    wb.Close()

excel.Quit()
