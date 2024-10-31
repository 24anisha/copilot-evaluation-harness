/**
 * Created by matias on 05-01-17.
 */
import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'abbreviate'
})
export class AbbreviatePipe {
  transform(value: string): string {
    let valueArr = value.split(' ');
    let res: string = '';
    for (let sub of valueArr){
      if(sub.length < 4){
        res = res + sub;
      }
      else {
        res = res + sub.substr(0,3)
      }
    }
    return res;
  }
}