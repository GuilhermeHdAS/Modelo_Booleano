
arquivobase = open("base.txt","w")
base = arquivobase.write("a.txt\nb.txt\nc.txt")
arquivobase.close()

arquivoconsulta = open("consulta.txt","w")
consulta = arquivoconsulta.write("casa & amor | casa & !mora")
arquivoconsulta.close()

arquivo1 = open("a.txt","w")
arq1 = arquivo1.write("Era uma CASA muito \nengracada. Não tinha teto, \nnão tinha nada.")
arquivo1.close()

arquivo2 = open("b.txt","w")
arq2 = arquivo2.write("quem casa quer casa. \nQUEM não mora em \ncasa, também quer casa!")
arquivo2.close()

arquivo3 = open("c.txt","w")
arq3 = arquivo3.write("quer casar comigo, amor? \nquer casar comigo, \nfaça o favor! \nmora na minha casa!")
arquivo3.close()
