import { AppStore } from './../core/store/app-store';
import { Action } from '@ngrx/store';
import { CoursesActionTypes } from './';
import { Course } from './shared';

export function coursesReducer(state: Course[], action: Action) {
  switch (action.type) {
    case CoursesActionTypes.ADD_COURSES:
      return action.payload;
    case CoursesActionTypes.RESET_COURSES:
      return [];
    case CoursesActionTypes.CREATE_COURSE:
      return [...state, action.payload];
    case CoursesActionTypes.UPDATE_COURSE:
      return state
        .map((course: Course) => course.id === action.payload.id ? action.payload : course);
    case CoursesActionTypes.DELETE_COURSE:
      return state.filter((course: Course) => course.id !== action.payload);
    default:
      return state;
  }
}