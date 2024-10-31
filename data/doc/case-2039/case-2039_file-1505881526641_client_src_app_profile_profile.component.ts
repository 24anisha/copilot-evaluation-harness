import { Component, OnInit, Input, Pipe, PipeTransform } from '@angular/core';
import { Router } from '@angular/router';
import { AuthService } from '../auth.service';
import { RecoService } from '../reco.service';
import { MyFilterPipe } from '../filter.pipe';

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.css'],
})

export class ProfileComponent implements OnInit {

  user: any;
  recos: any = [];

  constructor(
    private router: Router,
    private authService: AuthService,
    private recoService: RecoService
  ) { }


  ngOnInit() {
    if(!localStorage.getItem('user')) {
      this.router.navigate(['/']);
    }

    this.user = JSON.parse(localStorage.getItem('user'));

    this.recoService.getRecos().subscribe(recos => {
      this.recos = recos;
    });

  }

}