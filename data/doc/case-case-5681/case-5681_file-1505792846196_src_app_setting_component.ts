import { Component, OnInit } from "@angular/core";

import {
  AppConfiguration,
  AppNavigation,
  AppSideDrawer,
  AppUtilization,
  AppFileSystem,
  AppHttp
} from "../shared";

import { getString, setString } from "tns-core-modules/application-settings";

@Component({
  selector: "setting",
  moduleId: module.id,
  templateUrl: "./component.html",
  // styleUrls:["./component.scss"],
  providers:[]
})

export class SettingComponent implements OnInit {
  private actionTitle:string="Setting";
  constructor(
    private nav:AppNavigation,
    private utl:AppUtilization
  ) {
    // NOTE: ?
  }
  ngOnInit(): void {
    // setString('language','3');
    // let test = getString('language');
    // console.log(test);
    // console.log(JSON.stringify(Config.books));
  }
}


/*
https://docs.nativescript.org/ns-framework-modules/application-settings
import * as Application from "tns-core-modules/application";
import * as applicationModul from "tns-core-modules/application";
import { getString, setString } from "application-settings";

export class BackendService {

    static isLoggedIn(): boolean {
        return !!getString("token");
    }

    static get token(): string {
        return getString("token");
    }

    static set token(theToken: string) {
        setString("token", theToken);
    }
}
*/