/**
 * Copyright 2014 Mozilla Foundation
 * 
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 * 
 * http://www.apache.org/licenses/LICENSE-2.0
 * 
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
// Class: GraphicsBitmapFill
module Shumway.AVMX.AS.flash.display {
  import notImplemented = Shumway.Debug.notImplemented;
  import axCoerceString = Shumway.AVMX.axCoerceString;
  export class GraphicsBitmapFill extends ASObject implements IGraphicsFill, IGraphicsData {
    
    // Called whenever the class is initialized.
    static classInitializer: any = null;

    // List of static symbols to link.
    static classSymbols: string [] = null; // [];
    
    // List of instance symbols to link.
    static instanceSymbols: string [] = null; // ["bitmapData", "matrix", "repeat", "smooth"];
    
    constructor (bitmapData: flash.display.BitmapData = null, matrix: flash.geom.Matrix = null, repeat: boolean = true, smooth: boolean = false) {
      super();
      this.bitmapData = bitmapData;
      this.matrix = matrix;
      this.repeat = !!repeat;
      this.smooth = !!smooth;
    }
    
    // JS -> AS Bindings
    
    bitmapData: flash.display.BitmapData;
    matrix: flash.geom.Matrix;
    repeat: boolean;
    smooth: boolean;
    
    // AS -> JS Bindings
    
  }
}