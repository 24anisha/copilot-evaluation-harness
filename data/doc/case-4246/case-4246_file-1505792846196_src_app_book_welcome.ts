import { Component, AfterViewInit,OnInit } from "@angular/core";
import { ObservableArray } from "tns-core-modules/data/observable-array";
import {Page} from "ui/page";

import {
  AppConfiguration,
  AppSideDrawer,
  AppActionBar,
  AppNavigation,
  AppUtilization,
  AppFileSystem,
  AppHttp
} from "../shared";

import { BookModel, BookService } from "./service";

@Component({
  selector:'eba',
  moduleId: module.id,
  templateUrl: "./welcome.html"
})

export class WelcomeComponent implements OnInit {
  private actionItemVisibility:string="collapsed";
  private actionTitle:string="Effortless bible analysis";

  constructor(
    private page: Page,
    private actionBar: AppActionBar,
    private sideDrawer: AppSideDrawer,
    private bookService: BookService,
    private nav: AppNavigation
  ) {
    // NOTE: ?
    this.page.actionBarHidden = true;
  }
  ngOnInit() {
  }
  // NOTE: (tap)="itemButton($event)"
  itemButton(bookId: number) {
    this.bookService.lId = bookId;
    this.nav.to(['section']);
  }
  get dataItems(): ObservableArray<BookModel> {
    return this.bookService.lang;
  }
}