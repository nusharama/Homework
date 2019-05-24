Sub moderate3()
'Set variable to hold the ticker symbol
  Dim Ticker As String
  
  'Set variable to hold total volume of stock traded
  Dim YearlyChange As Double
  YearlyChange = 0
  
  Dim OpenPrice As Double
  Dim ClosePrice As Double

  Dim StartRow As Long
  StartRow = 2
  
  'Set variable for total rows to loop through
  Dim lastrow As Long
  lastrow = Cells(Rows.Count, "A").End(xlUp).Row
  Dim PrintRow As Long
  PrintRow = StartRow

    'Assign the columns that contain Yearly Change and Percent Change'
    Range("K1").Value = "Yearly Change"
    Range("L1").Value = "Percent Change"
    
 'Loop to search through ticker symbols
  For i = 2 To lastrow
  
    If Cells(i, 1).Value <> Cells(i + 1, 1).Value Then
        ClosePrice = Cells(i, 6).Value
        Range("K" & PrintRow).Value = ClosePrice
        PrintRow = PrintRow + 1
        TotalVolume = 0
    End If
 Next i
 End Sub