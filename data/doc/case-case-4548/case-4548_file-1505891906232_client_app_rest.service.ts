import { environment } from "../environments/environment";
import { RestangularModule } from "ngx-restangular";
import { ModuleWithProviders } from "@angular/core";


const APP_HEADERS = {};
const token = null;
const watchAuth = (): void => {
  APP_HEADERS["Authorization"] = (token) ? `bearer ${token}` : undefined;
};

/**
 * Function for setting the default restangular configuration.
 * API url, set authorization header if needed
 */
export function RestangularConfigFactory(RestangularProvider): void {
  watchAuth();

  RestangularProvider.setBaseUrl(environment.apiUrl);
  RestangularProvider.addFullRequestInterceptor((element, operation, path, url, headers, params): any => {
    return {
      headers: Object.assign({}, headers, APP_HEADERS)
    }
  });
};

/**
 * Module with configuration that will be used for calling the server
 * @type {ModuleWithProviders}
 */
export const APIModule: ModuleWithProviders = RestangularModule.forRoot([], RestangularConfigFactory);