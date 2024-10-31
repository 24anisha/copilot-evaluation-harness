/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.biblio.web.rest.util;

import com.google.zxing.WriterException;
import com.itextpdf.text.Document;
import com.itextpdf.text.DocumentException;
import com.itextpdf.text.Image;
import com.itextpdf.text.Paragraph;
import com.itextpdf.text.pdf.PdfWriter;
import java.awt.Graphics2D;
import java.io.ByteArrayOutputStream;

import java.io.FileOutputStream;
import java.io.IOException;
import java.util.Date;
import javax.imageio.ImageIO;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

/**
 *
 * @author kouwonou
 */
public class PdfBulder {



    public void buildPdf() throws WriterException {
        GenerateQRCode ge = new  GenerateQRCode();
        Document document = new Document();
        try {
          ge.createQRImage("ddddd", 125);
            PdfWriter.getInstance(document,
                    new FileOutputStream("Image.pdf"));
            document.open();
            ByteArrayOutputStream baos = new ByteArrayOutputStream();
            Image image1 = Image.getInstance("watermark.png");
            ImageIO.write( ge.createQRImage("1254", 0), "jpg", baos );
            Image image= Image.getInstance(baos.toByteArray());
            document.add(image);


            document.close();
        } catch (DocumentException | IOException e) {
        }
    }
}