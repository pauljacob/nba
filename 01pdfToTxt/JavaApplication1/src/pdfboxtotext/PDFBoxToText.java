/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package pdfboxtotext;

import java.io.IOException;
import java.util.logging.Level;
import java.util.logging.Logger;
import java.io.File;
import java.io.FileWriter;
import java.io.PrintWriter;

/**
 *
 * @author Paul
 */
public class PDFBoxToText {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {

        try{
            PDFManager pdfManager = new PDFManager();
            
            String fpath = "D:\\Google Drive\\pauljacob.dataanalyst\\ahgain3\\201910";
            Integer fpathlength = fpath.length();
            Integer fpathlengthminus = fpathlength - 6;
            String fpath2 = fpath.substring(0, fpathlengthminus);

            File folder = new File(fpath);
            File[] listOfFiles = folder.listFiles();

            for (int i = 0; i < listOfFiles.length; i++) {
              if (listOfFiles[i].isFile()) {
                System.out.println("File " + listOfFiles[i].getName());
                String pdfFileName = listOfFiles[i].getName();
                String fp = fpath+ "\\" + pdfFileName;
                int numba = pdfFileName.length();
                numba = numba - 4;
                
                pdfManager.setFilePath(fp);
                String text = pdfManager.toText();
                
                String txtFileName = pdfFileName.substring(0, numba) + ".txt";
                System.out.println(txtFileName);
                //anotherStringy1
                
                File file = new File(txtFileName);
                
                
                //String daFolder = "D:\\Google Drive\\pauljacob.dataanalyst\\ahgain2\\" + pdfFileName.substring(0,6) + "txt";
                //File tmpDir = new File(daFolder);
                //boolean exists = tmpDir.exists();
                //if(exists){
                    
                //} else{
                    //make folder here <<<<<<<<<<<=============================
                //}
                
                /////////////////////////////////////
                String daFolder = fpath2 + "\\" + pdfFileName.substring(0,6) + "txt";
                File file2 = new File(daFolder);
                if (!file2.exists()) {
                    if (file2.mkdir()) {
                        System.out.println("Directory is created!");
                    } else {
                        System.out.println("Failed to create directory!");
                    }
                }


                PrintWriter pw = new PrintWriter(daFolder + "\\" + file);
                pw.println(text);
                //pw.println(100000);
                pw.close();
                System.out.println("Done");
                
              } else if (listOfFiles[i].isDirectory()) {
                System.out.println("Directory " + listOfFiles[i].getName());
              }
            }
            
            




            } catch (IOException ex) {
                System.err.println(ex.getMessage());
                ex.printStackTrace();
                //Logger.getLogger(PDFBoxReadFromFile.class.getName()).log(Level.SEVERE, null, ex);
            }
    
        
    
}
}
