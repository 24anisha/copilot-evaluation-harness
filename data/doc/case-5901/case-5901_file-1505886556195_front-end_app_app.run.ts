import {IRootScope} from "../typings";
import {SeoPageResourceName, ISeoPageResource} from "./resources/seo.page.resource";


appRun.$inject = ['$rootScope', '$timeout', '$mdMedia'];
export function appRun($rootScope: IRootScope, $timeout, $mdMedia) {

    $rootScope.socialParams = {
        host: "",
        target: "",
        title: "",
        image: "",
        description: ""
    };
    $rootScope.loading = false;
    $rootScope.seoBase = "PALAMAR GROUP ";
    $rootScope.seo = {
        description: "Студія краси та навчальний центр для працівників салонів краси. м. Львів",
        description_ru: "Салон красоты и учебный центр для работников салонов красоты. м. Львов",
        title: "PALAMAR GROUP beauty parlour & academy "
    }
    ;
    $rootScope.isBigSize = $mdMedia('gt-lg');


    $rootScope.$on('$routeChangeStart', function () {
        //show loading gif
        $timeout(()=> {
            $rootScope.loading = true;
        }, 1);
    });

    $rootScope.$on('$routeChangeSuccess', function () {
        //hide loading gif
        $timeout(()=> {
            $rootScope.loading = false;


        }, 5);


    });

    $rootScope.$on('$routeChangeError', function () {
        //hide loading gif
        $timeout(()=> {
            $rootScope.loading = false;
        }, 1);

    });
}