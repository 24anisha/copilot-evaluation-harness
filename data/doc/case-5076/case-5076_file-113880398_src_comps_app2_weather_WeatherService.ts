import {Injectable} from '@angular/core';
import {Http, RequestOptions, URLSearchParams} from '@angular/http';
import {Observable} from 'rxjs/Observable';
import 'rxjs/add/operator/do';
import 'rxjs/add/observable/empty'
import 'rxjs/add/observable/empty'
import {IWeatherItem} from "./IWeather";

@Injectable()
export class WeatherService {
    static BASE_URL: string = 'https://secure.digitalsignage.com/Weather/';

    constructor(private http: Http) {
    }

    search(query: string): Observable<any> {

        // use .let() as a way to reuse Observable functions
        function processWeather(showToConsole) {
            return (source) =>
                source
                    .do(() => {
                        if (showToConsole)
                            console.log(`Showing weather`)
                    }).map((e) => {
                    var items: Array<IWeatherItem> = e[0].data.weather;
                    return items;
                })
        }

        // if you wish to use ?q=param_here you can use
        //const search:URLSearchParams = new URLSearchParams();
        //search.set('q', query);
        //return this.http.get(`${WeatherService.BASE_URL}`, new RequestOptions({search}))

        // do is a great way to trace for debugging Observables
        return this.http
            .get(`${WeatherService.BASE_URL}${query}`)
            .map((res: any) => res.json())
            .let(processWeather(true))
            .catch(function (e) {
                return Observable.empty();
            });
        //.map((item: Array<{item: IWeatherItem}>) => item.map((item: {show: IWeatherItem}));
    }
}