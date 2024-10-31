import {IConstants} from "../core/core.config";
import IActionDescriptor = angular.resource.IActionDescriptor;
import IHttpPromise = angular.IHttpPromise;

export interface IMaster extends ng.resource.IResource<IMaster>, pg.models.IMaster {

}
export interface ITask extends ng.resource.IResource<ITask>,  pg.models.ITask {

}
export interface IScheduler  extends pg.models.IScheduler {

}

export interface IMasterResource extends ng.resource.IResourceClass<IMaster> {
    addTask(params:{id:string}, task:any):ITask;
    updateTask(params:{id:string}, task:any):ITask;
    deleteTask(params:{id:string,taskId:string}):IMaster;
    getTasks(params:{id:string ,start:any,end:any}):ITask[];
}

export let MasterResourceName = 'MasterResource';

MasterResource.$inject = ['$resource', 'constants'];
export function MasterResource($resource:ng.resource.IResourceService, constants:IConstants) {
    let addTaskDescriptor:IActionDescriptor = {
        method: "POST",
        params: {id: '@id'},
        url: `${constants.apiUrl}/master/:id/task`,

    };
    let updateTaskDescriptor:IActionDescriptor = {
        method: "PUT",
        params: {id: '@id'},
        url: `${constants.apiUrl}/master/:id/task`,

    };
    let deleteTaskDescriptor:IActionDescriptor = {
        method: "DELETE",
        params: {id: '@id', taskIdId: '@taskId'},
        url: `${constants.apiUrl}/master/:id/task/:taskId`
    };
    let getTasksDescriptor:IActionDescriptor = {
        method: "GET",
        params: {id: '@id', start: '@start',end: '@end'},
        url: `${constants.apiUrl}/master/:id/tasks/:start/:end`,
        isArray: true,
    };
    return <IMasterResource>$resource( `${constants.apiUrl}/master/:id`, {id: '@_id'},
        {
            addTask: addTaskDescriptor,
            updateTask: updateTaskDescriptor,
            deleteTask: deleteTaskDescriptor,
            getTasks: getTasksDescriptor
        } );
}