import {Component, OnInit, ViewChild } from '@angular/core';
import { ModalComponent } from 'ng2-bs3-modal/ng2-bs3-modal';

import { ColegiosService } from '../../../../../services/sistema/ficha/colegios.service'
import {Colegio} from "../colegio";

@Component({
  selector: 'app-ver-colegio',
  templateUrl: 'ver-colegio.component.html',
  styleUrls: ['ver-colegio.component.css']
})
export class VerColegioComponent implements OnInit {
  @ViewChild('modal')
  modal: ModalComponent;

  private colegios = [
    {"id":1},
  ];
  selectedColegio_id: number;

  constructor(
    private colegiosService: ColegiosService,
  ) { }

  getColegios() {
    this.colegiosService.getColegios().subscribe((response) => {this.colegios = response})
  }

  ngOnInit(): void {
    this.getColegios();
  }

  indexOfObj(id: number): number {
    for (let i = 0; i < this.colegios.length; i++) {
      if ( this.colegios[i].id == id) {
        return i;
      }
    }
    return -1;
  }

  modalOpen(id: number): void {
    this.modal.open();
    this.selectedColegio_id = id;
  }

  modalClose(id: number): void {
    this.deleteColegio(id);
  }

  modalDismiss(): void {
    this.modal.dismiss();
  }


  deleteColegio(id: number): void {
    this.colegiosService.deleteColegio(id).subscribe(()=>{
      let index = this.indexOfObj(id);
      this.colegios.splice(index,1);
      this.modal.close();
      this.selectedColegio_id = null;
    });
  }

}