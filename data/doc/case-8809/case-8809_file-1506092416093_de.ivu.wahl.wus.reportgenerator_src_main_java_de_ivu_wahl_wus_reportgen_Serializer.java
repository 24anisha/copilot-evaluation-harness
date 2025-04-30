/*
 * Serializer
 * 
 * Created on 28.01.2009
 * Copyright (c) 2009 Kiesraad
 */
package de.ivu.wahl.wus.reportgen;

import java.io.File;
import java.io.FileOutputStream;

import javax.xml.transform.OutputKeys;
import javax.xml.transform.Source;
import javax.xml.transform.Transformer;
import javax.xml.transform.TransformerFactory;
import javax.xml.transform.TransformerFactoryConfigurationError;
import javax.xml.transform.stream.StreamResult;

public class Serializer {
  public void serialize(Source src, File emlFile) throws TransformerFactoryConfigurationError {
    try {
      FileOutputStream out = new FileOutputStream(emlFile);
      StreamResult streamResult = new StreamResult(out);
      TransformerFactory tf = TransformerFactory.newInstance();
      Transformer serializer = tf.newTransformer();
      serializer.setOutputProperty(OutputKeys.ENCODING, "UTF-8"); //$NON-NLS-1$
      serializer.setOutputProperty(OutputKeys.INDENT, "yes"); //$NON-NLS-1$
      serializer.transform(src, streamResult);
    } catch (Exception e) {
      e.printStackTrace();
      throw new RuntimeException(e);
    }
  }


}