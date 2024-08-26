import pikepdf

old_pdf=pikepdf.Pdf.open("Ashish Resume_09-08.pdf") //write the path of the file which you want to encrypt

no_extr=pikepdf.Permissions(extract=False)

old_pdf.save("pass_encry.pdf", encryption=pikepdf.Encryption(user="123asd",owner="ashish",allow=no_extr)) //write new pdf name
