import { Injectable } from '@angular/core';
import { Http } from '@angular/http';
import { xhrHeaders } from '../xhr-headers';

import { lessonsData } from '../data/lessons';

@Injectable()
export class LessonsService {
	
	lessons = [];

	constructor(private http:Http) {
		this.http = http;
		this.loadLessons();
	}

	loadLessons() {
		this.http.get('http://localhost:3000/lessons')
			.map(res => res.json())
			.subscribe(
				lessonsData => this.lessons = lessonsData,
				err => console.error("Error occurred:", err)
			);
	}

	createLesson(description) {
		const lesson = {description};
		this.lessons.push(lesson);
		this.http.post('http://localhost:3000/lessons', JSON.stringify(lesson), xhrHeaders())
			.subscribe(
				() => {},
				err => console.error(err)
			);
	}

	deleteLesson(lessonId) {
		const index = this.lessons.findIndex(
			lesson => lesson.id === lessonId
		);
		this.lessons.splice(index, 1);
		this.http.delete(`http://localhost:3000/lessons/${lessonId}`, xhrHeaders())
			.subscribe(
				() => {},
				err => console.error(err)
			);
	}

}