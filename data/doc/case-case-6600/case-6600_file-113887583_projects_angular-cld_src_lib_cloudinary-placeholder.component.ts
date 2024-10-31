import {
  AfterContentChecked,
  Component,
  HostBinding,
  Input,
  ElementRef,
  Renderer2,
} from '@angular/core';
import {Cloudinary} from './cloudinary.service';
import { SDKAnalyticsConstants }  from './SDKAnalyticsConstants';

@Component({
  selector: 'cl-placeholder',
  template: `<img [src]="this.placeholderImg">`
  ,
})
export class CloudinaryPlaceHolder implements AfterContentChecked {
  @Input('type') type: string;
  @HostBinding('style.width') itemWidth;
  @HostBinding('style.height') itemHeight;
  @HostBinding('attr.public-id') publicId;

  options: object = {};
  placeholderImg: string;

  constructor(private cloudinary: Cloudinary, private renderer: Renderer2, private el: ElementRef) {}

  setWidth(width) {
    this.itemWidth = width;
  }

  setHeight(height) {
    this.itemHeight = height;
  }

  setPublicId(id) {
    this.publicId = id;
  }

  ngAfterContentChecked() {
    const imageTag = this.cloudinary.imageTag(this.publicId, this.options);
    this.setElementAttributes(this.el.nativeElement.children[0], imageTag.attributes());
    this.placeholderImg = this.getPlaceholderImage();
  }

  getPlaceholderImage() {
    if (this.type === 'predominant-color' && this.itemHeight && this.itemWidth) {
      return this.cloudinary.url(this.publicId, {placeholder: 'predominant-color-pixel' || true, ...this.options});
    } else {
      return this.cloudinary.url(this.publicId, {placeholder: this.type || true, ...this.options});
    }
  }

  setElementAttributes(element, attributesLiteral) {
    Object.keys(attributesLiteral).forEach(attrName => {
      if (attrName !== 'src' && attrName !== 'style') {
        this.renderer.setAttribute(element, attrName, attributesLiteral[attrName]);
      }
    });
  }
}