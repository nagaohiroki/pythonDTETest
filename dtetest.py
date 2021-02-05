import win32com.client
dte = win32com.client.GetActiveObject('VisualStudio.DTE')
filename = 'D:/work/UE4/MyProject/Source/MyProject/TestWidget.cpp'
# dte.ItemOperations.OpenFile(filename)
# dte.ActiveDocument.Selection.MoveToLineAndOffset(5, 5)
dte.Debugger.Breakpoints.Add("", filename, 5)
