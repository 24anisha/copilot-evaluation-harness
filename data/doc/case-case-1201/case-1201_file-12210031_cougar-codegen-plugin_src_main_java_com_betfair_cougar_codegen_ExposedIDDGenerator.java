/*
 * Copyright 2014, The Sporting Exchange Limited
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package com.betfair.cougar.codegen;

import org.w3c.dom.Document;

import javax.xml.transform.Source;
import javax.xml.transform.Transformer;
import javax.xml.transform.TransformerFactory;
import javax.xml.transform.dom.DOMSource;
import javax.xml.transform.stream.StreamResult;
import javax.xml.transform.stream.StreamSource;
import java.io.File;
import java.io.FileOutputStream;

public class ExposedIDDGenerator {

    public static void transform(Document iddDoc, File xslFile, File iddFile) throws Exception {

        DOMSource source = new DOMSource(iddDoc);

        Source xslSource = new StreamSource(xslFile);

        TransformerFactory factory = TransformerFactory.newInstance();
        Transformer trans = factory.newTransformer(xslSource);

        trans.transform(source, new StreamResult(new FileOutputStream(iddFile)));
    }
}
