import { Injectable, Inject } from '@angular/core';
import {
  Http,
  Request,
  Response,
  Headers,
  XHRBackend,
  RequestOptions,
  RequestOptionsArgs
} from '@angular/http';
import { Observable } from 'rxjs/Observable';
import 'rxjs/add/operator/map';
import 'rxjs/add/operator/catch';

@Injectable()
export class AuthorizedHTTPService extends Http {
  private static USER_KEY: string = 'AMP-token';
  private static API_ENDPOINT: string = 'http://amt-server.herokuapp.com';
  constructor(backend: XHRBackend, options: RequestOptions) {
    let token = localStorage.getItem('AMP-token'); // your custom token getter function here
    options.headers.set('Authorization', token);
    super(backend, options);
  }

  public request(url: string | Request, options?: RequestOptionsArgs): Observable<Response> {
    let token = localStorage.getItem(AuthorizedHTTPService.USER_KEY);
    if (typeof url === 'string') { // meaning we have to add the token to the options, not in url
      url = AuthorizedHTTPService.API_ENDPOINT + url;
      if (!options) {
        // let's make option object
        options = { headers: new Headers() };
      }
      options.headers.set('Authorization', token);
    } else {
      // we have to add the token to the url object
      url.url = AuthorizedHTTPService.API_ENDPOINT + url.url;
      url.headers.set('Authorization', token);
    }
    return super.request(url, options)
      .catch(this.catchAuthError(this));
  }

  private catchAuthError(self: AuthorizedHTTPService) {
    // we have to pass HttpService's own instance here as `self`
    return (res: Response) => {
      console.log(res);
      if (res.status === 401 || res.status === 403) {
        // if not authenticated
      }
      return Observable.throw(res);
    };
  }
}