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

 
 
Sub moderate()
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



Sub moderate1()
Dim OpenPrice As Double
Dim ClosePrice As Double

'Count the number of stocks'
NumberStockRow = Cells(Rows.Count, 9).End(xlUp).Row

'Count the number of observations'
NumberObservation = Cells(Rows.Count, 1).End(xlUp).Row

'Assign the StartRow from 2'
StartRow = 2

'Make a loop to get the ClosePrice-OpenPrice and the Percent Change for each Stock'
For i = 2 To NumberObservation:
    If Cells(i, 1).Value = Range("I" & StartRow).Value Then
    OpenPrice = Cells(i, 3).Value
    ClosePrice = Range("K" & StartRow).Value
    Range("L" & StartRow) = ClosePrice - OpenPrice
        If OpenPrice = 0 Then
        Range("L" & StartRow) = 0
        Else
        Range("L" & StartRow) = (ClosePrice - OpenPrice) / OpenPrice * 100 & "%"
        End If
    StartRow = StartRow + 1
    End If

Next i
End Sub





