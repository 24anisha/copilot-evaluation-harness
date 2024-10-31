import {
  Directive
  , HostListener
  , HostBinding
  , ElementRef
  , Renderer
} from '@angular/core';

@Directive({
  selector: '[HighlightMouse]'
})
export class HighlightMouseDirective {

  @HostListener("mouseenter")
  onMouseOver() {
    /* this._renderer.setElementStyle(
       this._elementoRef.nativeElement,
       "background-color",
       "yellow"
     )
     */

    this.backgroundColor = 'yellow'
  }
  @HostListener("mouseleave")
  onMouseLeave() {
    /* this._renderer.setElementStyle(
       this._elementoRef.nativeElement,
       "background-color",
       "transparent"
     )*/

    this.backgroundColor = 'transparent'
  }


  //@HostBinding("style.backgroundColor") backgroundColor:string;
  @HostBinding("style.backgroundColor") get setColor() {
    
    return this.backgroundColor;
  }
  private backgroundColor: string;


  constructor(
    /*private _elementoRef: ElementRef
    , private _renderer: Renderer*/) {

  }


}