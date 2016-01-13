# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import os

from conexion import bd
from fpdf import FPDF

def imprimir(fac,mat,dni):
    pdf = FPDF()
    pdf.add_page()
    header(pdf,fac,mat,dni)
    pdf.output('prueba.pdf','F')
    os.system('/usr/bin/evince prueba.pdf')
    
        
def header(pdf,fac,mat,dni):
    cursor = bd.cursor()

    cursor.execute(""" SELECT fechafac FROM facturas WHERE idfac=?""", (fac,))
    datos=cursor.fetchall()
    for fila in datos:
        fecha=fila[0]
    
    pdf.set_font('Arial','B',12)
    pdf.cell(60,10,'TALLERAUTO',0,1,'C')
    pdf.set_font('Arial','',10)
    pdf.cell(60,10,'Calle Senra, 12  Marin (Pontevedra)',0,1,'L')
    pdf.cell(60,10,'36911 Tlfo: 986 882 211-656 565 918',0,1,'L')
    pdf.image('car.png',170,10,25,25,'png','')
    pdf.line(5,40,200,40)
    pdf.set_font('Times','B',12)    
    pdf.cell(50,10,'Fecha %s ' % fecha,0,0,'L')
    pdf.cell(130,10,'Factura numero: %s ' % fac,0,1,'R')
    pdf.cell(60,10,'DATOS CLIENTE:',0,1,'L')
    cursor.execute(""" SELECT dnicli, apelcli, nomcli, dircli, poblic, procli, cpcli FROM clientes WHERE dnicli=?""", (dni,))
    datos = cursor.fetchall()
    for fila in datos:
        pdf.cell(30,10,'%s' % fila[1],0,0,'L')
        pdf.cell(30,10,'%s' % fila[2],0,1,'L')
        pdf.cell(20,10,'%s' % fila[3],0,0,'L')
        pdf.cell(50,10,'%s' % fila[4],0,0,'R')
        pdf.cell(90,10,'Matricula Vehiculo: %s' %mat,0,1,'R')
        pdf.cell(30,10,'%s' % fila[6],0,0,'L')
        pdf.cell(60,10,'%s' % fila[5],0,1,'L')
    pdf.line(5,100,200,100)
    total=0
    cursor.execute(""" SELECT idv, conceptov, preciov FROM ventas WHERE idfac=?""", (fac,))
    datosv = cursor.fetchall()
    datosv = filter(None, datosv)
    pdf.cell(30,10,'ID',0,0,'L')
    pdf.cell(140,10,'Concepto',0,0,'L')
    pdf.cell(20,10,'Precio',0,1,'R')
    for fila in datosv:
        pdf.cell(30,10,'%s' % fila[0],0,0,'L')
        pdf.cell(140,10,'%s' % fila[1],0,0,'L')
        pdf.cell(20,10,'%s' % fila[2],0,1,'R')
        total+=float(fila[2])
    pdf.line(5,120,200,120)
    pdf.cell(30,10,'IVA',0,0,'L')
    pdf.cell(160,10,'%s' % (total*0.21),0,1,'R')

    pdf.cell(30,10,'Total',0,0,'L')
    pdf.cell(145,10,'%s' % (total*1.21),0,0,'R')

    pdf.cell(15,10,'Euros',0,1,'R')

        
    
    
    
    
