import {Component, ElementRef, ViewChild} from 'angular2/core';
import {Router, Route, RouteConfig, ROUTER_DIRECTIVES} from 'angular2/router';

import {Home} from './components/home/home';
import {About} from './components/about/about';
import {DynamoLinks} from './components/dynamo-links/dynamo-links';
import {DynamoIdeaBox} from './components/dynamo-idea-box/dynamo-idea-box';
import {DynamoTweets} from './components/dynamo-tweets/dynamo-tweets';
import {DynamoPictures} from './components/dynamo-pictures/dynamo-pictures';

@Component({
  selector: 'dynamo-page',
  providers: [],
  templateUrl: 'app/dynamo-page.html',
  styleUrls: ['app/dynamo-page.css'],
  directives: [ROUTER_DIRECTIVES],
  pipes: []
})
@RouteConfig([
  new Route({ path: '/home', component: Home, name: 'Home', useAsDefault: true}),
  new Route({ path: '/about', component: About, name: 'About'}),
  new Route({ path: '/dynamo-links', component: DynamoLinks, name: 'DynamoLinks'}),
  new Route({ path: '/dynamo-idea-box', component: DynamoIdeaBox, name: 'DynamoIdeaBox'}),
  new Route({ path: '/dynamo-tweets', component: DynamoTweets, name: 'DynamoTweets'}),
  new Route({ path: '/dynamo-pictures', component: DynamoPictures, name: 'DynamoPictures'})
])
export class DynamoPage {

  @ViewChild('navlist') navList: ElementRef;

  constructor() {}

  toggleMobileNav(){
    var navListElement = this.navList.nativeElement;
    var currentClass = navListElement.getAttribute('class');
    if(currentClass.indexOf('nav-list-active')>-1){
      navListElement.setAttribute('class',currentClass.replace('nav-list-active',''));
    }
    else{
      navListElement.setAttribute('class',currentClass +' nav-list-active');
    }
  }

}
