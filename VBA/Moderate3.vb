Sub Moderate1()
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
'Make a loop to highlight to Yearly Change'

    If Cells(i, 11).Value > 0 Then
    Cells(i, 11).Interior.ColorIndex = 4
    ElseIf Cells(i, 11).Value < 0 Then
    Cells(i, 11).Interior.ColorIndex = 3
    Else
    Cells(i, 11).Interior.ColorIndex = 0
End If
Next i
End Sub