Sub Easy1()
'Set a variable to cycle through the worksheets
   
'Set variable to hold the ticker symbol
  Dim Ticker As String
  
  'Set variable to hold total volume of stock traded
  Dim TotalVolume As Double
  TotalVolume = 0
  
  Dim StartRow As Long
  StartRow = 2
  
  'Set variable for total rows to loop through
  Dim lastrow As Long
  lastrow = Cells(Rows.Count, "A").End(xlUp).Row
  Dim PrintRow As Long
  PrintRow = StartRow
  
  'Assign the columns that contain Ticker and Total Stock Volume'
    Range("I1").Value = "Ticker"
    Range("J1").Value = "Total Stock Volume"
    
 'Loop to search through ticker symbols
  For i = 2 To lastrow
  
    If Cells(i, 1).Value = Cells(i + 1, 1).Value Then
        TotalVolume = TotalVolume + Cells(i + 1, 7).Value
    Else
        Ticker = Cells(i, 1).Value
        Range("I" & PrintRow).Value = Ticker
        Range("J" & PrintRow).Value = TotalVolume
        PrintRow = PrintRow + 1
        TotalVolume = 0
    End If
 Next i
End Sub