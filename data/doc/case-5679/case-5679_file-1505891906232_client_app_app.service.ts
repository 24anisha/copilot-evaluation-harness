import { Injectable } from "@angular/core";

import { Restangular } from "ngx-restangular";
import { DatatableSortType } from "ng2-md-datatable";

import { Page, PagedProducts, Product, Sort } from "./app.interface";
import { Observable } from "rxjs/Observable";


@Injectable()
export class AppService {

  constructor(private api: Restangular) {
  }

  public getData(page: Page, sorts: Sort[], search: string): Observable<PagedProducts> {
    let query:any = {};
    query.search = search || "";
    query.limit = page.size;
    query.offset = page.pageNumber * page.size;
    if (!sorts || sorts.length == 0) {
      query.sort = "_created";
    } else {
      let sort: Sort = sorts[0];
      query.sort = `${(sort.dir === "asc" ? "" : "-")}${sort.prop}`;
    }

    return Observable.fromPromise(Promise.all([
      this.api.all("products").getList(query).toPromise().then(data => data, () => []),
      this.api.all("products").get("count", query).toPromise().then(data => data, () => { return {count: 0}; })
    ])).map(data => this.getPagedProducts(data[0], page, sorts, search, data[1].count));
  }

  public updateData(product: Product): Observable<Product> {
    let id = product._id;
    product._id = undefined;
    if (!id) {
      return this.api.all("products").customPOST(product);
    } else {
      return this.api.all("products").one(id).customPUT(product);
    }
  }

  public createData(product: Product): Observable<Product> {
    product._id = undefined;
    return Observable.of(this.api.all("products").customPOST(product));
  }

  private getPagedProducts(data: any, page: Page, sorts: Sort[], search: string, count: number): PagedProducts {
    page.totalElements = count;
    let pagedData: PagedProducts = {
      products: data,
      page: page,
      sorts: sorts,
      search: search,
    };

    return pagedData;
  }

}