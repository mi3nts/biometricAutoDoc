import fitz


def createCoverPage():
    
    #SETTING UP
    doc = fitz.open()
    page = doc.newPage()
    
    #FORMATTING
    headerRect = fitz.Rect(70, 160, 500, 700)
    subHeaderRect = fitz.Rect(70, 330, 500, 700)
    infoRect = fitz.Rect(70, 420, 500, 700)
    namesRect = fitz.Rect(70, 600, 500, 700)
    
    border = fitz.Rect(10,10,585,830)
    border2 = fitz.Rect(20,20,575,820)
    
    #TEXT
    header = "Automated Documentation to Extract Learning from EEG (ADELE)"
    subHeader = "UTD - MINTS"
    infoText = "2020/06/04 T05"
    namesText = "Cristian Garces, Rami Jaber, Bradley Krakar, Jesse Ladyman"
    

    #TEXTBOXES
    rc = page.insertTextbox(headerRect, header,
                        align=fitz.TEXT_ALIGN_CENTER, 
                        fontsize = 35)

    rc = page.insertTextbox(subHeaderRect, subHeader,
                        align=fitz.TEXT_ALIGN_CENTER, 
                        fontsize = 20)
        
    rc = page.insertTextbox(infoRect, infoText,
                        align=fitz.TEXT_ALIGN_CENTER, 
                        fontsize = 20)
    
    rc = page.insertTextbox(namesRect, namesText,
                        align=fitz.TEXT_ALIGN_CENTER, 
                        fontsize = 15)

    #BORDER 
    shape = page.new_shape()
    #DRAWING THE RECTANGLES
    shape.draw_rect(border)
    shape.draw_rect(border2)
    #COMMITTING
    shape.finish()
    shape.commit()

    
    
    doc.save("finished.pdf")

#CALLING THE FUNCTION
createCoverPage()
