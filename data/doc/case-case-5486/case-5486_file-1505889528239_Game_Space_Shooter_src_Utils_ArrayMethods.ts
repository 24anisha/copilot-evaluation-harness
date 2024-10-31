/**
 * @description Class containing methods affecting arrays
 */
class ArrayMethods {
    /**
     * @description Check if an array contains a certain value
     * @param list
     * @param obj
     */
    static containsObject(list: any, obj: any): boolean {
        for (var i = 0; i < list.length; i++) {
            if (list[i] === obj) {
                return true;
            }
        } return false;
    }
    /**
     * @description Remove a value from an array
     * @param list
     * @param obj
     */
    static removeObject(list: any, obj: any) {
        for (var i = 0; i < list.length; i++) {
            if (list[i] === obj) {
                list.splice(i, 1);
            }
        }
    }
}